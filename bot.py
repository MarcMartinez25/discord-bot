import os
import discord
import random
from dotenv import load_dotenv
from responses import responses

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        response = random.choice(responses)
        await message.channel.send(response)

client.run(TOKEN)
