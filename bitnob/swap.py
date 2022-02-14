from bitnob.base import Bitnob


class Swap(Bitnob): 
    
    def swap_btc_to_usd(self, amount:int):
        """
        Swap BTC to USD
        amount = 0.00001

        - POST Request
        """
        body = {
            "amount" : amount
        }

        return self.send_request("POST", "/wallets/swap-bitcoin-usd", json=body)
    
    def swap_usd_to_btc(self, amount:int):
        """
        Swap USD to BTC
        amount = 30

        - POST Request
        """
        body = {
            "amount" : amount
        }

        return self.send_request("POST", "/wallets/swap-usd-bitcoin", json=body)