    # "data": {
    #     "balance": 0,
    #     "freezed": false,
    #     "cardNumber": "5368989165638980",
    #     "cardName": "Vinay Ayo",
    #     "cardType": "virtual",
    #     "cvv2": "695",
    #     "expiry": "2022-11-26T00:00:00.000Z",
    #     "status": "active",
    #     "valid": "11/22",
    #     "id": "f3788e65-68bd-4b60-a176-d2fa0138b0f2",
    #     "createdAt": "2021-11-25T14:35:41.280Z",
    #     "updatedAt": "2021-11-25T14:35:41.280Z"
    # }
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


# "cardTransactions": [
#     {
#         "id": "fc443267-c1c0-4948-aea1-144b62994494",
#         "createdAt": "2021-12-05T05:21:49.285Z",
#         "updatedAt": "2021-12-05T05:21:49.285Z",
#         "amount": null,
#         "cardBalanceBefore": 1000,
#         "cardBalanceAfter": 990,
#         "type": "debit",
#         "currency": "usd",
#         "reference": "c5edde689bbc",
#         "cardId": "aeb457d9-1f3a-4018-a8dd-bfd0bda910ad"
#     },

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



# "data": {
#         "id": "aeb457d9-1f3a-4018-a8dd-bfd0bda910ad",
#         "createdAt": "2021-12-05T05:18:14.823Z",
#         "updatedAt": "2021-12-05T05:18:50.122Z",
#         "balance": 990,
#         "freezed": false,
#         "cardNumber": "5368989305337684",
#         "last4": "7684",
#         "cardName": "Vinay Ayo",
#         "cardType": "virtual",
#         "cvv2": "248",
#         "expiry": "2022-12-06T00:00:00.000Z",
#         "status": "active",
#         "valid": "12/22",
#         "cardUser": {
#             "id": "cb4a8105-63a7-48d6-84d6-345c23e61c47",
#             "createdAt": "2021-12-05T05:18:02.763Z",
#             "updatedAt": "2021-12-05T05:18:02.763Z",
#             "customerEmail": "abceseescxsdded@gmail.com",
#             "firstName": "Vinay",
#             "idNumber": "00000000000",
#             "idType": "BVN",
#             "lastName": "Ayo",
#             "phoneNumber": "+23087800004",
#             "userPhoto": null,
#             "line1": "Ikeja",
#             "city": "Lagos",
#             "state": "Lagos",
#             "zipCode": "00234",
#             "country": "Nigeria"
#         }
#     }

class CardReciept:
    pass