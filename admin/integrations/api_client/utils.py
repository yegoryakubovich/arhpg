class ResponseState:
    successful = 'successful'
    error = 'error'


class Response:
    def __new__(cls, state: str = ResponseState.successful, message: str | None = None, **kwargs):
        json = {
            'state': state,
            **kwargs,
        }
        if message:
            json['message']: message

        return json
