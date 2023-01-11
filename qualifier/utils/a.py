import os
import openai
import streamlit as st
from PIL import Image
import requests

OPENAI = "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"
openai.api_key = OPENAI

prompt = st.text_input("prompt", value= "a white siemese cat")
value = st.text_input("value", value = 10)



@st.cache()
def getImage():
    response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="256x256"
    )
    image_url = response['data'][0]['url']
    return image_url

imageLink = getImage()

img_data = requests.get(imageLink).content

# by clicking on button, generates and save image in bytes form
# same image appears twice because one from imageLink and other from img_data2 txt file
with st.container():
    
    if st.button("click me"):
        st.image(img_data)
        st.write(imageLink)
        
        with open("image.txt","wb") as bfile:
            bfile.write(img_data)
            
        # this read image in bytes form from txt file      
        with open("image.txt","rb") as bfile:
            img_data2 = bfile.read()
            st.image(img_data2)
            
        
    
  

