import requests
import streamlit as st

def send_message(to, message):
    cfg = st.secrets["whatsapp"]
    url = f"https://graph.facebook.com/v17.0/{cfg['PHONE_ID']}/messages"
    headers = {
        "Authorization": f"Bearer {cfg['TOKEN']}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": message}
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()
