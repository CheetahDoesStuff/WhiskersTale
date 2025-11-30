import dotenv
from os import getenv
import discord

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

    if message.content.startswith("!ping"):
        embedVar = discord.Embed(
            title="Pong!",
            description="This is a test message to make sure the bot is online!",
            color=0x00ff00
        )
        await message.channel.send(embed=embedVar)

    elif message.content.startswith("!steam"):
        embedVar = discord.Embed(
            title="Steam",
            description=(
                "Check out our steam page "
                "[here](https://store.steampowered.com/app/4178100/Whiskers_Tale/)!\n"
                "Remember that wishlisting the game helps so much and is an amazing way "
                "of supporting further development!"
            ),
            color=0x346eeb
        )
        await message.channel.send(embed=embedVar)

client.run(TOKEN)
