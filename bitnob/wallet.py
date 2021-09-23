from bitnob.base import Bitnob, pagination_filter


class Wallet(Bitnob): 
    def wallet_detail(self):
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
    
    def list_transactions(self, **kwargs):
        """
        Listing all transactions

        order = (optional) Result order. Accepted values: `DESC` (default), ASC
        page = (optional) Result page.
        take = (optional) Number of results per request. Accepted values: 0 - 100. Default 10
        
        - GET Request
        """
        url_params = None
        if kwargs != {}:
            url_params = pagination_filter(kwargs=kwargs)
        return self.send_request("GET", f"/transactions/?{url_params}")