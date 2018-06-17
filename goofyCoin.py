import hashlib
import datetime as date
from Crypto.PublicKey import RSA

class NewUser:


    def __init__(self):
        key = RSA.generate(2048)
        self.privKey = key.export_key()
        self.pubKey = key.publickey().export_key()
        self.wallet = []
        self.coinAmount = len(self.wallet)

class Coin:


    pass

