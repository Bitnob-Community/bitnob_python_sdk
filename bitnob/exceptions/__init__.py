from .exceptions import *

exception_class = {
    400: BadRequestError,
    500: ServerError,
    401: UnauthorizedError,
    429: RateLimitError,
    404: QueryError,
}