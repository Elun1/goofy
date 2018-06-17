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

class Block:

    def __init__(self, index, data, prevHash):
        self.index = index
        self.timestamp = date.datetime.now()
        self.data = data
        self.prevHash = prevHash
        self.hash = computeHash()

    def computeHash(self):
        h = hashlib.sha256()
        h.update(str(self.index).encode('utf-8') +
                 str(self.timestamp).encode('utf-8') +
                 str(self.data).encode('utf-8') +
                 str(self.prevHash).encode('utf-8'))
        return h.hexdigest()

def createGenesis():
    return Block(0, 'Genesis block', "0")

def newBlock():

def createCoin():
    #only Goofy can create a coin.

def transferCoin():


#Goofy always exists
goofy = newUser()

