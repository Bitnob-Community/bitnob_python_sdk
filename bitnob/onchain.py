from bitnob.base import Bitnob


class Onchain(Bitnob): 
    
    def send_bitcoin(self, body:dict):
        return self.send_request("POST", "/wallets/send_bitcoin", json=body)

    def generate_address(self, body:dict):
        return self.send_request("POST", "/addresses/generate", json=body)
    
    def list_addresses(self, body:dict):
        return self.send_request("POST", "/addresses/generate", json=body)