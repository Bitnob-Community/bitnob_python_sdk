from .exceptions import *

exception_class = {
    400: BitnobBadRequestError,
    500: BitnobServerError,
    401: BitnobUnauthorizedError,
    429: BitnobRateLimitError,
    404: BitnobQueryError,
}