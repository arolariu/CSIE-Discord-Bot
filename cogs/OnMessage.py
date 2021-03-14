import json

from discord.ext import commands
from discord.utils import get
from discord_utils import *


class OnMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        # We use a variable to store ctx.content.lower()
        msg = ctx.content.lower()

        # On every message, a user gets 3 credits to spend.
        with open("credits.json", "r") as js:
            data = json.load(js)
        try:
            data[str(ctx.author.id)] += 3
        except KeyError:  # Means the user is a Webhook
            pass
        with open("credits.json", "w") as js:
            json.dump(data, js, indent=2)

        # Faculty selection from the #sectie-csie text channel.
        if ctx.channel.id == 613817796840914994 and msg in role_comms:
            try:
                role_dex = \
                    {
                        "cibe": "CIBERNETICĂ",
                        "info": "INFORMATICĂ ECONOMICĂ",
                        "stat": "STATISTICĂ",
                        "guest": "VIZITATOR"
                    }
                await ctx.author.add_roles(
                    get(ctx.guild.roles, name=role_dex[msg[0:-1] if msg[-1] == "!" else msg[1:]]))
                await ctx.author.remove_roles(get(ctx.guild.roles, name="FĂRĂ ROL"))
                await ctx.add_reaction(emoji="✔")
            except AttributeError:
                await ctx.add_reaction(emoji="❌")
                await ctx.channel.send(
                    "A aparut o eroare la atribuirea rolului. Contacteaza un moderator/admin/developer!")

        # If the user's last word is a quick-poll command, then create a poll:
        try:
            if msg.split()[-1] in reactions.keys():
                try:
                    reactions_count = msg.split()[-1].count("/")
                    for reaction in range(0, reactions_count + 1, 1):
                        await ctx.add_reaction(emoji=reactions[msg.split()[-1]][reaction])
                except AttributeError:
                    await ctx.send("Sigur ai vrut sa faci un poll? Nu recunosc comanda rapida.")
        except IndexError:
            pass  # We pass because it's 99% a false positive and we don't have to do anything.


def setup(bot):
    bot.add_cog(OnMessage(bot))
