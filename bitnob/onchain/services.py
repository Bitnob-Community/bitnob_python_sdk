from bitnob.base import Bitnob, pagination_filter
from bitnob.model import WalletAddress, Transaction


class Onchain(Bitnob): 

    def __generate_address_object(self, data):
        return WalletAddress(
            address = data.get("address"),
            address_type=data.get("addressType"),
            label=data.get("label")
        )
    
    def __generate_transaction_object(self, data):
        return Transaction(            
            reference = data.get("reference"),
            description = data.get("description"),
            amount = data.get("amount"),
            sat_amount = data.get("satAmount"),
            fees = data.get("fees"),
            btc_fees = data.get("btcFees"),
            sat_fees = data.get("satFees"),
            action = data.get("action"),
            transaction_type = data.get("type"),
            status = data.get("status"),
            id=data.get("id"),
            invoice_id=data.get("invoiceId"),
            channel=data.get("channel"),
            address=data.get("address"),
            payment_request=data.get("paymentRequest"),
            spot_price=data.get("spotPrice"),
            hash=data.get("hash"),
            confirmations=data.get("confirmations")
        )

    
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

        response = self.send_request("POST", "wallets/send_bitcoin", json=body)
        return self.__generate_transaction_object(data=response["data"])

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

        response = self.send_request("POST", "addresses/generate", json=body)
        return self.__generate_address_object(data=response["data"])
    
    def list_addresses(self, **kwargs):
        """
        Getting addresses attached to company

        - POST Request
        """
        url_params = None
        if kwargs != {}:
            url_params = pagination_filter(**kwargs)
        response =  self.send_request("GET", f"/addresses/?{url_params}",)
        data = response.get("data")
        return [self.__generate_address_object(address_data) for address_data in data]
    
    def get_recommeded_btc_fes(self):
        return self.send_request("GET", "recommended-fees/btc")