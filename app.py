import requests
import streamlit as st
import os
from sqlalchemy import create_engine
import pandas as pd

if os.environ.get('DB_HOST') is not None:
    ENGINE_PATH = f"postgresql://{os.environ.get('DB_USER')}:{os.environ.get('DB_PWD')}@{os.environ.get('DB_HOST')}/{os.environ.get('DB')}"
    engine = create_engine(ENGINE_PATH)
    conn = engine.connect()
else:
    ENGINE_PATH = None

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
    shop, state = query_params['shop'][0], query_params['state'][0]
    response = authenticate(shop, state)
    print(response)
    if response.status_code == 200:
        st.write("Success")
        if ENGINE_PATH is not None:
            st.write("Here's the last 20 orders for your shop:")
            df = pd.read_sql(f'select * from orders_{shop.replace(".", "_")} order by to_timestamp(created_at) desc limit 20', con=conn)
            st.dataframe(df)
    else:
        st.write('Please Access This App Through Your Shopify Admin')
