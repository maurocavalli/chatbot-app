from boxsdk import JWTAuth, Client
import streamlit as st

def get_box_client():
    cfg = st.secrets["box"]
    auth = JWTAuth(
        client_id=cfg["CLIENT_ID"],
        client_secret=cfg["CLIENT_SECRET"],
        enterprise_id=cfg["ENTERPRISE_ID"],
        jwt_key_id=None,
        rsa_private_key_data=cfg["JWT_PRIVATE_KEY"],
        rsa_private_key_passphrase=cfg["JWT_PASSPHRASE"].encode(),
    )
    return Client(auth)

def list_folder_items(folder_id="0"):
    client = get_box_client()
    return list(client.folder(folder_id).get_items())

def get_file_link(file_id):
    client = get_box_client()
    file = client.file(file_id).get()
    return file.get_shared_link()
