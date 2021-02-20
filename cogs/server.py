from discord.ext import commands
from discord_utils import *


# To use: $server in a channel.
class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Comanda $server ofera statistici interesante despre server.")
    async def server(self, ctx):
        guild = await self.bot.fetch_guild(606206204699738135)
        members = await guild.fetch_members(limit=None).flatten()
        year_results = server_years(members)
        role_results = server_roles(members)
        year_values = \
            f"""
    **AN I  :** {year_results["AN I"]} membri. ({round(year_results["AN I"] * 100 / len(members), 2)}% din total.)
    **AN II :** {year_results["AN II"]} membri. ({round(year_results["AN II"] * 100 / len(members), 2)}% din total.)
    **AN III:** {year_results["AN III"]} membri. ({round(year_results["AN III"] * 100 / len(members), 2)}% din total.)
    **Alumni:** {year_results["AN IV+"]} membri. ({round(year_results["AN IV+"] * 100 / len(members), 2)}% din total.)
            """

        role_values = \
            f"""
    **CIBERNETICĂ:** {role_results["CIBERNETICĂ"]} membri. ({round(role_results["CIBERNETICĂ"] * 100 / len(members), 2)}% din total.)
    **INFORMATICĂ:** {role_results["INFORMATICĂ ECONOMICĂ"]} membri. ({round(role_results["INFORMATICĂ ECONOMICĂ"] * 100 / len(members), 2)}% din total.)
    **STATISTICĂ :** {role_results["STATISTICĂ"]} membri. ({round(role_results["STATISTICĂ"] * 100 / len(members), 2)}% din total.)
    **VIZITATORI :** {role_results["VIZITATOR"]} membri. ({round(role_results["VIZITATOR"] * 100 / len(members), 2)}% din total.) 
            """

        result = discord.Embed(color=0xff0000)
        result.set_author(name="Statistica Server CSIE++")
        result.add_field(name="După vechime:", value=year_values, inline=False)
        result.add_field(name="După secție :", value=role_values, inline=False)
        result.add_field(name=f"TOTAL MEMBRI: {len(members)}", value="Vă mulțumim tuturor!!!", inline=False)
        return await ctx.send(embed=result)


def setup(bot):
    bot.add_cog(Server(bot))
