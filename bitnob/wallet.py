from bitnob.base import Bitnob


class Wallet(Bitnob): 
    
    def wallet_balance(self, body:dict):
        return self.send_request("GET", "/wallets")

    def get_transaction(self, transaction_id):
        return self.send_request("GET", f"/transactions/{transaction_id}")
    
    def list_transactions(self, body:dict):
        return self.send_request("POST", "/transactions/?order=ASC&page=2&take=10", json=body)