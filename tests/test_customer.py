
from bitnob import Customer

customer_client = Customer()

def test_creating_customer():
    body ={
        "email": "precious@bitnob.com",
        "firstName": "Precious",
        "lastName": "Ndubueze",
        "phone": "9064908234",
        "countryCode": "+234"
    }
    response = customer_client.create_customer(body=body)
    assert response["statusCode"] == 200