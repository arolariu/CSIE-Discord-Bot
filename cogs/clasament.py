import discord
import json

from discord.ext import commands


class Clasament(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Vezi cei mai bogati 10 oameni de pe acest server.")
    async def clasament(self, ctx):
        with open("credits.json", "r") as js:
            data = json.load(js)
        top_10 = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
        embed = discord.Embed(color=0xABBACD,
                              title="CLASAMENT CREDITE")
        iterator = 1
        for key, value in top_10.items():
            if iterator == 13:
                return await ctx.channel.send(embed=embed)
            embed.add_field(name=f"Loc #{iterator}: {str(self.bot.get_user(int(key)))[:-5]}",
                            value=f"**{value}** credite",
                            inline=True)
            iterator += 1


def setup(bot):
    bot.add_cog(Clasament(bot))
