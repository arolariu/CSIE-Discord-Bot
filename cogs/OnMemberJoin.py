import os
import json
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
        except Exception:  # General Exception since discord.py does not provide enough information.
            channel = self.bot.get_channel(773242027101913098)  # discutie-1 channel
            await channel.send(f"Nu am putut sa iti scriu un mesaj in privat, {member.name}, e totul in regula?")

        # JSON Operations for the Credits:
        with open("credits.json", "r") as js:
            data = json.load(js)
        data[member.id] = 250
        with open("credits.json", "w") as js:
            json.dump(data, js, indent=2)

        # Send an Embed to the welcome channel page.
        channel = self.bot.get_channel(703014828733628446)  # bun-venit channel
        embed = discord.Embed(title="!!!JOIN!!!",
                              color=0xFFFF00,
                              description=f"Membrul {member.name} a intrat pe server.")
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(OnMemberJoin(bot))
