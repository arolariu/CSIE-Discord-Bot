import discord
from discord.ext import commands


# To use: whois {member_tag}
class OnMemberBan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_ban(self, member):
        embed = discord.Embed(title="!!!BAN!!!",
                              color=0xFF0000,
                              description=f"Membrul {member.name} a fost banat.")
        channel = self.bot.get_channel(703014828733628446)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(OnMemberBan(bot))
