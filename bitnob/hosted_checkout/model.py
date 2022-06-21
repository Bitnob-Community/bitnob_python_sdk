class User:
    def __init__(self, id, email, firstName, lastName, countryCode, phone) -> None:
        self.id = id
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.countryCode = countryCode
        self.phone = phone
class Checkout:
    def __generate_user_object(self, data):
        return User(id=data["id"], 
                        email=data["email"], 
                        firstName=data["firstName"], 
                        lastName=data["lastName"], 
                        countryCode=data["countryCode"], 
                        phone=data["phone"]
                )

    def __init__(self, id, reference, amount,  
                sat_amount, sat_amount_paid, expires_at,
                lightning_expires_at, status, callback_url, success_url, checkout_type,
                description, address, lightning, companyName, companyLogo, customer) -> None:
        self.id = id
        self.reference = reference
        self.amount = amount
        self.sat_amount_paid = sat_amount_paid
        self.lightning_expires_at = lightning_expires_at
        self.expires_at = expires_at
        self.sat_amount = sat_amount
        self.callback_url = callback_url
        self.checkout_type = checkout_type
        self.status = status
        self.success_url = success_url
        self.description = description
        self.address = address
        self.lightning = lightning
        self.customer = self.__generate_user_object(data=customer)
        self.companyName = companyName
        self.companyLogo = companyLogo

class CheckoutStatus:
    def __init__(self, id, sat_amount, sat_amount_paid, status) -> None:
        self.id = id
        self.sat_amount_paid = sat_amount_paid
        self.sat_amount = sat_amount
        self.status = status

