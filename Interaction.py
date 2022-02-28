from Wallet import Wallet
from BlockchainUtils import BlockchainUtils
import requests


def postTransaction(sender, receiver, amount, type):
    transaction = sender.createTransaction(
        receiver.publicKeyString(), amount, type)
    url = "http://localhost:5000/transaction"
    package = {'transaction': BlockchainUtils.encode(transaction)}
    request = requests.post(url, json=package)


if __name__ == '__main__':

    maddox = Wallet()
    mila = Wallet()
    mila.fromKey('keys/stakerPrivateKey.pem')
    exchange = Wallet()

    #forger: genesis
    postTransaction(exchange, mila, 100, 'EXCHANGE')
    postTransaction(exchange, maddox, 100, 'EXCHANGE')
    postTransaction(exchange, maddox, 10, 'EXCHANGE')

    # forger: probably alice
    postTransaction(mila, mila, 25, 'STAKE')
    postTransaction(mila, maddox, 1, 'TRANSFER')
    postTransaction(mila, maddox, 1, 'TRANSFER')
