# Imports
import os
import json
import openai
from pathlib import Path
from web3 import Web3
import sys
import pandas as pd
import numpy as np 
import requests
from io import BytesIO
from glob import glob
from PIL import Image, ImageEnhance 
import streamlit as st
from dotenv import load_dotenv
from pinata import pinFiletoIPFS, pinJSONtoIPFS, convertDatatoJSON
load_dotenv()

load_dotenv()

w3 = Web3(Web3.HTTPProvider(os.getenv("WEB_PROVIDER_URI")))


################################################################################
# loading the contract
################################################################################
@st.cache(allow_output_mutation=True)
def load_contract():
    
    with open(Path("abi.json")) as abi:
        artwork_abi = json.load(abi)
        
    artwork_address = os.getenv("SMART_CONTRACT_DEPLOYED_ADDRESS")
    
    contract = w3.eth.contract(
        address=artwork_address,
        abi = artwork_abi
    )
    
    return contract

contract = load_contract()



################################################################################
# pin artwork
################################################################################

def pinArtWork(name, file):
  IPFSfilehash = pinFiletoIPFS(file.getvalue())
  
  tokenJSON = {
      "name":name,
      "image":IPFSfilehash
  }
  
  JSONdata = convertDatatoJSON(tokenJSON)
  JSONIPFShash = pinJSONtoIPFS(JSONdata)    
  return JSONIPFShash, tokenJSON

def pinAppraisal(content):
  JSONdata = convertDatatoJSON(content)
  JSONIPFShash = pinJSONtoIPFS(JSONdata)
  return JSONIPFShash

# sets the api key
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORG")

# Dall-E API endpoint 
# ## DALLE is openai just FYI
DALLE_ENDPOINT = "https://api.openai.com/v1/images/generations"



# Make a request to the Dall-E API
def generate_image(prompt):
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai.api_key}"
  }

  data = """
  {
    """
  data += f'"model": "image-alpha-001",'
  data += f'"prompt": "{prompt}",'
  data += """
    "num_images":10,
    "size":"1024x1024",
    "response_format":"url"
  }
  """
## DALLE is openai just FYI
  resp = requests.post(DALLE_ENDPOINT, headers=headers, data=data)

  if resp.status_code != 200:
    raise ValueError("Failed to generate image "+resp.text)

  return resp.json()['data'][0]['url']

# Create the main app

################################################################################
# frontend
################################################################################









def main():
  
  st.image('resources/ai.png', width=200)

  st.title("Digital Asset Generator")
  
  # accounts = w3.eth.accounts
  # address = st.selectbox("Select an Account", options=accounts)
  prompt = st.text_input("🖼 Tell me what to make for you. Click enter to show the image")
  if st.button("Generate Image "):
    image_url = generate_image(prompt)
    st.image(image_url, width=400)
  st.markdown("## Register a New Artwork")
  file = st.file_uploader("Upload Your Art", type = ["jpg", "jpeg","png"])
  name = st.text_input("Enter a name for the artwork")
  artist = st.text_input("Enter an artist name for the artwork")
  
  
    
  if st.button("Register Artwork"):
    JSONIPFShash, tokenJSON = pinArtWork(name, file)
    tokenURI = f"ipfs://{JSONIPFShash}"
      
    IPFSfilehash = tokenJSON["image"]
      
    tx_hash = contract.functions.registerArtWork(address, name, artist, int(appraisalValue), tokenURI, IPFSfilehash).transact({"from":address})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Receipt is ready. Here it is:")
    st.write(dict(receipt))
      
    st.write("Please view the following links for IPFS Gateway")
    st.markdown(f"[IPFS Gateway Link](https://ipfs.io/ipfs/{JSONIPFShash})")    
    st.markdown(f"[IPFS Image Link](https://ipfs.io/ipfs/{IPFSfilehash})")
    
    

if __name__ == "__main__":
  main()

