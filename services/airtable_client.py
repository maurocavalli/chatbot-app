from pyairtable import Table

def add_record(api_key, base_id, table_name, data):
    table = Table(api_key, base_id, table_name)
    return table.create(data)
