import discord
from discord.ext import commands


# General Commands Class
class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # The command $avatar {user} shows the user's current avatar.
    @commands.command(help="Un avatar tare? Foloseste $avatar {member_tag} pentru a il vedea mai bine!",
                      description="Comanda $avatar arata avatarul unui utilizator.\nSintaxa:")
    async def avatar(self, ctx, *, user=None):
        if user is not None:
            old_user = self.bot.get_user(int(user[3:-1]))
            link = old_user.avatar_url
            return await ctx.channel.send(link)
        else:
            return await ctx.channel.send("Ai uitat sa specifici un utilizator.")

    # The command $whois {user} provides detailed information about a user.
    @commands.command(description="Comanda $whois ofera detalii despre un anumit utilizator.")
    async def whois(self, ctx, *, user=None):
        if user is not None:
            converter = commands.MemberConverter()
            target_member = await converter.convert(ctx=ctx, argument="".join(user))
            old_user = target_member
            whois = discord.Embed(colour=0xff0000)
            whois.set_author(name=f" whois performed ~ {old_user}", icon_url=old_user.avatar_url)
            whois.set_thumbnail(url=old_user.avatar_url)
            whois.add_field(name="Nume de utilizator: ", value=old_user.name, inline=True)
            whois.add_field(name="User ID: ", value=old_user.id, inline=True)
            whois.add_field(name="Poreclă: ", value=old_user.nick, inline=False)
            whois.add_field(name="Activitate: ", value=old_user.activity, inline=True)
            whois.add_field(name="Status: ", value=old_user.status, inline=True)
            whois.add_field(name="Conectat la voce: ", value="DA" if old_user.voice is True else "NU", inline=False)
            whois.add_field(name="S-a alăturat pe server în data de: ",
                            value=old_user.joined_at.strftime("%A, %d %B %Y, %H:%M"), inline=False)
            whois.add_field(name="S-a alăturat pe discord în data de: ",
                            value=old_user.created_at.strftime("%A, %d %B %Y, %H:%M"), inline=False)
            whois.add_field(name="Cel mai mare rol: ", value=old_user.top_role.mention, inline=False)
            whois.set_footer(
                text=f'whois rulat de @{ctx.author}\nWHOIS tool creat de către Olariu Alexandru-Răzvan.')
            return await ctx.channel.send(embed=whois)
        else:
            return await ctx.channel.send("Ai uitat sa specifici un utilizator.")


def setup(bot):
    bot.add_cog(General(bot))
