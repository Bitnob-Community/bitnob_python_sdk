from bitnob.base import Bitnob, pagination_filter


class Customer(Bitnob): 
    
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
        
        return self.send_request("POST", "/customers", json=body)

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
        return self.send_request("GET", f"/customers/?{url_params}")
    
    def get_customer(self, customer_id):
        """
        Getting User using customer_id

        - GET Request
        """
        return self.send_request("GET", f"/customers/{customer_id}")
    
    def get_customer_by_email(self, email):
        """
        Getting a customer using their email
        email = customer@email.com

        - POST Request
        """
        body = {"email": email}
        return self.send_request("POST", "/customers/fetch_customer", json=body)
    
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
        return self.send_request("PUT", f"/customers/{customer_id}", json=body)