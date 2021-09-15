# Bitnob
---
This is a Python package for easy integration of Bitnob For Business API for various applications from Bitnob.

[![SDK CI](https://github.com/bitnob/bitnob_python_sdk/actions/workflows/main.yml/badge.svg)](https://github.com/bitnob/bitnob_python_sdk/actions/workflows/main.yml)

## Getting started

### Requirements
This package requires Python 3.6+

### Installation 
- `pip install bitnob`

### Usage
This SDK can be used both for Bitnob Sandbox and Production API. 
### Setting ENV KEYS
For sucessfully running of the SDK; the `BITNOB_API_KEY`.

Now this will throw a `BitnobBadKeyError` if you do not set it as an environment variable.

By default the SDK assumes that you are currently work on production, and your `BITNOB_API_KEY` must be a production-grade secret key. 

To run on sandbox(development mode), set `BITNOB_PRODUCTION=false` as an environment variable.

### Instantiate The Bitnob Functions
Before making use of any bitnob functions, it should be instantiated. Below is a demonstration:

> from bitnob import Lightning

> ln = Lightning()

- `Customer()`
- `Lightning()`
- `Onchain()`
- `Wallets()`


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
        - decode_payment request 
        - get_invoice


#### Full Lightning Workflow 
```python
    from bitnob import Lightning

    ln = Lightning()

    payload = {
        customerEmail: "parah@bitnob.com",
        description: "Dorime for Nonso and Tumise",
        tokens: 300,
        expires_at: "24h",
        mtokens: 200,
        private: {},
        is_including_private_channels: {},
        is_fallback_included: {}
    }

    # Create a lightning invoice 

   new_ln_invoice = ln.create_invoice(payload)
    
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
        customerEmail: "parah@bitnob.com",
        reference: "txt-ref-09fdcsf-7658dcgfh-84738pokli",
        satoshis: 30000,
        address: "btcjshlidlsidskdslisidsdosilsdmxksjsjldksossjoioidjifkji.zjijsi",
        description: "Go buy your momma a house!",
        priorityLevel: "priority"
    }

    # Send bitcoin using onchain 

    new_onchain = on_chain.send_bitcoin(payload)

```

### Wallets 
- To get wallets information, simply follow the instruction at the beginning of this sub-heading and instantiate a new `Wallets` class.
    - The following functions are available:
        - fetch_wallet_detail
        - fetch_all_transactions
        - fetch_transaction

## Development 


## Contributing 

Bug reports and pull requests are welcome on GitHub at [https://github.com/bitnob/bitnob_python_sdk](https://github.com/bitnob/bitnob_python_sdk). This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the code of conduct. Simply create a new branch and raise a Pull Request, we would review and merge. 

## License

The gem is available as open source under the terms of the [BSD License](https://opensource.org/licenses/BSD-3-Clause)