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
def get_query():
    #hardcoded query
    #will be changed in order to take any input
    q = "whatsup"
    response = ytSearch.youtube_query(q)
    return(response)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('t'):
        quote = get_quote()
        query = get_query()
        await message.channel.send(query)

client.run(os.getenv('TOKEN'))



