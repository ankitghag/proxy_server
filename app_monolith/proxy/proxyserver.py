from fastapi import Request
from fastapi.responses import Response
from shared.exceptions import ce_timeout
class cproxyserver:
    def __init__(self, router, proxyclient, lb):
        self.router= router
        self.proxyclient= proxyclient
        self.lb= lb

    async def handle(self, req):
        req_route= self.router.get_upstream_server(req.url.path)
        rto= None
        reqbody= await req.body()
        if req_route:
            for i in range(3):
                lserver= self.lb.get_server(req_route.upstream)
                # url= f"{req_route.upstream}{req.url.path}"
                if lserver:
                    url= f"{lserver.url}{req.url.path}"
                    print(f"REDIRECT {url}")
                    try:
                        response= await self.proxyclient.send(req.method, url, dict(req.headers), reqbody, req.query_params)
                        rto= Response(content= response.content, status_code= response.status_code, headers= dict(response.headers))
                        break
                    except ce_timeout as e:
                        print(f"EXC {e}")
                        lserver.health= False
                        self.lb.decrease_index()
                        continue
                        # rto= Response(content= "Timeout Error", status_code= response.status_code, headers= dict(response.headers))
                elif i == 0:
                    rto= Response(content= "No server is up",status_code= 503)
                    break
            if not rto:
                rto= Response(content= "All upstream servers timeout", status_code= 504)
        else:
            rto= Response(content= "Route not found", status_code= 404)
        return rto
