from wrapcord import main
from wrapcord import user
from wrapcord import channel
from wrapcord import exceptions

import html

class Message:
    def __init__(self, channel_id: int, message_id: int):
        data = main.get_request(f'channels/{channel_id}/messages/{message_id}')

        self.data = data
        try:
            self.content = data['content']
        except KeyError:
            raise exceptions.MessageNotFound(f'Channel {channel_id} Message {message_id}')

        self.channel_id = channel_id
        self.channel = channel.Channel(channel_id)
        self.message_id = message_id
        self.author_id = data['author']['id']
    
    def __str__(self) -> str:
        return self.content
    
    def react(self, emoji: str):
        escaped = html.escape(emoji)
        main.put_request(f'channels/{self.channel_id}/messages/{self.message_id}/reactions/{escaped}/@me')
        
        return self

    def delete(self):
        return main.delete_request(f'channels/{self.channel_id}/messages/{self.message_id}')

