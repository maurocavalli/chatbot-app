from boxsdk import JWTAuth, Client

def list_folder_items(folder_id):
    auth = JWTAuth.from_settings_file('box_config.json')
    client = Client(auth)
    items = client.folder(folder_id).get_items()
    return items
