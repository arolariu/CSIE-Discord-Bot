from discord.ext import commands
from discord.utils import get
from discord_utils import *


# To use: type "cibe!" / "info!" / "stat!" / "guest!" in a *SPECIFIC* channel.
class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author == self.bot.user:
            return
        msg = ctx.content.lower()
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
                await ctx.add_reaction(emoji="✔")
            except AttributeError:
                await ctx.add_reaction(emoji="❌")
                await ctx.channel.send(
                    "A aparut o eroare la atribuirea rolului. Contacteaza un moderator/admin/developer!")


def setup(bot):
    bot.add_cog(Roles(bot))
