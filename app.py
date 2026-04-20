import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from services.box_client import list_folder_items
from services.airtable_client import add_record
from services.whatsapp_client import send_message

import streamlit as st
st.title("Chatbot – Box + Airtable + WhatsApp")
...
