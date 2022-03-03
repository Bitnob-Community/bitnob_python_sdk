from bitnob.base import Bitnob
from abc import ABC, abstractmethod
from bitnob.stablecoin.model import Receipt
from bitnob.wallet.model import WalletAddress

class StableCoin(ABC):

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def generate_address(self):
        pass

    def generate_address_object(self, data):
        return WalletAddress(
            address = data.get("address"),
            address_type=data.get("addressType"),
            label=data.get("label")
        )
    
    def generate_receipt_object(self, data):
        return Receipt(
            reference = data.get("reference"),
            description = data.get("description"),
            amount = data.get("amount"),
            fees = data.get("fees"),
            action = data.get("action"),
            receipt_type = data.get("type"),
            status = data.get("status"),
            id=data.get("id")
        )
    



class USDC(StableCoin, Bitnob): 
    
    def send(self, body:dict):
        """
        Sending USDC

        body = {
            amount: 3000,
            address: "tb1q9h0yjdupyfpxfjg24rpx755xrplvzd9hz2nj7v",
            chain: "BSC"
            description: "lorem ipsum",
        } 

        - POST Request
        """
        required_data = ["amount", "address", "chain"]
        self.check_required_datas(required_data, body)

        response = self.send_request("POST", "wallets/send-usdc", json=body)
        return self.generate_receipt_object(data=response["data"])


    def generate_address(self, body:dict):
        """
        Generate Address for Customer

        body = {
            "label": "purchase xbox",
            "customerEmail": "customer@gmail.com",
            "chain": "BSC"
        }

        - POST Request
        """
        required_data = ["customerEmail", "chain"]
        self.check_required_datas(required_data, body)

        response =  self.send_request("POST", "addresses/generate/usdc", json=body)
        return self.generate_address_object(data=response["data"])

class USDT(StableCoin, Bitnob): 
    
    def send(self, body:dict):
        """
        Sending USDC

        body = {
            amount: 3000,
            address: "tb1q9h0yjdupyfpxfjg24rpx755xrplvzd9hz2nj7v",
            chain: "BSC",
            description: "lorem ipsum",
        } 

        - POST Request
        """
        required_data = ["amount", "address", "chain"]
        self.check_required_datas(required_data, body)

        response = self.send_request("POST", "wallets/send-usdt", json=body)
        return self.generate_receipt_object(data=response["data"])

    def generate_address(self, body:dict):
        """
        Generate Address for Customer

        body = {
            "label": "purchase xbox",
            "customerEmail": "customer@gmail.com"
            "chain": "BSC"
        }

        - POST Request
        """
        required_data = ["customerEmail", "chain"]
        self.check_required_datas(required_data, body)

        response =  self.send_request("POST", "addresses/generate/usdt", json=body)
        return self.generate_address_object(data=response["data"])