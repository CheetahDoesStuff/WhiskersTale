import dotenv
from os import getenv
import discord
from Bot.embeds import embeds

dotenv.load_dotenv()
TOKEN = getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if 

client.run(TOKEN)
