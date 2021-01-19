import os
import requests
import json
import discord
from discord.ext import commands
import ytSearch
from dotenv import load_dotenv

load_dotenv('botToken.env')

client = discord.Client()

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    data = json.loads(response.text)
    quote = data[0]['q'] + " -" + data[0]['a']
    return(quote)
def get_query(userQuery):

    response = ytSearch.youtube_query(userQuery)
    return(response)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    activity = discord.Activity(type=discord.ActivityType.listening, name="Tunes to Test to")
    await client.change_presence(activity=activity)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    if message.content.startswith('find '):
        #quote = get_quote()
        query = msg[5:]
        youtubeResponse = get_query(query)
        await message.channel.send(str(youtubeResponse) + " results found")

client.run(os.getenv('TOKEN'))



