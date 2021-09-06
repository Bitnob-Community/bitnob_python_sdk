import os
import requests
from requests.exceptions import HTTPError, ConnectionError
from .exceptions import exception_class, EnvVarsNotSet


class Bitnob:
    """
    Base Bitnob class
    """

    def __init__(self):
        pass

    def env_key_handler(self):
        self.api_key = os.environ.get("api_key")
        # self.base_url = "https://sandboxapp.bitnob.co/api/v1"
        self.base_url = os.environ.get("base_url")
        if self.api_key is None or self.base_url is None:
            raise EnvVarsNotSet()

    def send_request(self, method, path, **kwargs):
        """
        Create a request stub
        :param method:
        :param path:
        :param kwargs:
        :return:
        """
        self.env_key_handler()
        options = {
            "GET": requests.get,
            "POST": requests.post,
            "PUT": requests.put,
            "PATCH": requests.patch,
            "DELETE": requests.delete,
        }
        url = "{}{}".format(self.base_url, path)
        headers = {
            "content-type": "application/json",
            "Authorization": "Bearer {}".format(self.api_key),
        }
        try:
            response = options[method](url, headers=headers, **kwargs)
            data = response.json()
            try:
                data["statusCode"]
                error = exception_class.get(data["statusCode"])
                return error(data["message"])
            except KeyError:
                return data
        except (HTTPError, ConnectionError) as e:
            return e