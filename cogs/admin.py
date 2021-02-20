from discord.ext import commands
from discord.utils import get
from discord_utils import *


# Admin Commands Class
class Admin(commands.Cog, name="Administrator"):
    def __init__(self, bot):
        self.bot = bot

    # Clear command is used to delete spam messages from a text channel.
    @commands.command(help="Sterge mesajele scrise dintr-un canal.",
                      description="Pentru a putea folosi comanda clear, sintaxa este:")
    async def clear(self, ctx, amount):
        if ctx.author.id in power_users:
            try:
                if ctx.author.id in power_users[1:] and int(amount) > 5:
                    admin = await self.bot.fetch_user(power_users[0])
                    chat_history = []
                    messages = await ctx.channel.history(limit=int(amount)).flatten()
                    for msg in messages:
                        chat_history.append(f"{msg.author} : {msg.content}")
                        chat_history.append("\n")
                    chat_history = [msg for msg in chat_history[::-1]]
                    full_history = "".join(chat_history)
                    abuse = await admin.create_dm()
                    await abuse.send(full_history)
                    if int(amount) <= 15:
                        await ctx.channel.purge(limit=int(amount))
                    else:
                        await ctx.send(f"Maximul de mesaje șterse simultan este 50. (WARNING: @{ctx.author})")
                elif ctx.author.id == power_users[0]:
                    return await ctx.channel.purge(limit=int(amount))
                else:
                    return await ctx.send("Nu aveți drepturile necesare pentru a rula această comandă. Îmi pare rău!")
            except ValueError:
                return await ctx.send(
                    "Parametrii tăi nu se aseamănă cu cei ceruți. Comanda trebuie să fie de genul $clear {@tu} {nr}")
        else:
            return await ctx.send("Nu aveti destule drepturi pentru a executa aceasta comanda.")

    # Update command is used to update the year role of every member in the server.
    @commands.command(help="Actualizeaza rolul de an al membrilor.",
                      description="Pentru a putea folosi comanda update, sintaxa este:")
    async def update(self, ctx):
        if ctx.author.id in power_users:
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
            return await ctx.send(embed=embed, delete_after=180)
        else:
            return await ctx.send("Nu aveti destule drepturi pentru a executa aceasta comanda.")


def setup(bot):
    bot.add_cog(Admin(bot))
