from bitnob.base import Bitnob, pagination_filter
from bitnob.virtual_card.model import VirtualCard, VirtualCardTransaction, VirtualCardUser


class VirtualCardClient(Bitnob):

    def __generate_virtual_card_object(self, data):
        return VirtualCard(
            id = data.get("id"),
            cardNumber=data.get("cardNumber"),
            cardType=data.get("cardType"),
            cardBranch=data.get("cardBranch"),
            cvv= data.get("cvv2"),
            balance=data.get("balance"),
            cardName = data.get("cardName"),
            cardType = data.get("cardType"),
            expiry = data.get("expiry"),
            status = data.get("status"),
            valid = data.get("valid"), 
            last4=data.get("last4"),
            blocked=data.get("blocked"),
            frozen=data.get("frozen"),
        )
    
    def __generate_card_trans_object(self, data):
        return VirtualCardTransaction(
            id = data.get("id"),
            cardId = data.get("cardId"),
            amount = data.get("amount"),
            centAmount = data.get("centAmount"),
            type = data.get("type"),
            currency = data.get("currency"),
            reference = data.get("reference"),

        )
    
    def __generate_card_user_object(self, data):
        return VirtualCardUser(
            id = data.get("id"),
            customerEmail = data.get("customerEmail"),
            firstName = data.get("firstName"),
            lastName = data.get("lastName"),
            countryCode = data.get("countryCode"),
            phoneNumber = data.get("phoneNumber"),
            idType = data.get("idType"),
            idNumber = data.get("idNumber"),
            city = data.get("city"),
            state = data.get("state"),
            country = data.get("country"),
            zipCode = data.get("zipCode"),
            userPhoto = data.get("userPhoto"),
            customerId = data.get("customerId"),
            line1 = data.get("line1"),
            line2 = data.get("line2") or None, 
            kycPassed = data.get("kycPassed")
        )

    def register_card_user(self, body:dict):
        """
        Registering a Card User to access Virtual Card

        body = {
            customerEmail: "customer@gmail.com",
            idNumber: "478haomaaa",
            idType: "NIN",
            firstName: "John",
            lastName: "Doe",
            city: "New York",
            state: "Alabama"
            country: "Nigeria",
            zipCode: "100001", 
            userPhoto:"image.jpg"
            phoneNumber: "08023456789"
            line1: "38 West Street",
            line2: "Apt. 1",
        }

        - POST Request
        """
        required_data = ["customerEmail", "idNumber", "idNumber", "firstName", "lastName", "city", "state", "country", "zipCode", "line1", "phoneNumber", "userPhoto"]
        self.check_required_datas(required_data, body)
        
        response = self.send_request("POST", "virtualcards/registercarduser", json=body)
        return self.__generate_card_user_object(data=response["data"])
        
    def create_card(self, body:dict):
        """
        Create Card for customer

        email = customer@gmail.com
        """
        response = self.send_request("POST", "virtualcards/create", json=body)
        return self.__generate_virtual_card_object(data=response["data"])
    
    def top_up(self, body:dict):
        """
        Top Up Card
        body = {
            customerEmail: "customer@gmail.com",
            cardId: "d1cbc518-95d6-4bf2-a0f4-e6a33ee09603",
            amount: 1000
        }
        """
        response = self.send_request("POST", "virtualcards/topup", json=body)
        return self.__generate_card_trans_object(data=response["data"])        

    def withdraw(self, body:dict):
        """
        Withdraw from Card for customer

        body = {
            customerEmail: "customer@gmail.com",
            cardId: "d1cbc518-95d6-4bf2-a0f4-e6a33ee09603",
            amount: 1000
        }
        """
        response = self.send_request("POST", "virtualcards/withdraw", json=body)
        return self.__generate_card_trans_object(data=response["data"])        
    
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
        response = self.send_request("POST", "virtualcards/freeze", json=body)
        return self.__generate_virtual_card_object(data=response["data"])
    
    def unfreeze_card(self, card_id:str):
        """
        Unfreeze Card

        card_id = d1cbc518-95d6-4bf2-a0f4-e6a33ee09603
        """
        body = {
            "cardId" : card_id
        }
        response = self.send_request("POST", "virtualcards/unfreeze", json=body)
        return self.__generate_virtual_card_object(data=response["data"])
    
    def block_card(self, card_id:str):
        """
        Block Card

        card_id = d1cbc518-95d6-4bf2-a0f4-e6a33ee09603
        """
        body = {
            "cardId" : card_id
        }
        response = self.send_request("POST", "virtualcards/block", json=body)
        return self.__generate_virtual_card_object(data=response["data"])
    
    def unblock_card(self, card_id:str):
        """
        Unblock Card

        card_id = d1cbc518-95d6-4bf2-a0f4-e6a33ee09603
        """
        body = {
            "cardId" : card_id
        }
        response = self.send_request("POST", "virtualcards/unblock", json=body)
        return self.__generate_virtual_card_object(data=response["data"])
    
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
        response = self.send_request("GET", f"virtualcards/cards/?{url_params}")
        data = response["data"]["cards"]
        return [self.__generate_virtual_card_object(card_data) for card_data in data]
    
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
        response = self.send_request("GET", f"virtualcards/cards/{card_id}/transactions/?{url_params}")
        data = response["data"]["cardTransactions"]
        return [self.__generate_card_trans_object(card_transactions) for card_transactions in data]
    
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
        response = self.send_request("GET", f"virtualcards/cards/transactions/?{url_params}")
        data = response["data"]["cardTransactions"]
        return [self.__generate_card_trans_object(card_transactions) for card_transactions in data]

    def get_card(self, card_id):
        """
        Getting Card using card_id
        card_id = d1cbc518-95d6-4bf2-a0f4-e6a33ee09603

        - GET Request
        """
        response = self.send_request("GET", f"virtualcards/card/{card_id}")
        return self.__generate_virtual_card_object(data=response["data"])
    
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
        response = self.send_request("GET", f"virtualcards/carusersds/?{url_params}")
        data = response["data"]["cardUsers"]
        return [self.__generate_card_user_object(card_users) for card_users in data]