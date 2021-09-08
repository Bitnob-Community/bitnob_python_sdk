from bitnob.base import Bitnob


class Lightning(Bitnob): 
    
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

        - POST Request
        """
        return self.send_request("POST", "/wallets/ln/createinvoice", json=body)

    def pay_invoice(self, body:dict):
        """
        Paying lightning invoice

        body = {
            "request": "lntb10u1ps3z4vqpp5lhvr5hdhtw2z32f88dfym5hw2pk9a0a2gr5g0x85ccdy3hpwuneqdpsd4hkueteypehgmmswvsxummwwdjkuum9yphkugrnw4hxgctecqzpgxqr23sfppqtthagr80s0jruguvg38g78pgl8nwp32esp5wvx8sus7a4g66ujtw2zzvyj49zd2sfw5msh3jhaes2vm3z6ga84s9qyyssqm73qauemzqw3tz0equ7cfs2l8xfcgqzuusgg6rplp4hprv83cde97fhh5vxglsqfzwzpms24d7xrqc77cjv32tny82nktfhkz699awcqwdhwur",
            "reference": "skjrjfr"
        }

        - POST Request
        """
        return self.send_request("POST", "/wallets/ln/pay", json=body)
    
    def initiate_payment(self, body:dict):
        """
        Creating lightning invoice for customer

        body = {
            "request": "lntb10u1pssrea6pp5rdmqtcxdl69syel7xal4ajmaq6phtd23ujnzdzqwv68p4mprhajqdpsd4hkueteypehgmmswvsxummwwdjkuum9yphkugrnw4hxgctecqzpgxqr23sfppqh4rqy3muaufpmzcfyhpqy8ase4gjsmvtsp5c5nghldmj8k0q8fl4l3eyvga95905g4f8kzwah6pts2kr2l3f03s9qyyssqj5lz3wlas54kfh2dhnk3d5xz5j8d2t4ym963kc29gfh3dketwscsq0y07ypsylk50yj0jx284764vtkwlnpx2czerks7t6mry4h0axcpmazk8l"
        }

        - POST Request
        """
        return self.send_request("POST", "/wallets/ln/initiatepayment", json=body)
    
    def decode_payment_request(self, body:dict):
        """
        Creating lightning invoice for customer

        body = {
            "request": "lntb10u1psny337pp5km35drx473py8ucup33k0qhrql0ll7cg528c9999eyssp8l0l7xsdpsd4hkueteypehgmmswvsxummwwdjkuum9yphkugrnw4hxgctecqzpgxqr23sfppq00dkh7zckw5d7xgzkk0tctcamlzu6fnrsp53d3kuz79s7akxj9hx0ucnd5fzpd5dlsmwxu7dcja0ksqguqkkm7q9qyyssqyr0lgw260u7pqyjfuwp4azszhugt9m353c9vfq36qltxnqe40qm3dxz4vrqxjyp0utyhvr3p3rrvjpuc0jfts3yd0y02ckqhnx9zp8gpzrazdt"
        }

        - POST Request
        """
        return self.send_request("POST", "/wallets/ln/decodepaymentrequest", json=body)
    
    def get_invoice(self, body:dict):
        """
        Getting lightning invoice

        body = {
            "id": "1b7605e0cdfe8b0267fe377f5ecb7d068375b551e4a626880e668e1aec23bf64"
        }

        - POST Request
        """
        return self.send_request("POST", "/wallets/ln/getinvoice", json=body)