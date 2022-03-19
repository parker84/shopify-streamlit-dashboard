import os
import requests
from urllib.parse import urlparse
from urllib.parse import parse_qs
import streamlit as st

# interact with FastAPI endpoint
AUTH_ENDPOINT = "https://shopify-streamlit.herokuapp.com/dash_auth"

url = os.environ["REQUEST_URI"] 
parsed = urlparse(url) 
query_params = parse_qs(parsed.query)

def authenticate(shop:str, state:str):
    r = requests.get(
        AUTH_ENDPOINT, params={"shop": shop, "state": state}, timeout=5001
    )
    return r

st.title(":fire: ShopLit :fire:")
if authenticate(query_params['shop'], query_params['state']) == 200:
    st.write("Success")
else:
    st.write('Please Access This App Through Your Shopify Admin')
