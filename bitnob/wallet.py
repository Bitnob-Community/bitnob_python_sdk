from bitnob.base import Bitnob


class Wallet(Bitnob): 
    
    def wallet_details(self, body:dict):
        """
        Retrive company wallet details

        - GET Request
        """
        return self.send_request("GET", "/wallets")

    def get_transaction(self, transaction_id):
        """
        Getting a transaction based on transaction_id 

        - GET Request
        """
        return self.send_request("GET", f"/transactions/{transaction_id}")
    
    def list_transactions(self, order=None, page=None, take=None):
        """
        Listing all transactions

        order = (optional) Result order. Accepted values: `DESC` (default), ASC
        page = (optional) Result page.
        take = (optional) Number of results per request. Accepted values: 0 - 100. Default 10
        
        - GET Request
        """
        return self.send_request("GET", "/transactions/?order=ASC&page=2&take=10")