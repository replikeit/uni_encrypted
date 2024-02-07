
from web3 import Web3
import os
from scripts.encoder import generate_random_input

rpc_url = f"https://goerli.infura.io/v3/{os.environ['WEB3_INFURA_PROJECT_ID']}"
w3 = Web3(Web3.HTTPProvider(rpc_url))
abi_uni = """
[
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "weth_",
          "type": "address"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "inputs": [
        {
          "internalType": "bytes",
          "name": "inputData",
          "type": "bytes"
        }
      ],
      "name": "encodedSwap",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "int256",
          "name": "amount0Delta",
          "type": "int256"
        },
        {
          "internalType": "int256",
          "name": "amount1Delta",
          "type": "int256"
        },
        {
          "internalType": "bytes",
          "name": "data",
          "type": "bytes"
        }
      ],
      "name": "uniswapV3SwapCallback",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ]
"""

abi_weth = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"src","type":"address"},{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"deposit","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"guy","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Withdrawal","type":"event"}]'


def send_tx(function_call: any, nonce, value: int = 0) -> str:
    tx = function_call.buildTransaction({
        'gas': 2000000,
        'value': value,
        'nonce': nonce + 1,
    })
    signed_txn = w3.eth.account.signTransaction(tx, os.environ["PRIVATE_KEY"])
    return w3.eth.sendRawTransaction(signed_txn.rawTransaction)



def main():
    uni_encrypt_contract = w3.eth.contract(address='0xAbfb6f23D77D9D8177b5fC58f971cF7E68914486',
                                            abi=abi_uni)
    weth = w3.eth.contract(address="0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6", 
                            abi=abi_weth)
    nonce = w3.eth.getTransactionCount('0x27A4D4F37ca0B0B4d60fd49971DA87C5a301B1B8')
    send_tx(weth.functions.deposit(), nonce, 10000000000000000)
    send_tx(weth.functions.approve('0xAbfb6f23D77D9D8177b5fC58f971cF7E68914486', 10000000000000000), nonce + 1)
    data = generate_random_input('0x0d239A060e6970b50479B990814E8f9dfD22306E', 0.01)
    print(data)
    tx3 = send_tx(uni_encrypt_contract.functions.encodedSwap(data), nonce + 2)


if __name__ == '__main__':
    main()