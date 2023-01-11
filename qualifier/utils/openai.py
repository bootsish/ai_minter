# Imports
import os
import openai
#import sys
#import pandas as pd
#import numpy as np 
import requests
#from io import BytesIO
#from glob import glob
#from PIL import Image, ImageEnhance 
import streamlit as st
from dotenv import load_dotenv
load_dotenv()


# sets the api key
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORG")

def getImage(prompt):
    response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="256x256"
    )
    image_url = response['data'][0]['url']
    return image_url

imageLink = getImage()

img_data = requests.get(imageLink).content

st.image(img_data)
st.write(imageLink)

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
def main():
  st.title("Digital Asset Generator")

  prompt = st.text_input("🖼 Tell me what to make for you. Click enter to show the image")
  if prompt:
    image_url = generate_image(prompt)
    st.image(image_url, width=400)

if __name__ == "__main__":
  main()




