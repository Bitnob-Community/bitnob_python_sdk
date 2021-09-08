from bitnob.base import Bitnob


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

        - POST Request
        """
        return self.send_request("POST", "/wallets/send_bitcoin", json=body)

    def generate_address(self, body:dict):
        """
        Creating lightning invoice for customer

        body = {
            "label": "purchase xbox",
            "customerEmail": "customer@gmail.com"
        }

        - POST Request
        """
        return self.send_request("POST", "/addresses/generate", json=body)
    
    def list_addresses(self, body:dict):
        """
        Getting addresses attached to company

        - POST Request
        """
        return self.send_request("POST", "/addresses/generate", json=body)