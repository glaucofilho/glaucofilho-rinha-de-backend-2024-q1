import json

from starlette.middleware.base import (
    BaseHTTPMiddleware,
    RequestResponseEndpoint,
)
from starlette.requests import Request
from starlette.responses import Response


class DebugParamsMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        # Log request details
        body = await request.body()
        try:
            body_str = json.loads(body.decode())
        except json.JSONDecodeError:
            body_str = "Não foi possível decodificar o body para JSON."

        save_str = f"\nMETHOD: {request.method}"
        save_str += f"\nURL: {request.url}"
        save_str += f"\nHEADERS: {request.headers}"
        save_str += f"\nQUERY: {request.query_params}"
        save_str += f"\nBODY: {body_str}"

        # Get the response
        response = await call_next(request)

        # Ensure the response is fully read
        body = b""
        async for chunk in response.body_iterator:
            body += chunk
        response_body_str = body.decode()

        # Log the response
        save_str += f"\nRESPONSE: {response_body_str}"
        save_str += "\n________________________________"

        # Write logs to a file
        with open("log.log", "a") as file:
            file.write(save_str)

        # Create a new response to send back to the client
        new_response = Response(
            content=body,
            status_code=response.status_code,
            headers=dict(response.headers),
        )
        return new_response
