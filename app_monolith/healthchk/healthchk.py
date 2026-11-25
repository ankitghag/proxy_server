import asyncio
from fastapi import Request
class chealthchk:
    def __init__(self, routes, reqclient):
        self.routes= routes
        self.reqclient= reqclient

    async def chk_health(self): 
        while True:
            for route in self.routes:
                for server in route.upstream:
                    try:
                        hres= await self.reqclient.send("GET", f"{server.url}/health")
                        if hres.status_code == 200:
                            server.health= True
                            # print(f"HELATHY {server.url} | TRUE ")
                    except Exception:
                            server.health= False
                            # print(f"HELATHY {server.url} | FALSE ")
            await asyncio.sleep(5)

