# AI NFT Minter

The purpose of this project is to allow the user to mint an AI generated image using ERC 721 protocols. The application also allows for the user to add new appraisals on specific minted images. ***This image is AI generated!***

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

First things first, the ArtRegistry contract will need to be deployed to your local Ethereum network (Ganache). This is done by using Ganache and Remix. Make sure the Web provider's URI in your .env matches the Ganache network and deploy via Remix. Once deployed, copy and paste the smart contract address inside your .env. OpenAI and Pinata keys and secrets will need to be placed inside .env, as well.

You are now able to run the command below:

```
streamlit run app.py
```

Inside the app.py, you are able to prompt the generative model for the NFT you would like to mint. Once the image generates you will have to manually save to the desired location. You can then proceed to drag and drop or upload to mint and even transfer the token to a friend.

## Contributors

[Connor Boots](https://github.com/bootsish) <br> [Cale McDowell](https://github.com/gcm107)

## License

N/A
