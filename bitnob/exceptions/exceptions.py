class BitnobBadKeyError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self):
        self.message = "API Key is not set"
        super().__init__(self.message)

class BitnobServerError(Exception):
    def __init__(self, *args):
        self.message = args[0]
        self.code = 500

    @property
    def response(self):
        return {"status": "error", "name": "BitnobServerError", "code": self.code, "message": self.message}


class BitnobUnauthorizedError(Exception):
    def __init__(self, *args):
        self.message = args[0]
        self.code = 401

    @property
    def response(self):
        return {"status": "error", "name": "BitnobUnauthorizedError", "code": self.code, "message": self.message}


class BitnobQueryError(Exception):
    def __init__(self, *args):
        self.message = args[0]
        self.code = 404

    @property
    def response(self):
        return {"status": "error", "name": "BitnobQueryError", "code": self.code, "message": self.message}


class BitnobRateLimitError(Exception):
    def __init__(self, *args):
        self.message = args[0]
        self.code = 429

    @property
    def response(self):
        return {"status": "error", "name": "P2PError", "code": self.code, "message": self.message}


class BitnobBadRequestError(Exception):
    def __init__(self, *args):
        self.message = args[0]
        self.code = 400

    @property
    def response(self):
        return {"status": "error", "name": "BitnobBadRequestError", "code": self.code, "message": self.message}

class BitnobRequiredParamError(Exception):
    def __init__(self, message):
        super().__init__(message)
