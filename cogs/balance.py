import json
import discord

from discord.ext import commands


# Check Credit Balance Command
class Balance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Comanda $balance afiseaza cate credite ai.")
    async def balance(self, ctx, *, user=None):
        if user is not None:
            old_user = self.bot.get_user(int(user[3:-1]))
            user = str(user[3:-1])
        with open("credits.json", "r") as js:
            data = json.load(js)
        if user is None:
            embed = discord.Embed(color=0x00FF00,
                                  title=f"BALANTA: {ctx.author.name}",
                                  description=f"Momentan ai **{data[str(ctx.author.id)]}** credite."
                                  )
        else:
            embed = discord.Embed(color=0x0000FF,
                                  title=f"BALANTA: {old_user}",
                                  description=f"**{data[str(user)]}** credite.")
        return await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Balance(bot))
