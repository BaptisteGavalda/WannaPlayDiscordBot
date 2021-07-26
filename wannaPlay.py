import discord
import json

class MyClient(discord.Client):
    async def on_ready(self):
        with open("games.json", 'r') as file:
            self.games = json.load(file)
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if '/listGames' in message.content:
            await message.channel.send(self.listGames())
    
    def get_game_index(self, game):
        for index in range(0, len(self.games["games"])):
            if self.games["games"][index]["title"] == game:
                return (index)
        return (-1)

    def addGame(self, game, player):
        g_list = self.listGames()
        if game not in g_list:
            self.listGames["games"][self.get_game_index(game)][game] += player

    def listGames(self):
        g_list = ""
        for game in self.games["games"]:
            if g_list != "":
                g_list += ', '
            g_list += '[' + game["title"] + ']'
        return (g_list)

    def searchGame(self):
        pass

with open('token.json', 'r') as token_file:
    tokens = json.load(token_file)

client = MyClient()
client.run(tokens["bot_token"])
