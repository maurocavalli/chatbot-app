import streamlit as st
from services.box_client import list_folder_items
from services.airtable_client import add_record
from services.whatsapp_client import send_message

st.title("Chatbot – Box + Airtable + WhatsApp")

folder_id = st.text_input("Box Folder ID", "0")

if st.button("List Files"):
    items = list_folder_items(folder_id)
    for item in items:
        st.write(f"{item.name} – {item.id}")
