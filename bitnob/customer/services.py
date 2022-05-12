
from bitnob.base import Bitnob, pagination_filter
from .model import User

class Customer(Bitnob): 

    def __generate_user_object(self, data):
        return User(id=data["id"], 
                        email=data["email"], 
                        firstName=data["firstName"], 
                        lastName=data["lastName"], 
                        countryCode=data["countryCode"], 
                        phone=data["phone"]
                )
    
    def create_customer(self, body:dict):
        """
        Creating your customer on the Bitnob platform
        body = {
            "email": "customer@gmail.com",
            "firstName": "CustomerfirstName",
            "lastName": "CustomerlastName",
            "phone": "9xxxxxxxx",
            "countryCode": "+234"
        }

        - POST Request
        """
        required_data = ["email", "firstName", "lastName", "phone", "countryCode"]
        self.check_required_datas(required_data, body)
        
        response = self.send_request("POST", "customers", json=body)
        return self.__generate_user_object(data=response.get("data"))



    def list_customers(self, **kwargs):
        """
        Listing all customer

        order = (optional) Result order. Accepted values: `DESC` (default), ASC
        page = (optional) Result page.
        take = (optional) Number of results per request. Accepted values: 0 - 100. Default 10
        
        - GET Request
        """
        url_params = None
        if kwargs != {}:
            url_params = pagination_filter(kwargs=kwargs)
        response = self.send_request("GET", f"customers/?{url_params}")
        data = response["data"]["customers"]
        return [self.__generate_user_object(user_data) for user_data in data]

    
    def get_customer(self, customer_id):
        """
        Getting User using customer_id

        - GET Request
        """
        response =  self.send_request("GET", f"customers/{customer_id}")
        return self.__generate_user_object(data=response.get("data"))
    
    def get_customer_by_email(self, email):
        """
        Getting a customer using their email
        email = customer@email.com

        - POST Request
        """
        body = {"email": email}
        response =  self.send_request("POST", "customers/fetch_customer", json=body)
        return self.__generate_user_object(data=response.get("data"))
    
    def update_customer(self, body:dict, customer_id):
        """
        Updating User using customer_id
        body = {
            "email": "customer@gmail.com",
            "firstName": "CustomerfirstName",
            "lastName": "CustomerlastName",
            "phone": "9xxxxxxxx",
            "countryCode": "+234"
        }

        - PUT Request
        """
        response =  self.send_request("PUT", f"customers/{customer_id}", json=body)
        return self.__generate_user_object(data=response.get("data"))