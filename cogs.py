import os
import platform


import discord
from discord.ext import commands
from discord.utils import get
from discord_utils import *


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
                whois.set_footer(text=f'whois rulat de @{ctx.author}\nWHOIS tool creat de către Olariu Alexandru-Răzvan.')
                await ctx.channel.send(embed=whois)


# To use: avatar {member_tag}
class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author == self.bot.user:
            return
        msg = ctx.content.lower()
        if msg.startswith('avatar') and (ctx.mentions.__len__() > 0):
            for user in ctx.mentions:
                link = user.avatar_url
                await ctx.channel.send(link)


# To use: type "cibe!" / "info!" / "stat!" / "guest!" in a *SPECIFIC* channel.
class RoleAssign(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author == self.bot.user:
            return
        msg = ctx.content.lower()
        if ctx.channel.id == 613817796840914994 and msg in role_comms:
            try:
                role_dex = \
                    {
                        "cibe": "CIBERNETICĂ",
                        "info": "INFORMATICĂ ECONOMICĂ",
                        "stat": "STATISTICĂ",
                        "guest": "VIZITATOR"
                    }
                await ctx.author.add_roles(get(ctx.guild.roles, name=role_dex[msg[0:-1] if msg[-1] == "!" else msg[1:]]))
                await ctx.add_reaction(emoji="✔")
            except AttributeError:
                await ctx.add_reaction(emoji="❌")
                await ctx.channel.send("A aparut o eroare la atribuirea rolului. Contacteaza un moderator/admin/developer!")


# To use: type a *SPECIFIC* phrase at the end of your message in a channel.
class PollReactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author == self.bot.user:
            return
        msg = ctx.content.lower()
        if msg.split()[-1] in reactions.keys():
            try:
                reactions_count = msg.split()[-1].count("/")
                for reaction in range(0, reactions_count + 1, 1):
                    await ctx.add_reaction(emoji=reactions[msg.split()[-1]][reaction])
            except AttributeError:
                await ctx.send("Sigur ai vrut sa faci un poll? Nu recunosc comanda rapida.")


# To use: $server in a channel.
class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def server(self, ctx):
        guild = await self.bot.fetch_guild(606206204699738135)
        members = await guild.fetch_members(limit=None).flatten()
        year_results = server_years(members)
        role_results = server_roles(members)
        year_values = \
            f"""
    **AN I  :** {year_results["AN I"]} membri. ({round(year_results["AN I"] * 100 / len(members), 2)}% din total.)
    **AN II :** {year_results["AN II"]} membri. ({round(year_results["AN II"] * 100 / len(members), 2)}% din total.)
    **AN III:** {year_results["AN III"]} membri. ({round(year_results["AN III"] * 100 / len(members), 2)}% din total.)
    **Alumni:** {year_results["AN IV+"]} membri. ({round(year_results["AN IV+"] * 100 / len(members), 2)}% din total.)
            """

        role_values = \
            f"""
    **CIBERNETICĂ:** {role_results["CIBERNETICĂ"]} membri. ({round(role_results["CIBERNETICĂ"] * 100 / len(members), 2)}% din total.)
    **INFORMATICĂ:** {role_results["INFORMATICĂ ECONOMICĂ"]} membri. ({round(role_results["INFORMATICĂ ECONOMICĂ"] * 100 / len(members), 2)}% din total.)
    **STATISTICĂ :** {role_results["STATISTICĂ"]} membri. ({round(role_results["STATISTICĂ"] * 100 / len(members), 2)}% din total.)
    **VIZITATORI :** {role_results["VIZITATOR"]} membri. ({round(role_results["VIZITATOR"] * 100 / len(members), 2)}% din total.) 
            """

        result = discord.Embed(color=0xff0000)
        result.set_author(name="Statistica Server CSIE++")
        result.add_field(name="După vechime:", value=year_values, inline=False)
        result.add_field(name="După secție :", value=role_values, inline=False)
        result.add_field(name=f"TOTAL MEMBRI: {len(members)}", value="Vă mulțumim tuturor!!!", inline=False)
        await ctx.send(embed=result)


# To use: $update in a channel.
class UpdateMembers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
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


# To use: $ver in a channel.
class BotVersion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ver(self, ctx):
        embed = discord.Embed(color=0x000000)
        embed.set_author(name="About this Bot:")
        about_info_1 = \
            f"""
    **Bot Developer:** <@276709808512696320> (중간끝#6826)
    **UID:** 613154066662555648
    **Latency:** {round(self.bot.latency * 1000, 2)}ms
    **Current Working Directory:** {os.getcwd()}
    **Operating Platform:** {platform.platform(aliased=True)}
    **Compiler being used:** {platform.python_compiler()}
    **Operating System:** {platform.system()}
    **OS version:** {platform.version()}
    **CPU type:** {platform.processor()}
    **CPU cores:** {os.cpu_count()} cores
            """
        about_info_2 = \
            f"""
    중간끝 ( B O T ) este momentan la versiunea **2.1a.**
    
    Acest robot a fost conceput pentru a servi studentii de pe serverul de discord CSIE++.
    Serverul CSIE++ reprezinta comunitatea studentilor din facultatea de Cibernetica, Statistica si Informatica Economica.
    Robotul este complet integrat cu capabilitatile servereului si ofera studentilor o gama variata de resurse.
    
    
    **În această versiune:**
        ```diff
        ++ Am simplificat procesul de asignare automata a anului.
        ++ Am actualizat bibliotecile interne ale botului la ultima versiune.
        ++ Am incorporat biblioteci de encoding si decoding pentru fisiere JSON.
        -- Botul momentan este instabil.
        ```
    """
        embed.add_field(name="Bot Status:", value=about_info_1, inline=False)
        embed.add_field(name="Bot Description:", value=about_info_2, inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/743466478707409037/744920174477443112/wat.gif")
        await ctx.send(embed=embed)


# To use: $clear {amount_of_messages_to_be_deleted} in a channel.
class ClearMessages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clear(self, ctx, amount):
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
                await ctx.channel.purge(limit=int(amount))
            else:
                await ctx.send("Nu aveți drepturile necesare pentru a rula această comandă. Îmi pare rău!")
        except ValueError:
            await ctx.send("Parametrii tăi nu se aseamănă cu cei ceruți. Comanda trebuie să fie de genul $clear {@tu} {nr}")


# To use: react to a *SPECIFIC* message in a *SPECIFIC* channel.
class CustomRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        guild = await self.bot.fetch_guild(606206204699738135)
        channel = self.bot.get_channel(744513142188670977)
        msg = await channel.fetch_message(id=744562841276645457)
        reaction_dex = \
        {
            "1️⃣": 1,
            "2️⃣": 2,
            "3️⃣": 3,
            "4️⃣": 4,
            "5️⃣": 5
        }
        embed = msg.embeds
        embed_desc = embed[0].description
        role_page = [embed_desc.count(f"Pagina {i}/6") for i in range(1, 7)]
        start_page = role_page.index(1)
        await msg.edit(embed=role_pages[start_page])

        if payload.message_id == 744562841276645457:

            # The user has hit the back page reaction:
            if payload.emoji.name == "👈":
                try:
                    if (start_page - 1) > 0:
                        start_page -= 1
                    else:
                        start_page = 5
                    await msg.edit(embed=role_pages[start_page])
                except Exception as e:
                    print(e)
                await msg.remove_reaction(member=payload.member, emoji="👈")

            # The user has hit the next page reaction:
            elif payload.emoji.name == "👉":
                try:
                    if (start_page + 1) > 5:
                        start_page = 0
                    else:
                        start_page += 1
                    await msg.edit(embed=role_pages[start_page])
                except Exception as e:
                    print(e)
                await msg.remove_reaction(member=payload.member, emoji="👉")

            # The user has hit a role reaction.
            else:
                try:
                    role_dex = \
                        {
                            1: ["Ofițer", "Drogat", "Scîrțar", "Weeb", "Chad"],
                            2: ["Bercenar", "Covid-20", "Nașul", "Gay", "Sărac"],
                            3: ["DJ", "Party", "Memer", "LOL-ist", "CSGO-ist"],
                            4: ["C/C++", "C#", "Python", "Java", "JavaScript"],
                            5: ["Data Scientist", "Software Developer", "Graphics Industry", "Web Developer",
                                "Game Industry"],
                            6: ["SiSC Member", "MLSA Member", "VIP Member", None, None]
                        }
                    custom_role = discord.utils.get(guild.roles, name=role_dex[start_page + 1][reaction_dex[payload.emoji.name] - 1])
                    await payload.member.add_roles(custom_role)
                    await msg.remove_reaction(member=payload.member, emoji=payload.emoji.name)
                except Exception as e:
                    print(e)


# To use: automatically when a new member joins the server.
class MemberJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(f"Bună {member.name}...")
        embed = discord.Embed(color=0x00ff00)
        embed.set_author(name="Bun venit pe Serverul de discord CSIE++ !!")
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="Pentru inceput:", value=f"{os.getenv('DM_MESSAGE1')}", inline=False)
        embed.add_field(name="In concluzie:", value=f"{os.getenv('DM_MESSAGE2')}", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/743466478707409037/744920174477443112/wat.gif")
        await member.dm_channel.send(embed=embed)


