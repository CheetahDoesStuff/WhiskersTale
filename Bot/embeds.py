import discord

embeds = {
    "!ping":discord.Embed(
                title="Pong!",
                description="This is a test message to make sure the bot is online!",
                color=0x00ff00
            ),
    
    "!steam":discord.Embed(
                title="Steam",
                description=(
                    "Check out our steam page "
                    "[here](https://store.steampowered.com/app/4178100/Whiskers_Tale/)!\n"
                    "Remember that wishlisting the game helps so much and is an amazing way "
                    "of supporting further development!"
                ),
                color=0x346eeb
            )
}