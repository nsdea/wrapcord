from wrapcord import main
from wrapcord import guild
from wrapcord import message
from wrapcord import exceptions

class Channel:
    def __init__(self, channel_id: int):
        data = main.get_request(f'channels/{channel_id}')

        self.data = data
        try:
            self.name = data['name']
        except KeyError:
            raise exceptions.ChannelNotFound(channel_id)
        self.id = channel_id
        try:
            self.messages = main.get_request(f'channels/{channel_id}/messages')
        except:
            self.messages = None
       
        self.topic = data['topic']
        self.guild_id = data['guild_id']
        # self.guild = guild.Guild(self.guild_id)
        try:
            self.last_message_id = self.messages[0]['id']
        except:
            self.last_message_id = None


    def __str__(self) -> str:
        return self.name
    
    def send(self, content: str):
        return message.Message(channel_id=self.id, message_id=main.post_request(f'channels/{self.id}/messages', data={'content': content})['id'])

    def delete(self):
        main.delete_request(f'channels/{self.id}')
    
    def edit(self, name=None, topic=None):
        data = {}
        if name:
            data['name'] = name
        if topic:
            data['topic'] = topic

        print(data)

        main.patch_request(f'channels/{self.id}', data)
