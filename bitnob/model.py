from bitnob.wallet.model import WalletAddress, Transaction
from bitnob.stablecoin.model import Receipt
from bitnob.customer.model import User
from bitnob.lightning.model import Invoice

#Used in Customer Service
class User:
    def __init__(self, id, email, firstName, lastName, countryCode, phone) -> None:
        self.id = id
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.countryCode = countryCode
        self.phone = phone


# Used in Lightning Invoice
class Invoice:
    def __init__(self, description, request, tokens) -> None:
        self.description = description
        self.request = request
        self.tokens = tokens

# Stablecoins and Bitcoin Onchain Address
class WalletAddress:
    def __init__(self,address, address_type, label=None) -> None:
        self.address = address
        self.address_type = address_type
        self.label = label


#Onchain and Lightning Invoice
class Transaction:
    def __init__(self, id, reference, amount, 
                fees, btc_fees, sat_fees, 
                sat_amount, spot_price, action,
                type, status, channel, payment_request, 
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
        self.type = type
        self.status = status
        self.channel = channel
        self.action = action
        self.payment_request = payment_request
        self.description = description
        self.address = address
        self.hash = hash
        self.confirmations = confirmations
        self.invoice_id = invoiceId


# Virtual Card 
class VirtualCard:
    def __init__(self, id, balance, cardNumber, 
                    cvv, cardName, cardType, expiry, 
                    status, valid) -> None:
        self.id = id
        self.balance = balance
        self.card_number = cardNumber
        self.card_name = cardName
        self.card_type = cardType
        self.expiry = expiry
        self.status = status
        self.valid = valid
        self.cvv = cvv


# Virtual Card Transaction
class cardTransaction:
    def __init__(self, id, amount, cardBalanceBefore, cardBalanceAfter, type, currency, reference, cardId) -> None:
        self.id = id
        self.amount = amount
        self.card_balance_before = cardBalanceBefore
        self.card_balance_after = cardBalanceAfter
        self.type = type
        self.currency = currency
        self.reference = reference
        self.cardId = cardId


#StableCoins Receipt
class Receipt:
    def __init__(self, id, reference, description, amount, fees, action, receipt_type, status) -> None:
        self.reference =reference
        self.description = description
        self.amount = amount
        self.fees = fees
        self.action = action
        self.receipt_type = receipt_type
        self.status = status
        self.id=id
    
    @property
    def cent_amount(self):
        self.amount * 100
    
    @property
    def cent_fees(self):
        self.fees * 100
    
    @property
    def total_amount(self):
        """
        Total amount debited from user
        """
        return self.amount + self.fees
    
    @property
    def total_cents(self):
        """
        Total cents debited from user
        """
        return self.centAmount + self.centFees