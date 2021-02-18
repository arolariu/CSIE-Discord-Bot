import discord
from discord.ext import commands


# To use: whois {member_tag}
class Whois(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author == self.bot.user:
            return
        msg = ctx.content.lower()
        if msg.startswith('whois') and (ctx.mentions.__len__() > 0):
            for user in ctx.mentions:
                whois = discord.Embed(colour=0xff0000)
                whois.set_author(name=f" whois performed ~ {user}", icon_url=user.avatar_url)
                whois.set_thumbnail(url=user.avatar_url)
                whois.add_field(name="Nume de utilizator: ", value=user.name, inline=True)
                whois.add_field(name="User ID: ", value=user.id, inline=True)
                whois.add_field(name="Poreclă: ", value=user.nick, inline=False)
                whois.add_field(name="Activitate: ", value=user.activity, inline=True)
                whois.add_field(name="Status: ", value=user.status, inline=True)
                whois.add_field(name="Conectat la voce: ", value="DA" if user.voice is True else "NU", inline=False)
                whois.add_field(name="S-a alăturat pe server în data de: ",
                                value=user.joined_at.strftime("%A, %#d %B %Y, %H:%M"), inline=False)
                whois.add_field(name="S-a alăturat pe discord în data de: ",
                                value=user.created_at.strftime("%A, %#d %B %Y, %H:%M"), inline=False)
                whois.add_field(name="Cel mai mare rol: ", value=user.top_role.mention, inline=False)
                whois.set_footer(
                    text=f'whois rulat de @{ctx.author}\nWHOIS tool creat de către Olariu Alexandru-Răzvan.')
                await ctx.channel.send(embed=whois)


def setup(bot):
    bot.add_cog(Whois(bot))
