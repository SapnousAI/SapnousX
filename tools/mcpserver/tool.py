import requests

def call_mcp_server(endpoint, payload, token=None):
    headers = {'Authorization': f'Bearer {token}'} if token else {}
    try:
        resp = requests.post(endpoint, json=payload, headers=headers)
        return resp.json()
    except Exception as e:
        return str(e)
