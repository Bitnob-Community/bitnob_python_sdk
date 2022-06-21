class WalletAddress:
    def __init__(self,address, address_type, label=None) -> None:
        self.address = address
        self.address_type = address_type
        self.label = label

class Transaction:
    def __init__(self, id, reference, amount, 
                fees, btc_fees, sat_fees, 
                sat_amount, spot_price, action,
                transaction_type, status, channel, payment_request, 
                description, address, hash,
                confirmations, invoiceId) -> None:
        self.id = id
        self.reference = reference
        self.amount = amount
        self.btc_fees = btc_fees
        self.fees = fees
        self.sat_fees = sat_fees
        self.sat_amount = sat_amount
        self.spot_price = spot_price
        self.transaction_type = transaction_type
        self.status = status
        self.channel = channel
        self.action = action
        self.payment_request = payment_request
        self.description = description
        self.address = address
        self.hash = hash
        self.confirmations = confirmations
        self.invoice_id = invoiceId



