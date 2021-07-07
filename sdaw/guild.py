import main

class Guild:
    def __init__(self, guild_id):
        data = main.get_request(f'guilds/{guild_id}')

        self.data = data
        self.name = data['name']
        self.id = guild_id
        self.member_count = data['approximate_member_count']
        self.online_count = data['approximate_presence_count']
        self.boost_tier = data['premium_tier']
