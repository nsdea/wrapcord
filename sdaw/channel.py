import main
import message

class Channel:
    def __init__(self, channel_id: int):
        data = main.get_request(f'channels/{channel_id}')

        self.data = data
        self.name = data['name']
        self.id = channel_id
        self.messages = main.get_request(f'channels/{channel_id}/messages')
        self.topic = data['topic']
        self.last_message = message.Message(channel_id=channel_id, message_id=self.messages[0]['id'])

    def __str__(self) -> str:
        return self.name
    
    def send(self, content: str):
        return message.Message(channel_id=self.id, message_id=main.post_request(f'channels/{self.id}/messages', data={'content': content})['id'])