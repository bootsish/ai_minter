# ai_minter



## Technologies

To run this application, you need the following tools installed in the same directory that you are working in.




[Web3.py](https://web3py.readthedocs.io/en/stable/overview.html): A Python library for connecting to and performing operations on Ethereum-based blockchains.

[ethereum-tester](https://pypi.org/project/ethereum-tester/0.1.0a4/): A Python library that provides access to the tools we’ll use to test Ethereum-based applications.

[mnemonic](https://pypi.org/project/mnemonic/): A Python implementation for generating a 12- or 24-word mnemonic seed phrase based on the BIP-39 standard.

[bip44](https://pypi.org/project/bip44/): A Python implementation for deriving hierarchical deterministic wallets from a seed phrase based on the BIP-44 standard.

[Ganache](https://www.trufflesuite.com/ganache) This program allows you to quickly and easily set up/test a local blockchain. 


[MetaMask](https://metamask.io/download/) - MetaMask is a digital wallet for the Ethereum blockchain

_[Solidity](https://soliditylang.org/)_ - This is a programming language we use to create smart contracts.

_[Remix IDE website](https://remix.ethereum.org/)_ - This is where we build and test smart contracts that we create with Solidity.


Streamlit - Python library for building web interfaces for your Python applications.


## Installation Guide

Make sure all of the above tools are installed in your dev environment.

```
pip install streamlit
pip install web3==5.17
pip install eth-tester==0.5.0b3
pip install mnemonic
pip install bip44
