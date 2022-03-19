import requests
import streamlit as st

AUTH_ENDPOINT = "https://shopify-streamlit.herokuapp.com/dash_auth"
query_params = st.experimental_get_query_params()

def authenticate(shop:str, state:str):
    r = requests.get(
        AUTH_ENDPOINT, params={"shop": shop[0], "state": state[0]}, timeout=5001
    )
    return r

st.title(":fire: ShopLit :fire:")
auth_code = authenticate(query_params['shop'], query_params['state'])
print(auth_code)
if auth_code == 200:
    st.write("Success")
else:
    st.write('Please Access This App Through Your Shopify Admin')
