# Ethereum Smart Contract for Encrypted Token Swap

This repository contains a Solidity smart contract designed for performing encrypted token swaps on the Uniswap V3 decentralized exchange (DEX). 

## Overview

The smart contract features a function that accepts an encrypted input containing a pool address and a token amount in hexadecimal format. The contract decrypts the data to reveal the true pool address and token amount, then proceeds to perform a token swap on Uniswap V3. Encrypting algorithm is basic XOR chipher.

## Requirements

To successfully set up and run the Smart Contract for Encrypted Token Swap, you will need the following environment and tools:

1. **Python**: A recent version of Python (3.9 or later) should be installed on your system. Python is the primary language used for scripting in Brownie and running the deployment scripts. You can download it from [Python's official website](https://www.python.org/downloads/).

2. **Brownie**: Brownie is a Python-based development and testing framework for smart contracts on the Ethereum network. Install Brownie using pip:

    ```
    pip install eth-brownie
    ```

    Alternatively, you can visit [Brownie's GitHub repository](https://github.com/eth-brownie/brownie) for more detailed installation instructions.

3. **Node.js and npm**: Node.js is required for various blockchain development tools, and npm (Node Package Manager) is used to install packages. You can download them from [Node.js's official website](https://nodejs.org/).

4. **Ganache CLI**: Used for local blockchain development. It can be installed via npm:

    ```
    npm install -g ganache-cli
    ```

5. **Solidity Compiler**: The Solidity version should be compatible with the smart contract. Brownie will automatically install the required Solidity compiler version when compiling the contract.

6. **An Ethereum Wallet**: A wallet with a Goerli Testnet account containing test ETH for deploying and testing the contract. You can use wallets like MetaMask.

7. **Infura Account**: Required for deploying the contract to a testnet/mainnet. Sign up at [Infura](https://infura.io/) and create a new project to obtain the `WEB3_INFURA_PROJECT_ID`.

8. **Etherscan Account**: For verifying the contract source code on Etherscan. Create an account on [Etherscan](https://etherscan.io/) and generate an API token.

Once you have these requirements set up, you can follow the instructions in the `Deployment` section to deploy the smart contract.

## Environment Setup

A `.env` file is required for configuration:

```
export WEB3_INFURA_PROJECT_ID=""
export ETHERSCAN_TOKEN=""
export PRIVATE_KEY=""
```

- `WEB3_INFURA_PROJECT_ID`: Essential for running tests.
- `ETHERSCAN_TOKEN`: Optional, for publishing the contract source code on Etherscan.
- `PRIVATE_KEY`: Required for deploying the contract.

## Project Framework

The project is built using the Brownie framework, providing a powerful suite of development tools for Ethereum smart contract development.

### Testing

Tests are included to ensure contract functionality and can be run using Brownie. The `WEB3_INFURA_PROJECT_ID` is necessary for executing these tests.

```
$ source .env
$ brownie test --network mainnet-fork
```

### Deployment

To deploy the smart contract, use the following command:

```
$ source .env
$ brownie run deploy --network goerli
```

Ensure that `.env` file is correctly set up with `PRIVATE_KEY`, `ETHERSCAN_TOKEN` (if you need to publish source code), and `WEB3_INFURA_PROJECT_ID`.

Deployed smart-contract address: [0x764ecB4b71f100F3aB385E1A906709e75A04d5A3](https://goerli.etherscan.io/address/0x764ecB4b71f100F3aB385E1A906709e75A04d5A3)