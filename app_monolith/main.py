# app/main.py

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from modules.users import router
from router.route import croute, csroute 
from router.router import crouter
from proxy.proxyclient import cproxyclient
from proxy.proxyserver import cproxyserver
from loadbalancer.round_robin import cround_robin
from loadbalancer.load_balancer import cload_balancer
from healthchk.healthchk import chealthchk
from ratelimiter.fixedwindow import cfixedwindow
from ratelimiter.ratelimiter import cratelimiter
from observability.logging_config import configure_logging
from observability.middleware import  RequestLoggingMiddleware
import asyncio
import logging


app = FastAPI(title="My FastAPI Application")

# app.include_router(
#     users_router,
#     prefix="/api/v1",
#     tags=["Users"],
# )



route_list= (croute("/user", [csroute("http://127.0.0.1:8001"), csroute("http://127.0.0.1:8002"), csroute("http://127.0.0.1:8003")]), croute("/order", [csroute("http://127.0.0.1:8004")]))
# route_list= {"/user": [{"http://127.0.0.1:8001": {"heal"}},
# {},
# {}],
# "/order": [{}]}
configure_logging()
router= crouter(route_list)
# Note here cproxyclient can be anything 
lb_strategy= cround_robin()
lb= cload_balancer(lb_strategy)
#
proxyclient= cproxyclient()
hc= chealthchk(route_list, proxyclient)
proxyserver= cproxyserver(router, proxyclient, lb)

fixedwindow= cfixedwindow(1)
ratelimiter= cratelimiter(fixedwindow)
app= FastAPI()

app.add_middleware(RequestLoggingMiddleware)
logger= logging.getLogger("proxy");
@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    if not ratelimiter.chk_allow():
        logger.warning("Rate limit exceeded")
        return JSONResponse(status_code=429, content={"detail": "Too Many Requests"})
    response = await call_next(request)
    return response

@app.api_route("/{path:path}", methods= ["GET", "POST", "PUT", "PATCH", "DELETE"])
async def handle(request: Request, path: str):
    print(ratelimiter.chk_allow())
    print(f"PATH {path} ")
    return await proxyserver.handle(request)

@app.on_event("startup")
async def startup():
    asyncio.create_task(hc.chk_health())

@app.on_event("shutdown")
async def shutdown():
    await proxyclient.close()
