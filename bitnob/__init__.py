from .lightning import Lightning
from .base import Bitnob
from .customer import Customer
from .onchain import Onchain
from .wallet import Wallet

customer = Customer()
lightning = Lightning()
onchain = Onchain()
wallet = Wallet()
