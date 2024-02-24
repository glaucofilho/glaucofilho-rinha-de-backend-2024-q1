import json

from starlette.middleware.base import (
    BaseHTTPMiddleware,
    RequestResponseEndpoint,
)
from starlette.requests import Request
from starlette.responses import Response


class DebugParamsMiddleware(BaseHTTPMiddleware):
    """
    Middleware para depuração que registra os detalhes das solicitações e respostas em um arquivo de log.

    Este middleware é responsável por registrar os detalhes de cada solicitação recebida e a resposta
    correspondente em um arquivo de log chamado "log.log". Ele decodifica o corpo da solicitação como
    JSON, se possível, e registra todos os detalhes relevantes, incluindo o método HTTP, URL, cabeçalhos,
    parâmetros de consulta, corpo da solicitação e corpo da resposta.

    Métodos:
    - dispatch: Intercepta cada solicitação recebida e registra seus detalhes antes de passá-la adiante
                para o próximo middleware ou rota.
    """

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        """
        Intercepta a solicitação e registra os detalhes antes de passá-la adiante.

        Este método é chamado automaticamente para cada solicitação recebida pelo aplicativo.
        Ele registra os detalhes da solicitação e, em seguida, passa a solicitação adiante
        para ser processada pelos middlewares e rotas subsequentes.

        Parâmetros:
        - request: O objeto Request representando a solicitação recebida.
        - call_next: O próximo endpoint de solicitação-resposta a ser chamado após o processamento
                     deste middleware.

        Retorna:
        - Response: A resposta resultante após o processamento da solicitação pelo aplicativo.
        """
        # Registra detalhes da requisição
        body = await request.body()
        try:
            body_str = json.loads(body.decode())
        except json.JSONDecodeError:
            body_str = "Não foi possível decodificar o body para JSON."

        save_str = f"\nMÉTODO: {request.method}"
        save_str += f"\nURL: {request.url}"
        save_str += f"\nCABEÇALHOS: {request.headers}"
        save_str += f"\nQUERY: {request.query_params}"
        save_str += f"\nCORPO: {body_str}"

        # Obtém a resposta
        response = await call_next(request)

        # Garante que a resposta seja totalmente lida
        body = b""
        async for chunk in response.body_iterator:
            body += chunk
        response_body_str = body.decode()

        # Registra a resposta
        save_str += f"\nRESPOSTA: {response_body_str}"
        save_str += "\n________________________________"

        # Escreve os logs em um arquivo
        with open("log.log", "a") as file:
            file.write(save_str)

        # Cria uma nova resposta para enviar de volta ao cliente
        new_response = Response(
            content=body,
            status_code=response.status_code,
            headers=dict(response.headers),
        )
        return new_response
