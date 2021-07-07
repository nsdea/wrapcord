import os
import html
import json
import dotenv
import requests
import threading
import websocket

dotenv.load_dotenv()

def build_url(path):
    return f'https://discord.com/api/v9/{path}'

def headers():
    return {'authorization': 'Bot ' + os.getenv('TOKEN')}

def get_request(path):
    '''Retuns a <dict> of a API call, whereas path is the URL path after the base URL'''
    response = requests.get(build_url(path), headers=headers()).text
    
    return json.loads(response)

def post_request(path, data: dict):
    '''Send a get request with a path & data, returns its response'''
    response = requests.post(build_url(path), headers=headers(), data=data).text

    return json.loads(response)

def put_request(path):
    '''Send a put request with a path, returns its response code'''
    response = requests.put(build_url(path), headers=headers())

    return response.ok

def delete_request(path):
    '''Send a delete request with a path, returns its response code'''
    response = requests.delete(build_url(path), headers=headers())

    return response.ok
