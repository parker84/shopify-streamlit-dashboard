import requests
import streamlit as st

AUTH_ENDPOINT = "https://shopify-streamlit.herokuapp.com/dash_auth"
query_params = st.experimental_get_query_params()

def authenticate(shop:str, state:str):
    response = requests.get(
        AUTH_ENDPOINT, params={"shop": shop, "state": state}, timeout=5001
    )
    return response

st.title(":fire: ShopLit :fire:")
if 'shop' not in query_params:
    st.write('Please Access This App Through Your Shopify Admin')
else:
    response = authenticate(query_params['shop'][0], query_params['state'][0])
    print(response)
    if response.status_code == 200:
        st.write("Success")
    else:
        st.write('Please Access This App Through Your Shopify Admin')
