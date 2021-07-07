from wrapcord import main
from wrapcord import exceptions

class User:
    def __init__(self, user_id: int):
        data = main.get_request(f'users/{user_id}')

        try:
            self.username = data['username']
        except KeyError:
            raise exceptions.UserNotFound(user_id)
            
        self.name = self.username
        self.discriminator = data['discriminator']
        self.tag = self.discriminator

    def __str__(self) -> str:
        return self.username + '#' + self.tag