from discord.ext import commands
from discord.utils import get
from discord_utils import *


# To use: $update in a channel.
class Update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Comanda $update actualizeaza rolul de an al membrilor de pe server.")
    async def update(self, ctx):
        start = datetime.datetime.now()
        guild = await self.bot.fetch_guild(606206204699738135)
        members = await guild.fetch_members(limit=None).flatten()
        _val1 = get(ctx.guild.roles, name="AN I")
        _val2 = get(ctx.guild.roles, name="AN II")
        _val3 = get(ctx.guild.roles, name="AN III")
        _val4 = get(ctx.guild.roles, name="AN IV+")
        role_dex = \
            {
                "AN I": _val1,
                "AN II": _val2,
                "AN III": _val3,
                "AN IV+": _val4
            }
        for member in members:
            temp = server_years(member)
            good_role = None
            for key, value in temp.items():
                if value == 1:  # False Positive Reference Warning
                    good_role = role_dex[key]
            member_roles = [role for role in member.roles if role.name in ["AN I", "AN II", "AN III", "AN IV+"]]
            if len(member_roles) == 0:
                try:
                    await member.add_roles(good_role, reason="Adaugare rol.")
                except Exception as e:
                    await ctx.send(f"Am intampinat urmatoarea eroare: {e}")
            else:
                for role in member_roles:
                    if role.name != good_role.name:
                        await member.remove_roles(role, reason="Rol asignat incorect.")
                        await member.add_roles(good_role, reason="Corectare rol.")
        end = datetime.datetime.now()
        elapsed = end - start
        embed = discord.Embed(color=0x00ff00)
        embed.set_footer(text=f"Procedura de update a membrilor a durat {round(elapsed.seconds, 2)} de secunde.")
        await ctx.send(embed=embed, delete_after=180)


def setup(bot):
    bot.add_cog(Update(bot))
