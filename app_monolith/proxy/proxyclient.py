import httpx
from shared.exceptions import ce_timeout

class cproxyclient:
    def __init__(self):
        self.client= httpx.AsyncClient(timeout=10)

    async def send(self, method, url, headers=None, body=None, params=None):
        res= None
        try:
            res= await self.client.request(method= method, url= url, headers= headers, content= body, params= params, timeout=10)
        except httpx.TimeoutException as e:
            raise ce_timeout() from e
        return res

    async def close(self):
        await self.client.aclose()

