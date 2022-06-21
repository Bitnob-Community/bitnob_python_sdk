from bitnob.base import Bitnob, pagination_filter
from .model import Checkout, CheckoutStatus


class HostedCheckout(Bitnob): 

    def __generate_checkout_object(self, data):
        return Checkout(
            id=data["id"],
            reference = data["reference"],
            amount = data["amount"],
            sat_amount_paid = data["sat_amount_paid"],
            lightning_expires_at = data["lightning_expires_at"],
            expires_at = data["expires_at"],
            sat_amount = data["sat_amount"],
            callback_url = data["callback_url"],
            checkout_type = data["type"],
            status = data["status"],
            success_url = data["success_url"],
            description = data["description"],
            address = data["address"],
            lightning = data["lightning"],
            customer=data["customer"],
            companyName=data["companyName"],
            companyLogo=data["companyName"],
        )
    
    def __generate_checkout_status_object(self, data):
        return CheckoutStatus(
                        sat_amount_paid=data["sat_amount_paid"],
                        sat_amount = data["sat_amount"],
                        status = data["status"]
                )
    
    def create_checkout(self, body:dict):
        """
        Create Checkout

        body = {
            amount: 10,
            description: "description"
            customerEmail: "customer@gmail.com",
            notificationEmail: "CustomerfirstName",
            callbackUrl: "htpps://domain.com/callbackUrl",
            successUrl: "htpps://domain.com/successUrl",
            reference: "reference"
        }

        - POST Request
        """
        required_data =  ["amount", "description", "customerEmail", "notificationEmail", "callbackUrl", "successUrl", "reference"]
        self.check_required_datas(required_data, body)
        
        response = self.send_request("POST", "checkout", json=body)
        return self.__generate_checkout_object(data=response.get("data"))

    def list_checkouts(self, **kwargs):
        """
        Listing checkouts

        order = (optional) Result order. Accepted values: `DESC` (default), ASC
        page = (optional) Result page.
        take = (optional) Number of results per request. Accepted values: 0 - 100. Default 10
        
        - GET Request
        """
        url_params = None
        if kwargs != {}:
            url_params = pagination_filter(**kwargs)
        response = self.send_request("GET", f"checkout/?{url_params}")
        data = response.get("data")
        return [self.__generate_checkout_object(user_data) for user_data in data]
    
    def get_checkout_status(self, checkout_id):
        """
        Get Checkout Status

        - GET Request
        """
        response =  self.send_request("GET", f"checkout/status/{checkout_id}")
        return self.__generate_checkout_status_object(data=response.get("data"))


    def get_checkout_info(self, checkout_id):
        """
        Get Checkout Status

        - GET Request
        """
        response =  self.send_request("GET", f"checkout/info/{checkout_id}")
        return self.__generate_checkout_object(data=response.get("data"))
    