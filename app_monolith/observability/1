import logging
import time
import uuid
from observability.request_context import request_id

access_logger = logging.getLogger("access")
error_logger = logging.getLogger("proxy.middleware")


class RequestLoggingMiddleware:

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):

        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        req_id = str(uuid.uuid4())
        token = request_id.set(req_id)

        method = scope["method"]
        path = scope["path"]

        start_time = time.perf_counter()
        status_code = 500

        async def send_wrapper(message):

            nonlocal status_code

            if message["type"] == "http.response.start":
                status_code = message["status"]

                headers = list(message.get("headers", []))
                headers.append((b"x-request-id", req_id.encode()))
                message["headers"] = headers

            await send(message)

        try:
            await self.app(scope, receive, send_wrapper)

        except Exception:
            error_logger.exception("Request processing failed")
            raise

        finally:
            duration = (time.perf_counter() - start_time) * 1000

            access_logger.info(
                "%s %s %s %.2fms",
                method, path, status_code, duration,
                extra={"request_id": req_id}
            )

            request_id.reset(token)
