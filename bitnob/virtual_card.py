from bitnob.base import Bitnob, pagination_filter


class VirtualCard(Bitnob): 
    
    def register_card_user(self, body:dict):
        """
        Registering a Card User to access Virtual Card

        body = {
            customerEmail: "customer@gmail.com",
            idNumber: "gauddksdop0ao",
            idType: "hahhahhajaja",
            firstName: "gsgsgsgsgsgs",
            lastName: "ggahagaga",
            city: "Lagos"
            state: "Lagos"
            country: "Nigeria",
            zipCode: "520231"
            line1: "2349021534385"
            amount: 1000
        }

        - POST Request
        """
        required_data = ["customerEmail", "idNumber", "idNumber", "firstName", "lastName", "city", "state", "country", "zipCode", "line1"]
        self.check_required_datas(required_data, body)
        
        return self.send_request("POST", "virtualcards/registercarduser", json=body)
    
    def create_card(self, email:str):
        """
        Create Card for customer

        email = customer@gmail.com
        """
        body = {
            "email" : email
        }
        return self.send_request("POST", "virtualcards/create", json=body)
    
    def top_up(self, body:dict):
        """
        Top Up Card
        body = {
            customerEmail: "customer@gmail.com",
            cardId: "d1cbc518-95d6-4bf2-a0f4-e6a33ee09603",
            amount: 1000
        }
        """
        return self.send_request("POST", "virtualcards/credit", json=body)

    def withdraw(self, body:dict):
        """
        Withdraw from Card for customer

        body = {
            customerEmail: "customer@gmail.com",
            cardId: "d1cbc518-95d6-4bf2-a0f4-e6a33ee09603",
            amount: 1000
        }
        """
        return self.send_request("POST", "virtualcards/withdraw", json=body)
    
    def mock_transaction(self, body:dict):
        """
        Mock transaction(works only on sandbox)
        body = {
            cardId: "d1cbc518-95d6-4bf2-a0f4-e6a33ee09603",
            amount: 1000,
            type: deduct
        }
        """
        return self.send_request("POST", "virtualcards/mock-transaction", json=body)

    def freeze_card(self, card_id:str):
        """
        Freeze Card

        card_id = d1cbc518-95d6-4bf2-a0f4-e6a33ee09603
        """
        body = {
            "cardId" : card_id
        }
        return self.send_request("POST", "virtualcards/freeze", json=body)
    
    def unfreeze_card(self, card_id:str):
        """
        Unfreeze Card

        card_id = d1cbc518-95d6-4bf2-a0f4-e6a33ee09603
        """
        body = {
            "cardId" : card_id
        }
        return self.send_request("POST", "virtualcards/unfreeze", json=body)
    
    def block_card(self, card_id:str):
        """
        Block Card

        card_id = d1cbc518-95d6-4bf2-a0f4-e6a33ee09603
        """
        body = {
            "cardId" : card_id
        }
        return self.send_request("POST", "virtualcards/block", json=body)
    
    def unblock_card(self, card_id:str):
        """
        Unblock Card

        card_id = d1cbc518-95d6-4bf2-a0f4-e6a33ee09603
        """
        body = {
            "cardId" : card_id
        }
        return self.send_request("POST", "virtualcards/unblock", json=body)
    
    def terminate_card(self, card_id:str):
        """
        Unfreeze Card

        card_id = d1cbc518-95d6-4bf2-a0f4-e6a33ee09603
        """
        body = {
            "cardId" : card_id
        }
        return self.send_request("POST", "virtualcards/terminate", json=body)
    


    def list_cards(self, **kwargs):
        """
        Listing all cards

        order = (optional) Result order. Accepted values: `DESC` (default), ASC
        page = (optional) Result page.
        take = (optional) Number of results per request. Accepted values: 0 - 100. Default 10
        
        - GET Request
        """
        url_params = None
        if kwargs != {}:
            url_params = pagination_filter(**kwargs)
        return self.send_request("GET", f"virtualcards/cards/?{url_params}")
    
    def list_card_transactions(self, card_id, **kwargs):
        """
        Listing card transactions

        card_id = d1cbc518-95d6-4bf2-a0f4-e6a33ee09603

        order = (optional) Result order. Accepted values: `DESC` (default), ASC
        page = (optional) Result page.
        take = (optional) Number of results per request. Accepted values: 0 - 100. Default 10
        
        - GET Request
        """
        url_params = None
        if kwargs != {}:
            url_params = pagination_filter(**kwargs)
        return self.send_request("GET", f"virtualcards/cards/{card_id}/transactions/?{url_params}")
    
    
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
            url_params = pagination_filter(**kwargs)
        return self.send_request("GET", f"virtualcards/cards/transactions/?{url_params}")

    
    def get_card(self, card_id):
        """
        Getting Card using card_id
        card_id = d1cbc518-95d6-4bf2-a0f4-e6a33ee09603

        - GET Request
        """
        return self.send_request("GET", f"virtualcards/card/{card_id}")
    
    
    def list_card_users(self, **kwargs):
        """
        Listing all Card Users

        order = (optional) Result order. Accepted values: `DESC` (default), ASC
        page = (optional) Result page.
        take = (optional) Number of results per request. Accepted values: 0 - 100. Default 10
        
        - GET Request
        """
        url_params = None
        if kwargs != {}:
            url_params = pagination_filter(**kwargs)
        return self.send_request("GET", f"virtualcards/carusersds/?{url_params}")