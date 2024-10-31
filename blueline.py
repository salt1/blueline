import discord
from discord.ext import commands
import os

DISCORD_TOKEN = os.environ['discordkey']
MENTIONED_USER_ID = '714355124146929684'

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_message(message):
    if MENTIONED_USER_ID in [str(user.id) for user in message.mentions]:
        try:
            for i in range(50):
                await message.author.send("GET SPAMMED")
        except discord.Forbidden:
            await message.channel.send(f"{message.author.mention}, I tried to DM you but couldn't. Please enable DMs.")
    await bot.process_commands(message)

bot.run(DISCORD_TOKEN)
