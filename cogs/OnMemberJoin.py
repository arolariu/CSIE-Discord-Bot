import os

from discord.ext import commands
from discord_utils import *


# To use: automatically when a new member joins the server.
class OnMemberJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        try:
            await member.create_dm()
            await member.dm_channel.send(f"Bună {member.name}...")
            embed = discord.Embed(color=0x00ff00)
            embed.set_author(name="Bun venit pe Serverul de discord CSIE++ !!")
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name="Pentru inceput:", value=f"{os.getenv('DM_MESSAGE1')}", inline=False)
            embed.add_field(name="In concluzie:", value=f"{os.getenv('DM_MESSAGE2')}", inline=False)
            embed.set_image(url=LOGO_GIF)
            await member.dm_channel.send(embed=embed)
        except Exception as e:
            channel = self.bot.get_channel(773242027101913098)  # discutie-1 channel
            await channel.send(f"Nu am putut sa iti scriu un mesaj in privat, {member.name}, e totul in regula?")
        channel = self.bot.get_channel(703014828733628446)  # bun-venit channel
        await channel.send(f"Bun venit pe canalul de discord, {member.name}!")


def setup(bot):
    bot.add_cog(OnMemberJoin(bot))
