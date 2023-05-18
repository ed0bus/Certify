from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/2885280182ee49d2a21e7ce953b542a4'))
account = w3.eth.account.create()
privateKey = account.privateKey.hex()
address = account.address

print(f'Your adress: {address}\nYour keyL {privateKey}')
