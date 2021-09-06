class EnvVarsNotSet(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self):
        self.message = "API Key or Base URL is not set"
        super().__init__(self.message)

class ServerError(Exception):
    def __init__(self, *args):
        self.message = args[0]
        self.code = 500

    @property
    def response(self):
        return {"status": "error", "name": "ServerError", "code": self.code, "message": self.message}


class UnauthorizedError(Exception):
    def __init__(self, *args):
        self.message = args[0]
        self.code = 401

    @property
    def response(self):
        return {"status": "error", "name": "UnauthorizedError", "code": self.code, "message": self.message}


class QueryError(Exception):
    def __init__(self, *args):
        self.message = args[0]
        self.code = 404

    @property
    def response(self):
        return {"status": "error", "name": "QueryError", "code": self.code, "message": self.message}


class RateLimitError(Exception):
    def __init__(self, *args):
        self.message = args[0]
        self.code = 404

    @property
    def response(self):
        return {"status": "error", "name": "P2PError", "code": self.code, "message": self.message}


class BadRequestError(Exception):
    def __init__(self, *args):
        self.message = args[0]
        self.code = 400

    @property
    def response(self):
        return {"status": "error", "name": "BadRequestError", "code": self.code, "message": self.message}
