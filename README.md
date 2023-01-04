# AI NFT Minter

The purpose of this project is to allow the user to mint an AI generated image using ERC 721 protocols. The application also allows for the user to add new appraisals on specific minted images.

![AI](resources/ai.png)

## Technologies

This application uses the [OpenAI](https://www.openai.com) API service to generate AI images, [Solidity](https://soliditylang.org/) for the minting of the ERC 721 token and appraisal functions, [Remix IDE website](https://remix.ethereum.org/) for smart contract editing, compiling, testing, and deploying, another API service from [Pinata](https://www.pinata.cloud/) for pinning data using IPFS, [Streamlit](https://docs.streamlit.io/) interface for user interaction, and the [Web3](https://web3py.readthedocs.io/en/stable/overview.html) python package to complete our dApp. We will use [Ganache](https://trufflesuite.com/ganache/) as our personal Ethereum blockchain provider and will utilize [MetaMask](https://metamask.io/) as the wallet viewer.

## Installation Guide

Run the following code in your terminal.

```
pip install web3==5.17
pip install streamlit
```

As always, make sure python is updated to its most current version.

```
brew update
brew upgrade
conda update conda
```

## Usage

```
streamlit run app.py
```

## Contributors

[Connor Boots](https://github.com/bootsish) <br> [Cale McDowell](https://github.com/gcm107)

## License

N/A
