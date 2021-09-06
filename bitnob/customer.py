from bitnob.base import Bitnob


class Customer(Bitnob): 
    
    def create_customer(self, body:dict):
        return self.send_request("POST", "/customers", json=body)

    # def list_customers(self, body:dict):
    #     response = self.send_request("POST", "/wallets/ln/pay", json=body)
    #     return response.json()
    
    def get_customer(self, customer_id):
        return self.send_request("GET", f"/customers/{customer_id}")
    
    def get_customer_by_email(self, email):
        body = {"email": email}
        return self.send_request("POST", "/customers/fetch_customer", json=body)

    
    def update_customer(self, body:dict, customer_id):
        return self.send_request("PUT", f"/customers/{customer_id}", json=body)