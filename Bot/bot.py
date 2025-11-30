import dotenv
from os import getenv
import discord
from Bot.embeds import embeds

dotenv.load_dotenv()
TOKEN = str(getenv("TOKEN")) # Had to add this so ty shuts up

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

    try:
        embed = next((v for k, v in embeds.items() if message.content.startswith(k)), None)
        await message.channel.send(embed=embed)
    except Exception:
        return


def runBot():
    client.run(TOKEN)
