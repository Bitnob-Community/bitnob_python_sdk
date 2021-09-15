import os
import requests
from requests.exceptions import HTTPError, ConnectionError
from .exceptions import exception_class, BitnobBadKeyError, BitnobRequiredParamError


class Bitnob:
    """
    Base Bitnob class
    """

    def __init__(self):
        self.BITNOB_LIVE_URL = 'https://api.bitnob.co/api/v1'
        self.BITNOB_SANDBOX_URL = 'https://sandboxapi.bitnob.co/api/v1'

    def env_key_handler(self):
        self.api_key = os.environ.get("BITNOB_API_KEY")
        self.production = os.environ.get("BITNOB_PRODUCTION")
        if self.api_key is None:
            raise BitnobBadKeyError()
        if self.production is None or self.production == True:
            self.base_url = self.BITNOB_LIVE_URL
        else:
            self.base_url = self.BITNOB_SANDBOX_URL

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
                exception = exception_class.get(data["statusCode"])
                raise exception(data["message"])
            except KeyError:
                return data
        except (HTTPError, ConnectionError) as e:
            return e
    
    def check_required_params(self, required_param, passed_param):
        for key in passed_param.keys():
            if key not in required_param:
                added_message = "The following are required " + ",".join(required_param)
                raise BitnobRequiredParamError(f'{key} is required!' + added_message)
                

def pagination_filter(**kwargs):
    return "&".join([f"{k}={v}" for k, v in kwargs.items()])
        