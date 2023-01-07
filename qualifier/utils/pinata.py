import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()

file_headers = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_SECRET_API_KEY")
}

json_headers = {
    "Content-Type": "application/json",
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_SECRET_API_KEY")
}

def convertDatatoJSON(content):
    data = {"pinataOptions":{"cidVersion":1}, "pinataContent": content}
    return json.dumps(data)

def pinFiletoIPFS(file):
    r = requests.post("https://api.pinata.cloud/pinning/pinFileToIPFS", files={"file":file}, headers=file_headers)
    print(r.json())
    return r.json()["IpfsHash"]
    
def pinJSONtoIPFS(json):
    r = requests.post("https://api.pinata.cloud/pinning/pinJSONToIPFS", data=json, headers=json_headers)
    print(r.json())
    return r.json()["IpfsHash"]

    