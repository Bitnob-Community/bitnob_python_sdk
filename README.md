# Bitnob
---
This is a Python package for easy integration of Bitnob For Business API for various applications from Bitnob.

## Getting started

### Requirements
This package requires Python 3.6+

### Installation 
- `pip install bitnob`

### Usage
This SDK can be used both for Bitnob Sandbox and Production API. 
### Setting ENV KEYS
For sucessfully running of the SDK; the `BITNOB_API_KEY` must be set.

Now this will throw a `BitnobBadKeyError` error, if you do not set it as an environment variable, when initiatizing a function.

By default the SDK assumes that you are currently working on production, and your `BITNOB_API_KEY` must be a production-grade secret key. 

To run on sandbox(development mode), set `BITNOB_PRODUCTION=false` as an environment variable.

### Instantiate The Bitnob Functions
Before making use of any bitnob functions, it should be instantiated. Below is a demonstration:

> from bitnob import Lightning

> lightning = Lightning()

- `customer = Customer()`
- `onchain = Onchain()`
- `wallet = Wallets()`


#### Customers

- To manage customers in your application, instantiate a new `Customer` class.
    - The following functions are available:
        - create_customer
        - get_customer_by_email 
        - get_customer 
        - update_customer

### Lightning
- To create Lightning Transactions, instantiate a new `Lightning` class.
    - The following functions are available:
        - create_invoice
        - pay_invoice 
        - initiate_payment
        - decode_payment_request 
        - get_invoice


#### Full Lightning Workflow 
```python
    from bitnob import Lightning

    lightning = Lightning()

    payload = {
        "customerEmail": "bernard@bitnob.com",
        "description": "Enjoy Life!",
        "tokens": 300,
        "expires_at": "24h",
        "private": false,
        "is_including_private_channels": false,
        "is_fallback_included": true,
    }

    # Create a lightning invoice 

   new_ln_invoice = lightning.create_invoice(payload)
    
```
### Onchain 
- To create Onchain Transactions, instantiate a new `Onchain` class.
    - The following functions are available:
        - send_bitcoin
        - generate_address
        - list_addresses


#### Full Onchain Transaction Workflow

```python

    from bitnob import Onchain

    on_chain = Onchain()

    payload = {
        "customerEmail": "bernard@bitnob.com",
        "reference": "txt-ref-09fdcsf-7658dcgfh-84738pokli",
        "satoshis": 30000,
        "address": "btcjshlidlsidskdslisidsdosilsdmxksjsjldksossjoioidjifkji.zjijsi",
        "description": "Go buy your momma a house!",
        "priorityLevel": "priority"
    }

    # Send bitcoin using onchain 

    new_onchain = on_chain.send_bitcoin(payload)

```

### Wallets 
- To get wallets information, simply follow the instruction at the beginning of this sub-heading and instantiate a new `Wallets` class.
    - The following functions are available:
        - wallet_detail
        - get_transaction
        - list_transactions

### Webhook Authentication
- The Bitnob SDK comes with a function that enables your business authenticate events sent to your webhook. It is advised to authenticate all requests sent to your endpoint to avoid fake transactions. 

#### Usage
```python
    from fastapi import FastAPI
    from bitnob import webhook_authenication

    app = FastAPI()

    @app.post("/webhook_endpoint/")
    async def webhook_event_handler(event):
        if webhook_authenication(event):
            #Handle event
            #return 200
        else:
            #do nothing or throw error
```

## Development 


## Contributing 

Bug reports and pull requests are welcome on GitHub at [https://github.com/bitnob/bitnob_python_sdk](https://github.com/bitnob/bitnob_python_sdk). This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the code of conduct. Simply create a new branch and raise a Pull Request, we would review and merge. 

## License

The package is available as open source under the terms of the [BSD License](https://opensource.org/licenses/BSD-3-Clause)