import os

import discord
from discord.ext import commands

client = discord.Client()

@client.event
async def onReady():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def onMessage(message):
    if message.author == client.user:
        return

    if message.content.startswith('!henlo'):
        await message.channel.send('Hello!')

client.run(os.getenv('token'))
"""
bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('NzkwMDQwMTEwOTcxMzU1MTU3.X960MA.6sbKDv5jtjWLUtsR6_x5nYMkmT8')
"""