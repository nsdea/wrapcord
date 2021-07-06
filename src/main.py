import os
import html
import json
import dotenv
import requests

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
    '''Send a get request with a path & data, returns its response'''
    response = requests.put(build_url(path), headers=headers())

    return response.ok

class User:
    def __init__(self, user_id: int):
        data = get_request(f'users/{user_id}')
     
        self.username = data['username']
        self.name = self.username
        self.discriminator = data['discriminator']
        self.tag = self.discriminator

    def __str__(self) -> str:
        return self.username + '#' + self.tag

class Message:
    def __init__(self, channel_id: int, message_id: int):
        data = get_request(f'channels/{channel_id}/messages/{message_id}')

        self.data = data
        self.content = data['content']
        self.channel_id = channel_id
        self.message_id = message_id
        self.author = User(user_id=data['author']['id'])
    
    def __str__(self) -> str:
        return self.content
    
    def react(self, emoji: str):
        escaped = html.escape(emoji)
        return put_request(f'channels/{self.channel_id}/messages/{self.message_id}/reactions/{escaped}/@me')

class Channel:
    def __init__(self, channel_id: int):
        data = get_request(f'channels/{channel_id}')

        self.data = data
        self.name = data['name']
        self.id = channel_id
        self.messages = get_request(f'channels/{channel_id}/messages')
        self.topic = data['topic']
        self.last_message = Message(channel_id=channel_id, message_id=self.messages[0]['id'])

    def __str__(self) -> str:
        return self.name
    
    def send(self, content: str):
        return Message(channel_id=self.id, message_id=post_request(f'channels/{self.id}/messages', data={'content': content})['id'])

if __name__ == '__main__':
    print(Channel(840878311008763914).send('Ich reagiere mit einem Daumen :)').react('👍'))