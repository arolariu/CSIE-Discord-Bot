import json
import os

from discord.ext import commands
from discord_utils import *


class OnEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # When the bot is ready to perform his tasks, this event will trigger:
    @commands.Cog.listener()
    async def on_ready(self):
        embed = discord.Embed(title=f"Am primit restart si sunt gata de actiune!",
                              color=0x00FAFA)
        channel = self.bot.get_channel(744632571471855807)
        await channel.send(embed=embed)

    # If a member gets banned this event will trigger:
    @commands.Cog.listener()
    async def on_member_ban(self, member):
        embed = discord.Embed(title=f"Membrul {member.name} a fost banat.",
                              color=0xFF0000)
        channel = self.bot.get_channel(703014828733628446)
        await channel.send(embed=embed)

    # If a member joins the server this event will trigger:
    @commands.Cog.listener()
    async def on_member_join(self, member):

        # Create DM for the new member:
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
        data[str(member.id)] = 250  # Assign 250 credits to the new member.
        with open("credits.json", "w") as js:
            json.dump(data, js, indent=2)

        # Send an Embed to the welcome channel page.
        channel = self.bot.get_channel(703014828733628446)  # bun-venit channel
        embed = discord.Embed(title=f"Membrul {member.name} a intrat pe server.",
                              color=0xFFFF00)

        await channel.send(embed=embed)

    # If a member leaves the server, this event will trigger:
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        embed = discord.Embed(title=f"Membrul {member.name} a iesit de pe server.",
                              color=0xFFFF00)
        channel = self.bot.get_channel(703014828733628446)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(OnEvents(bot))
