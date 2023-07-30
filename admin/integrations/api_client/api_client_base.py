import httpx
from furl import furl


class RequestTypes:
    get = 'get'
    post = 'post'


class ApiClientBase:
    def __init__(self, host: str) -> None:
        self.host = host

    def url_create(self, path: str, parameters=None) -> str:
        if parameters is None:
            parameters = {}

        f = furl(
            scheme='https',
            netloc=self.host,
            path=path,
        )
        f.set(args=parameters)
        return f.url

    def request(
            self,
            path: str,
            parameters: dict,
            data: dict = None,
            token: str | None = None,
            type: str = RequestTypes.get,
    ):
        with httpx.Client() as session:
            url = self.url_create(
                path=path,
                parameters=parameters,
            )
            headers = {}
            if token:
                headers['Authorization'] = 'Bearer {token}'.format(
                    token=token,
                )
            response = {}

            if type == RequestTypes.get:
                response = session.get(
                    url=url,
                    headers=headers,
                )

            elif type == RequestTypes.post:

                # form_data = aiohttp.FormData()
                # for name, value in data.items():
                #     form_data.add_field(name=name, value=value)

                response = session.post(
                    url=url,
                    data=data,
                    headers=headers,
                )
            response = response.json()
            return response

    def get(self, path: str, parameters=None, token: str = None):
        if parameters is None:
            parameters = {}
        response = self.request(
            type=RequestTypes.get,
            path=path,
            token=token,
            parameters=parameters,
        )
        return response

    def post(self, path: str, parameters=None, data=None, token: str = None):
        if parameters is None:
            parameters = {}
        if data is None:
            data = {}
        response = self.request(
            type=RequestTypes.post,
            path=path,
            token=token,
            parameters=parameters,
            data=data,
        )
        return response
