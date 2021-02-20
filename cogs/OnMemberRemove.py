import discord
from discord.ext import commands


# To use: whois {member_tag}
class OnMemberRemove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        embed = discord.Embed(title="!!!LEAVE!!!",
                              color=0xFFFF00,
                              description=f"Membrul {member.name} a iesit de pe server.")
        channel = self.bot.get_channel(703014828733628446)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(OnMemberRemove(bot))
