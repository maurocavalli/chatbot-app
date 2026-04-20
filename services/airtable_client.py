import requests
import streamlit as st

def add_record(table, data):
    cfg = st.secrets["airtable"]
    url = f"https://api.airtable.com/v0/{cfg['BASE_ID']}/{table}"
    headers = {
        "Authorization": f"Bearer {cfg['API_KEY']}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json={"fields": data}, headers=headers)
    return response.json()
