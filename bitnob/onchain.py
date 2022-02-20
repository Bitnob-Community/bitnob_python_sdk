from bitnob.base import Bitnob, pagination_filter


class Onchain(Bitnob): 
    
    def send_bitcoin(self, body:dict):
        """
        Sending bitcoin

        body = {
            "satoshis": 3000,
            "address": "tb1q9h0yjdupyfpxfjg24rpx755xrplvzd9hz2nj7v",
            "customerEmail": "customer@email.com",
            "description": "lorem ipsum",
            "priorityLevel": "high"
        }

        required_data = "satoshis", "address", "customerEmail"

        - POST Request
        """
        required_data = ["satoshis", "address", "customerEmail"]
        self.check_required_datas(required_data, body)

        return self.send_request("POST", "wallets/send_bitcoin", json=body)

    def generate_address(self, body:dict):
        """
        Generate Address for Customer

        body = {
            "label": "purchase xbox",
            "customerEmail": "customer@gmail.com"
        }

        - POST Request
        """
        required_data = ["customerEmail"]
        self.check_required_datas(required_data, body)

        return self.send_request("POST", "addresses/generate", json=body)
    
    def list_addresses(self, **kwargs):
        """
        Getting addresses attached to company

        - POST Request
        """
        url_params = None
        if kwargs != {}:
            url_params = pagination_filter(**kwargs)
        return self.send_request("GET", f"/addresses/?{url_params}",)
    
    def get_recommeded_btc_fes(self):
        return self.send_request("GET", "recommended-fees/btc")