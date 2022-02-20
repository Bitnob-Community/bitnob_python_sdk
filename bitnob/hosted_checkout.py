from bitnob.base import Bitnob, pagination_filter


class HostedCheckout(Bitnob): 
    
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
        
        return self.send_request("POST", "/checkout", json=body)

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
        return self.send_request("GET", f"/checkout/?{url_params}")
    
    def get_checkout_status(self, checkout_id):
        """
        Get Checkout Status

        - GET Request
        """
        return self.send_request("GET", f"/checkout/status/{checkout_id}")

    def get_checkout_info(self, checkout_id):
        """
        Get Checkout Status

        - GET Request
        """
        return self.send_request("GET", f"/checkout/info/{checkout_id}")
    