from bitnob.base import Bitnob, pagination_filter
from .model import LNURL


class LNURL(Bitnob): 
    def __generate_ln_url_object(self, data):
        return LNURL(
            id=data["id"], 
            tld = data["tld"],
            identifier = data["identifier"],
            identifier_type = data["identifier_type"],
            ln_url = data["ln_url"],
            ln_url_QR = data["ln_url_QR"],
            sat_min_sendable = data["sat_min_sendable"],
            sat_max_sendable = data["sat_max_sendable"]
        )

    def create_lnurl(self, body):
        """
        Create LNURL/Address

        body = {
            "identifier": "satoshi",
            "tld": "bitcoin.org",
            "identifierType": "username",
            "customerEmail": "satoshi@bitcoin.org",
            "satMinSendable": 1,
            "satMaxSendable": 1000000
        }

        required_data = "identifier", "tld", "customerEmail"

        - POST Request
        """
        required_data = ["identifier", "tld", "customerEmail"]
        self.check_required_datas(required_data, body)
        response = self.send_request("POST", "lnurl", json=body)
        return self.__generate_ln_url_object(data=response.get("data"))

    def decode_lnurl(self, encoded_lnurl):
        """
        Decode LnUrl

        encoded_lnurl

        - POST Request
        """
        body = {
            "encodedLnurl": encoded_lnurl
        }
        response = self.send_request("POST", "lnurl", json=body)
        return response

    def pay_lnurl(self, body:dict):
        """
        Paying lnurl

        body = {
            "encodedLnUrl": "LNURL1DP68GURN8GHJ7UM5V9NKJMN894SHQ6FWVEKX7AM9WF6X7UPW0PUH5TEWWAJKCMPDDDHX7AMW9ACXKTNP8QMNSE3WV4JRXC3SX3JRGERZXYERJCFNVG6KZTMVDE6HYMRS9AEKZAR0WD5XJJE6N7Y",
            "satoshis": 1000,
            "reference": "reference",
            "customerEmail": "satoshi@bitcoin.org",
            "comment": "comment",
        }

        required_data = "encodedLnUrl", "reference", "satoshis", "customerEmail"

        - POST Request
        """
        required_data = ["encodedLnUrl", "reference", "satoshis", "customerEmail"]
        self.check_required_datas(required_data, body)

        response = self.send_request("POST", "lnurl/paylnurl", json=body)
        return response
    

    def create_ln_withdrawal(self, body:dict):
        """
        create ln-withdrawal

        body = {
            "customerEmail": "satoshi@bitcoin.org",
            "description": "Have some gifts for the holidays",
            "satoshis": 1000
        }

        required_data = "description", "satoshis", "customerEmail"

        - POST Request
        """
        required_data =  ["description", "satoshis", "customerEmail"]
        self.check_required_datas(required_data, body)

        response = self.send_request("POST", "lnurl/createLnUrlWithdrawal", json=body)
        return response
    
    def decode_lnaddress(self, ln_address):
        """
        Decode lnaddress

        encoded_lnurl

        - POST Request
        """
        body = {
            "lnAddress": ln_address
        }
        response = self.send_request("POST", "lnurl/decodelnaddress", json=body)
        return response
    
    def pay_lnaddress(self, body:dict):
        """
        Paying lnaddress

        body = {
            "lnAddress": "satoshi@bitcoin.org",
            "satoshis": 10,
            "reference": "testpayment",
            "customerEmail": "satoshi@bitnob.com"
        }

        required_data = "encodedLnUrl", "reference", "satoshis", "customerEmail"

        - POST Request
        """
        required_data = ["lnAddress", "reference", "satoshis", "customerEmail"]
        self.check_required_datas(required_data, body)

        response = self.send_request("POST", "lnurl/paylnaddress", json=body)
        return response
    
    def list_lnurls(self, **kwargs):
        """
        Listing lnurls

        order = (optional) Result order. Accepted values: `DESC` (default), ASC
        page = (optional) Result page.
        take = (optional) Number of results per request. Accepted values: 0 - 100. Default 10
        
        - GET Request
        """
        url_params = None
        if kwargs != {}:
            url_params = pagination_filter(kwargs=kwargs)
        response = self.send_request("GET", f"lnurl/?{url_params}")
        data = response["data"]["lnUrls"]
        return [self.__generate_ln_url_object(ln_data) for ln_data in data]
    
    def get_lnurl(self, lnurl_id):
        """
        Getting LNURL using lnurl_id

        - GET Request
        """
        response =  self.send_request("GET", f"lnurl/{lnurl_id}")
        return response
    
    def get_lnurl_by_identifier(self, username):
        """
        Getting a user lnurl by their username
        username = "satoshi"

        - GET Request
        """
        response =  self.send_request("GET", f"lnurl/fetchlnurl/{username}")
        return self.__generate_ln_url_object(data=response.get("data"))
    
    def update_lnurl(self, body:dict, lnurl_id):
        """
        Updating LNURL
        body = {
            "identifier": "satoshi",
            "tld": "bitcoin.org",
            "identifierType": "username",
            "customerEmail": "satoshi@bitcoin.org",
            "satMinSendable": 1,
            "satMaxSendable": 1000000
        }

        - PUT Request
        """
        response =  self.send_request("PUT", f"lnurl/{lnurl_id}", json=body)
        return self.__generate_ln_url_object(data=response.get("data"))