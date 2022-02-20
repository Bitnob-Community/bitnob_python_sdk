from bitnob import USDT, USDC
usdc = USDC()
usdt = USDT()

def test_generate_usdc_address():
    body = {
        "chain": "BSC",
        "customerEmail": "precious@bitnob.com"
        }
    data = usdc.generate_address(body=body)
    assert data.address_type == "BSC"


def test_generate_usdt_address():
    body = {
        "chain": "BSC",
        "customerEmail": "precious@bitnob.com"
        }
    data = usdt.generate_address(body=body)
    assert data.address_type == "BSC"


def test_send_usdc():
    body = {
        "amount": 10,
        "address": "4zMMC9srt5Ri5X14GAgXhaHii3GnPAEERYPJgZJDncDU",
        "chain": "SOL",
        "description": "string"
    }
    data = usdc.send(body=body)
    assert data.amount == "10"
    total = data.amount + data.fees
    assert total == data.total_amount


def test_send_usdt():
    body = {
        "amount": 10,
        "address": "4zMMC9srt5Ri5X14GAgXhaHii3GnPAEERYPJgZJDncDU",
        "chain": "BSC",
        "description": "string"
    }
    data = usdt.send(body=body)
    assert data.amount == "10"
    total = data.amount + data.fees
    assert total == data.total_amount