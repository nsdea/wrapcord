import main
import user
import html

class Message:
    def __init__(self, channel_id: int, message_id: int):
        data = main.get_request(f'channels/{channel_id}/messages/{message_id}')

        self.data = data
        self.content = data['content']
        self.channel_id = channel_id
        self.message_id = message_id
        self.author = user.User(user_id=data['author']['id'])
    
    def __str__(self) -> str:
        return self.content
    
    def react(self, emoji: str):
        escaped = html.escape(emoji)
        return main.put_request(f'channels/{self.channel_id}/messages/{self.message_id}/reactions/{escaped}/@me')

    def delete(self):
        return main.delete_request(f'channels/{self.channel_id}/messages/{self.message_id}')

