from web3 import Web3




def sendTransaction(message):
    w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/2885280182ee49d2a21e7ce953b542a4'))
    address = '0x4dF55DE808d4b67a13ED690c04B2856B16b08442'
    privateKey = '0xac492fc4d8cf34d02ec82725c151d6c9629ce8568d9b8dddb495f8c71734c434'
    nonce = w3.eth.getTransactionCount(address)
    gasPrice = w3.eth.gas_price
    value = w3.toWei(0, 'ether')
    signedTx = w3.eth.account.signTransaction(dict(
        nonce=nonce,
        gasPrice=gasPrice,
        gas=100000,
        to='0xDcf7e51536082D5a1F9ad763974a745B3de4356E',
        value=value,
        data=message.encode('utf-8')

    ), privateKey)

    tx = w3.eth.sendRawTransaction(signedTx.rawTransaction)
    txId = w3.toHex(tx)
    return txId




