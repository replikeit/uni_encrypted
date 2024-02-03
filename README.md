# Ethereum Smart Contract for Encrypted Token Swap

This repository contains a Solidity smart contract designed for performing encrypted token swaps on the Uniswap V3 decentralized exchange (DEX). 

## Overview

The smart contract features a function that accepts an encrypted input containing a pool address and a token amount in hexadecimal format. The contract decrypts the data to reveal the true pool address and token amount, then proceeds to perform a token swap on Uniswap V3. Encrypting algorithm is basic XOR chipher.

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