# {
#   "status": true,
#   "message": "lightning invoice successfully created",
#   "data": {
#     "description": "jsjsjs",
#     "request": "lntb10u1p3p9t5ypp53lxdgsqtem24ytrded2aq5x90yvm8fn3nl9h6dxr0u6lqrfeys3qdq2dfek5um2wvcqzpgxqr23sfppqppth2s03ya2ks4979rwg39ddc0env8tesp5sl60vw2k82l32xune9u6dlhge9gqtstk7ujzfqge3vdpk59w6gfs9qyyssqaalvv6z2qx88e7hakh9t33pryeyr7jcsvn8crsfv0j7y5gvzts3qflf7htn744ywdzuneqmkp0zyv8mjcrfnfkslha0cjxejleltrhgqjzlpvy",
#     "tokens": "1000"
#   }
# }
class Invoice:
    def __init__(self, description, request, tokens) -> None:
        self.description = description
        self.request = request
        self.tokens = tokens

# "data": {
#         "reference": "skjrjfr",
#         "amount": "0.93",
#         "fees": "0",
#         "btcFees": "0",
#         "btcAmount": "0.0000193",
#         "satFees": "0",
#         "satAmount": "1930",
#         "spotPrice": "47979.76",
#         "action": "send_bitcoin",
#         "type": "debit",
#         "status": "pending",
#         "channel": "lightning",
#         "paymentRequest": "lntb19300n1ps5xxgepp5r6w7hpqzfe5f5eg9ep98u0243qtnqn9e7xmwvjynzf25kyyghr9sdpsd4hkueteypehgmmswvsxummwwdjkuum9yphkugrnw4hxgctecqzpgxqr23sfppq97tmvgjq9r4s24047zukwvqrmz5g720wsp5hjxvud80p7yc8p58vdgj8d30c7t8nv5d9rnd59vftccxqvvwk3ns9qyyssq87pa3vxsntqturd5r6n9g57gv964r80q0wcnjcakzsuuqk3xkpgpxul304v7n82xhju8xcjkgckywwhfqzshj5w9q7apat08nm2nh8cpczpu6n",
#         "description": null,
#         "address": null,
#         "hash": null,
#         "confirmations": null,
#         "invoiceId": null,
#         "id": "5c3683d3-5e73-4d15-a910-74c8cba6c8ef",
#         "createdAt": "2021-09-16T10:15:26.711Z",
#         "updatedAt": "2021-09-16T10:15:26.711Z"
#     }
