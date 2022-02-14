from bitnob.base import Bitnob


class USDC(Bitnob): 
    
    def send_usdc(self, body:dict):
        """
        Sending USDC

        body = {
            amount: 3000,
            address: "tb1q9h0yjdupyfpxfjg24rpx755xrplvzd9hz2nj7v",
            description: "lorem ipsum",
        } 

        - POST Request
        """
        required_data = ["amount", "address"]
        self.check_required_datas(required_data, body)

        return self.send_request("POST", "/wallets/send-usdc", json=body)

    def create_usdc_address(self, body:dict):
        """
        Generate Address for Customer

        body = {
            "label": "purchase xbox",
            "customerEmail": "customer@gmail.com"
        }

        - POST Request
        """
        required_data = ["customerEmail", "labdl"]
        self.check_required_datas(required_data, body)

        return self.send_request("POST", "/addresses/generate", json=body)