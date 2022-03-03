from bitnob import Onchain

onchain = Onchain()

def test_generate_btc_address():
    body = {
        "customerEmail": "precious@bitnob.com"
        }
    data = onchain.generate_address(body=body)
    assert data.address_type == "bech32"