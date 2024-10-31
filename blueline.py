import discord
from discord.ext import commands
import os
import webserver

DISCORD_TOKEN = os.environ['discordkey']

class Client(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('---'):
            await message.channel.send(f'```ansi\n[2;34m---------------------------------------------------------------------------------------------------------------[0m\n```')

# 인텐트 설정
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

webserver.keep_alive()
bot.run(DISCORD_TOKEN)
