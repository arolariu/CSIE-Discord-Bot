from discord.ext import commands
from discord_utils import *


# To use: type a *SPECIFIC* phrase at the end of your message in a channel.
class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author == self.bot.user:
            return
        msg = ctx.content.lower()
        if msg.split()[-1] in reactions.keys():
            try:
                reactions_count = msg.split()[-1].count("/")
                for reaction in range(0, reactions_count + 1, 1):
                    await ctx.add_reaction(emoji=reactions[msg.split()[-1]][reaction])
            except AttributeError:
                await ctx.send("Sigur ai vrut sa faci un poll? Nu recunosc comanda rapida.")


def setup(bot):
    bot.add_cog(Poll(bot))
