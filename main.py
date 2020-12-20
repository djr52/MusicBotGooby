import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv('botToken.env')

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!henlo'):
        await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))
