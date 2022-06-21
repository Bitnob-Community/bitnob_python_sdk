from bitnob.base import Bitnob, pagination_filter
from .model import Invoice
from bitnob.wallet.model import Transaction


class Lightning(Bitnob):

    def __generate_invoice_object(self, data):
        return Invoice(
            description = data.get("description"),
            tokens=data.get("tokens"),
            request=data.get("request")
        )
    
    def __generate_transaction_object(self, data):
        return Transaction(            
            reference = data.get("reference"),
            description = data.get("description"),
            amount = data.get("amount"),
            sat_amount = data.get("satAmount"),
            fees = data.get("fees"),
            btc_fees = data.get("btcFees"),
            sat_fees = data.get("satFees"),
            action = data.get("action"),
            transaction_type = data.get("type"),
            status = data.get("status"),
            id=data.get("id"),
            invoice_id=data.get("invoiceId"),
            channel=data.get("channel"),
            address=data.get("address"),
            payment_request=data.get("paymentRequest"),
            spot_price=data.get("spotPrice"),
            hash=data.get("hash"),
            confirmations=data.get("confirmations")
        )
    
    def create_invoice(self, body:dict):
        """
        Creating lightning invoice for customer

        body = {
            "description": "xxxxxxxxx",
            "tokens": 1000,
            "private": false,
            "is_including_private_channels": false,
            "is_fallback_included": true,
            "customerEmail": "customer@gmail.com"
        }

        required_data = "description", "tokens", "customerEmail"

        - POST Request
        """
        required_data = ["description", "tokens", "customerEmail"]
        self.check_required_datas(required_data, body)

        response = self.send_request("POST", "wallets/ln/createinvoice", json=body)
        return self.__generate_invoice_object(data=response["data"])


    def pay_invoice(self, body:dict):
        """
        Paying lightning invoice

        body = {
            "request": "lntb10u1ps3z4vqpp5lhvr5hdhtw2z32f88dfym5hw2pk9a0a2gr5g0x85ccdy3hpwuneqdpsd4hkueteypehgmmswvsxummwwdjkuum9yphkugrnw4hxgctecqzpgxqr23sfppqtthagr80s0jruguvg38g78pgl8nwp32esp5wvx8sus7a4g66ujtw2zzvyj49zd2sfw5msh3jhaes2vm3z6ga84s9qyyssqm73qauemzqw3tz0equ7cfs2l8xfcgqzuusgg6rplp4hprv83cde97fhh5vxglsqfzwzpms24d7xrqc77cjv32tny82nktfhkz699awcqwdhwur",
            "reference": "reference"
        }

        required_data = "request", "reference"

        - POST Request
        """
        required_data = ["request", "reference"]
        self.check_required_datas(required_data, body)

        response = self.send_request("POST", "wallets/ln/pay", json=body)
        return self.__generate_transaction_object(data=response["data"])
    
    def initiate_payment(self, invoice_request):
        """
        Initiate payment on lighting network.

        invoice_request = "lntb10u1psny337pp5km35drx473py8ucup33k0qhrql0ll7cg528c9999eyssp8l0l7xsdpsd4hkueteypehgmmswvsxummwwdjkuum9yphkugrnw4hxgctecqzpgxqr23sfppq00dkh7zckw5d7xgzkk0tctcamlzu6fnrsp53d3kuz79s7akxj9hx0ucnd5fzpd5dlsmwxu7dcja0ksqguqkkm7q9qyyssqyr0lgw260u7pqyjfuwp4azszhugt9m353c9vfq36qltxnqe40qm3dxz4vrqxjyp0utyhvr3p3rrvjpuc0jfts3yd0y02ckqhnx9zp8gpzrazdt"

        - POST Request
        """
        
        body = {"request" : invoice_request}
        return self.send_request("POST", "wallets/ln/initiatepayment", json=body)
    
    def decode_payment_request(self, invoice_request):
        """
        Decode Payment Request

        invoice_request = "lntb10u1psny337pp5km35drx473py8ucup33k0qhrql0ll7cg528c9999eyssp8l0l7xsdpsd4hkueteypehgmmswvsxummwwdjkuum9yphkugrnw4hxgctecqzpgxqr23sfppq00dkh7zckw5d7xgzkk0tctcamlzu6fnrsp53d3kuz79s7akxj9hx0ucnd5fzpd5dlsmwxu7dcja0ksqguqkkm7q9qyyssqyr0lgw260u7pqyjfuwp4azszhugt9m353c9vfq36qltxnqe40qm3dxz4vrqxjyp0utyhvr3p3rrvjpuc0jfts3yd0y02ckqhnx9zp8gpzrazdt"

        - POST Request
        """
        body = {"request" : invoice_request}
        return self.send_request("POST", "wallets/ln/decodepaymentrequest", json=body)
    
    def get_invoice(self, invoice_id):
        """
        Getting lightning invoice
        invoice_id = "1b7605e0cdfe8b0267fe377f5ecb7d068375b551e4a626880e668e1aec23bf64"

        - POST Request
        """
        body = {"id" : invoice_id}
        return self.send_request("POST", "wallets/ln/getinvoice", json=body)
    
    def list_invoices(self, **kwargs):
        """
        Getting addresses attached to company

        - POST Request
        """
        url_params = None
        if kwargs != {}:
            url_params = pagination_filter(**kwargs)
        return self.send_request("GET", f"/wallets/ln/getinvoices/?{url_params}",)