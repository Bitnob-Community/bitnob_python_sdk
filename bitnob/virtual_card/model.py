class VirtualCard:
    def __init__(self, id, balance, cardNumber, 
                    cvv, cardName, cardType, expiry, 
                    status, valid, last4, blocked, frozen) -> None:
        self.id = id
        self.balance = balance
        self.card_number = cardNumber
        self.card_name = cardName
        self.card_type = cardType
        self.expiry = expiry
        self.status = status
        self.valid = valid
        self.cvv = cvv
        self.last4 = last4
        self.blocked = blocked,
        self.frozen = frozen

class VirtualCardTransaction:
    def __init__(self, id, amount, centAmount, type, currency, reference, cardId) -> None:
        self.id = id
        self.amount = amount
        self.cent_amount = centAmount
        self.type = type
        self.currency = currency
        self.reference = reference
        self.cardId = cardId

class VirtualCardUser:
    def __init__(self, id, customerEmail, firstName, lastName, 
                countryCode, phoneNumber, idType, idNumber, 
                city, state, country, zipCode, userPhoto, 
                customerId, line1, line2, kycPassed) -> None:
        self.id = id
        self.customer_email = customerEmail
        self.first_name = firstName
        self.last_name = lastName
        self.country_code = countryCode
        self.phone_number = phoneNumber
        self.id_type = idType
        self.id_number = idNumber
        self.city = city
        self.state = state
        self.country = country
        self.zip_code = zipCode
        self.user_photo = userPhoto
        self.customer_id = customerId
        self.line1 = line1
        self.line2 = line2
        self.kyc_passed = kycPassed
