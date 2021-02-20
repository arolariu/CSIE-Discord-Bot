import json

from discord.ext import commands

from discord_utils import *


# To use: $update in a channel.
class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Comanda $update actualizeaza rolul de an al membrilor de pe server.")
    async def test(self, ctx):
        start = datetime.datetime.now()
        guild = await self.bot.fetch_guild(606206204699738135)
        members = await guild.fetch_members(limit=None).flatten()

        # JSON Operations for the Credits:
        with open("credits.json", "r") as js:
            data = json.load(js)

        with open("credits.json", "w") as js:
            for member in members:
                data[member.id] = 1000
            json.dump(data, js, indent=2)

        end = datetime.datetime.now()
        elapsed = end - start
        embed = discord.Embed(color=0x00ff00)
        embed.set_footer(text=f"Procedura de update a membrilor a durat {round(elapsed.seconds, 2)} de secunde.")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Test(bot))
