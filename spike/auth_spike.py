import json
import requests
import msal
import pyodata

def get_config():
    with open('../test_config.json') as f:
        config = json.load(f)

    return config

def get_token():
    config = get_config()
    context = msal.ConfidentialClientApplication(config['client_id'], client_credential=config['client_secret'], validate_authority=True)
    token = context.acquire_token_by_refresh_token(config['refresh_token'], ['https://admin.services.crm.dynamics.com/user_impersonation'])
    return token

#token = get_token()
config = get_config()

headers = {'Authorization': 'Bearer ' + config['access_token'],
           'OData-MaxVersion': '4.0',
           'OData-Version': '4.0',
           'Accept': 'application/json'}

req2 = requests.get('{}/accounts?$select=name'.format(config['api_url']), headers=headers)
