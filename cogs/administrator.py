from discord.ext import commands
from discord.utils import get
from discord_utils import *
import json


# Admin Commands Class
class Admin(commands.Cog, name="================================================\nAdministrator"):
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

    # The $load command is used to load a custom plugin in the bot.
    @commands.command(help="Incarca un plugin.")
    async def load(self, ctx, extension):
        if ctx.author.id == 276709808512696320:
            try:
                self.bot.load_extension(f'cogs.{extension}')
            except discord.ext.commands.errors.ExtensionNotFound:
                return await ctx.channel.send(f"Nu am gasit fisierul {extension}")
            except discord.ext.commands.errors.ExtensionAlreadyLoaded:
                return await ctx.channel.send(f"Extensia {extension} a fost incarcata deja.")
            except discord.ext.commands.errors.ExtensionFailed:
                return await ctx.channel.send(f"Extensia {extension} are o eroare.")
        else:
            return await ctx.channel.send("Doar 중간끝#6826 are acces la aceasta comanda.")

    # The $reload command is used to reload a custom plugin for the bot.
    @commands.command(help="Restarteaza un plugin.")
    async def reload(self, ctx, extension):
        if ctx.author.id == 276709808512696320:
            try:
                self.bot.reload_extension(f'cogs.{extension}')
            except discord.ext.commands.errors.ExtensionNotFound:
                return await ctx.channel.send(f"Nu am gasit fisierul {extension}")
            except discord.ext.commands.errors.ExtensionAlreadyLoaded:
                return await ctx.channel.send(f"Extensia {extension} a fost incarcata deja.")
            except discord.ext.commands.errors.ExtensionFailed:
                return await ctx.channel.send(f"Extensia {extension} are o eroare.")
        else:
            return await ctx.channel.send("Doar 중간끝#6826 are acces la aceasta comanda.")

    # The $unload command is used to unload a custom plugin from the bot.
    @commands.command(help="Descarca un plugin.")
    async def unload(self, ctx, extension):
        if ctx.author.id == 276709808512696320:
            try:
                self.bot.unload_extension(f'cogs.{extension}')
            except discord.ext.commands.errors.ExtensionNotFound:
                return await ctx.channel.send(f"Nu am gasit fisieru {extension}")
            except discord.ext.commands.errors.ExtensionAlreadyLoaded:
                return await ctx.channel.send(f"Extensia {extension} a fost incarcata deja.")
            except discord.ext.commands.errors.ExtensionFailed:
                return await ctx.channel.send(f"Extensia {extension} are o eroare.")
        else:
            return await ctx.channel.send("Doar 중간끝#6826 are acces la aceasta comanda.")

    # The $print command is used to test different bot functionalities.
    @commands.command(help="Pentru DEBUG comenzi.")
    async def print(self, ctx, *args):
        if ctx.author.id in power_users:
            result = " ".join([i for i in args])
            return await ctx.channel.send(result)
        else:
            return await ctx.channel.send("Nu aveti permisiunile necesare.")

    # The $warn command is used to warn other users for bad behavior.
    @commands.command(help="Avertizeaza un utilizator daca a gresit.")
    async def warn(self, ctx, user=None, *args):
        if ctx.author.id in power_users:
            old_user = None
            if user is not None:
                try:
                    old_user = self.bot.get_user(int(user[3:-1]))
                    if old_user is None:
                        old_user = self.bot.get_user(int(user[2:-1]))
                except ValueError:
                    return await ctx.channel.send("Sigur ai formulat bine comanda?")

            with open("warnings.json", "r") as warns:
                data = json.load(warns)

            # We get the current date for the new warn:
            date = datetime.datetime.now()
            result = str(date.year) + "-" + str(date.month) + "-" + str(date.day) + \
                " |TZ| " + str(date.hour) + ":" + str(date.minute) + ":" + str(date.second)

            try:
                data[str(old_user)]["Reasons"] += [" ".join(args)]
                data[str(old_user)]["Date(s) warned on:"] += [result]
            except KeyError:
                data[str(old_user)] = {"Reasons": [" ".join(args)]}
                data[str(old_user)].update({"Date(s) warned on:": [result]})

            with open("warnings.json", "w") as warns:
                json.dump(data, warns, indent=2)

            embed = discord.Embed(color=0XFFFF00,
                                  title=":warning: AVERTISMENT :warning:",
                                  description=f"{old_user} a fost avertizat din cauza ca: \n{' '.join(args)}",
                                  timestamp=datetime.datetime.utcnow())
            embed.set_footer(text=f"Nr. total de warnings: {len(data[str(old_user)]['Reasons'])}")
            return await ctx.channel.send(embed=embed)
        else:
            return await ctx.channel.send("Nu ai destule drepturi pentru a accesa aceasta comanda.")


def setup(bot):
    bot.add_cog(Admin(bot))
