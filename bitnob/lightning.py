from bitnob.base import Bitnob


class Lightning(Bitnob): 
    
    def create_invoice(self, body:dict):
        return self.send_request("POST", "/wallets/ln/createinvoice", json=body)

    def pay_invoice(self, body:dict):
        return self.send_request("POST", "/wallets/ln/pay", json=body)
    
    def initiate_payment(self, body:dict):
        return self.send_request("POST", "/wallets/ln/initiatepayment", json=body)
    
    def decode_payment_request(self, body:dict):
        return self.send_request("POST", "/wallets/ln/decodepaymentrequest", json=body)
    
    def get_invoice(self, body:dict):
        return self.send_request("POST", "/wallets/ln/getinvoice", json=body)