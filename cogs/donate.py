import json
import discord

from discord.ext import commands


# Donate some credits to another user.
class Donate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Donate some credits to another user.")
    async def donate(self, ctx, user, amount):
        amount = int(amount)
        old_user = user
        user = str(user[3:-1])

        if int(user) == int(ctx.author.id):
            return await ctx.channel.send("Nu poti sa iti dai bani singur.")

        with open("credits.json", "r") as js:
            data = json.load(js)

        if data[str(ctx.author.id)] < amount:
            return await ctx.channel.send("Nu ai destule credite.")

        if user in data.keys():
            data[str(user)] += amount
            data[str(ctx.author.id)] -= amount

        with open("credits.json", "w") as js:
            json.dump(data, js, indent=2)

        embed = discord.Embed(title="DONATIE",
                              color=0xFAFAFA,
                              description=f"{ctx.author.name} a donat {amount} credite catre {old_user}.")
        return await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Donate(bot))
