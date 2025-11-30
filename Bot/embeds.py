import discord

embeds = {

    "!commands":discord.Embed(
                title="Commands",
                description=(
                    "This is a complete list of all '!' commands availble.\n"
                    "**Rules**\n"
                    "  >  **'!rules'** - Displays a complete list of the servers rules.\n"
                    "  >  **'!rule (1-10)'** - Displays a single rule, for pointing out if someone is breaking a rule in chat."
                    "**Game**\n"
                    "  >  **'!steam'** - Provides the steam link to the game!"
                    "**Misc**\n"
                    "  >  **'!ping'** - A simple test command, used to check if the bot is online."
                ),
                color=0x38ff92
            ),

    "!ping":discord.Embed(
                title="🏓  Pong!",
                description="This is a test message to make sure the bot is online!",
                color=0xff0000
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
            ),

    "!rules":discord.Embed(
                title="Rules",
                description=(
                    "**By joining the server you agree to our rules, breaking them may result in appropriate punishment.** \n"
                    "\n"
                    "* **Rule 1:** No NSFW and r34, no jokes about it is allowed either. Breaking this will result in a permanent ban.\n"
                    "* **Rule 2:** Respect everyone. Breaking this will result in a 1 week timout.\n"
                    "* **Rule 3:** Do not be rude or mean, bullying is not allowed either. Breaking this will result in a 1 day timeout.\n"
                    "* **Rule 4:** English only in all of the servers channels.\n"
                    "* **Rule 5:** No begging for roles, mod, sneak peeks etc.\n"
                    "* **Rule 6:** Don't ping or annoy the owner (Whisker) or moderators. You are allowed to ping mods if someone is breaking rules.\n"
                    "* **Rule 7:** No ai art anywhere in the server. No nsfw/r34 pfps/bio/banners. Don't steal art.\n"
                    "* **Rule 8:** No pedophiles nor going after minors. We are a safe community for everyone, including minors.\n"
                    "* **Rule 9:** Don't find/use loopholes in the rules, moderators always has the final say.\n"
                    "* **Rule 10:** Follow discord TOS."
                    "\n"
                    "Moderators have the right to punish regardless of if you think you broke the rules or not. Moderators always has the final say."
                ),
                color=0xff4938
            ),
    "!rule 1": discord.Embed(
                title="Rule 1",
                description=(
                    "**Rule 1: No NSFW or R34.**\n"
                    "No jokes about it are allowed either.\n"
                    "Breaking this will result in a **permanent ban**."
                ),
                color=0xff4938
            ),

    "!rule 2": discord.Embed(
                title="Rule 2",
                description=(
                    "**Rule 2: Respect everyone.**\n"
                    "Breaking this will result in a **1 week timeout**.\n"
                    "Breaking this rule will result in a punishment decided by the present mod."
                ),
                color=0xff4938
            ),

    "!rule 3": discord.Embed(
                title="Rule 3",
                description=(
                    "**Rule 3: Do not be rude or mean. Bullying is not allowed.**\n"
                    "Breaking this will result in a **1 day timeout**."
                ),
                color=0xff4938
            ),

    "!rule 4": discord.Embed(
                title="Rule 4",
                description=(
                    "**Rule 4: English only in all server channels.**\n"
                    "Breaking this rule will result in a punishment decided by the present mod."
                ),
                color=0xff4938
            ),

    "!rule 5": discord.Embed(
                title="Rule 5",
                description=(
                    "**Rule 5: No begging for roles, mod, sneak peeks, etc.**\n"
                    "Breaking this rule will result in a punishment decided by the present mod."
                ),
                color=0xff4938
            ),

    "!rule 6": discord.Embed(
                title="Rule 6",
                description=(
                    "**Rule 6: Do not ping or annoy the owner (Whisker) or moderators.**\n"
                    "You *are* allowed to ping mods **if someone is breaking rules**.\n"
                    "Breaking this rule will result in a punishment decided by the present mod."
                ),
                color=0xff4938
            ),

    "!rule 7": discord.Embed(
                title="Rule 7",
                description=(
                    "**Rule 7: No AI/Nsfw/Stolen art anywhere in the server.**\n"
                    "No NSFW/R34 pfps, bios, or banners. Do not steal art.\n"
                    "Breaking this rule will result in a punishment decided by the present mod."
                ),
                color=0xff4938
            ),

    "!rule 8": discord.Embed(
                title="Rule 8",
                description=(
                    "**Rule 8: No pedophiles. Do not go after minors.**\n"
                    "This is a safe community for everyone, including minors.\n"
                    "Breaking this rule will result in a punishment decided by the present mod."
                ),
                color=0xff4938
            ),

    "!rule 9": discord.Embed(
                title="Rule 9",
                description=(
                    "**Rule 9: Do not find or use loopholes in the rules.**\n"
                    "Moderators always have the final say.\n"
                    "Breaking this rule will result in a punishment decided by the present mod."
                ),
                color=0xff4938
            ),

    "!rule 10": discord.Embed(
            title="Rule 10",
            description=(
                "**Rule 10: Follow Discord ToS.**\n"
                    "Breaking this rule will result in a punishment decided by the present mod."
            ),
            color=0xff4938
        ),

}