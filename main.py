import os
import platform

import datetime
import logging

import discord
from discord.utils import get
from discord.ext import commands

# Flask script to run a server thread.
# from keep_alive import keep_alive

# Helper variables:
role_comms = ["cibe!", "!cibe", "info!", "!info", "stat!", "!stat", "guest!", "!guest"]
power_users = \
    [
        276709808512696320,  # RAZVAN
        261216306894864396,  # BARGAU
        3075860320381829,  # DANIEL
        3422159595719884,  # LOWENT
        3760652865305313,  # BIENCU
        3241515951409070   # OBAMAG
    ]


# Helper Functions:


def server_years(members):
    """
    The function server_years calculates the join date of every member in the guild.
    :param members: *MUST* be a Member Iterator List
    :return: A list which contains 4 elements:
            key AN I: The count of year 1 students.
            key AN II: The count of year 2 students.
            key AN III: The count of year 3 students.
            key AN IV: The count of year 4 students.
    """
    current_year = int(datetime.datetime.now().year)
    y1, y2, y3, y4 = 0, 0, 0, 0

    try:
        for member in members:
            join_date = str(member.joined_at)
            join_year = int(join_date[0:4])
            join_month = int(join_date[5:7])
            if join_year == current_year and join_month >= 6:
                y1 += 1
            elif join_year == current_year - 1 or (join_year == current_year and join_month < 6):
                y2 += 1
            elif join_year == current_year - 2:
                y3 += 1
            else:
                y4 += 1
    except TypeError:
        join_date = str(members.joined_at)
        join_year = int(join_date[0:4])
        join_month = int(join_date[5:7])
        if join_year == current_year and join_month >= 6:
            y1 += 1
        elif join_year == current_year - 1 or (join_year == current_year and join_month < 6):
            y2 += 1
        elif join_year == current_year - 2:
            y3 += 1
        else:
            y4 += 1

    result = {
        "AN I": y1,
        "AN II": y2,
        "AN III": y3,
        "AN IV+": y4
    }
    return result


def server_roles(members):
    """
    The function server_roles calculates the number of members from each of the faculty sections.
    :param members: *MUST* be a Member Iterator List
    :return: A dictionary which contains 4 elements:
            key CIBERNETICA: The count of the 1st section students.
            key INFORMATICA: The count of the 2nd section students.
            key STATISTICA: The count of the 3rd section students.
            key VIITATOR: The count of the 4th section students.
    """
    r1, r2, r3, r4 = 0, 0, 0, 0

    try:
        for member in members:
            if "CIBERNETICĂ" == member.top_role.name:
                r1 += 1
            elif "INFORMATICĂ ECONOMICĂ" == member.top_role.name:
                r2 += 1
            elif "STATISTICĂ" == member.top_role.name:
                r3 += 1
            elif "VIZITATOR" == member.top_role.name:
                r4 += 1
    except TypeError:
        if "CIBERNETICĂ" == members.top_role.name:
            r1 += 1
        elif "INFORMATICĂ ECONOMICĂ" == members.top_role.name:
            r2 += 1
        elif "STATISTICĂ" == members.top_role.name:
            r3 += 1
        elif "VIZITATOR" == members.top_role.name:
            r4 += 1

    result = {
        "CIBERNETICĂ": r1,
        "INFORMATICĂ ECONOMICĂ": r2,
        "STATISTICĂ": r3,
        "VIZITATOR": r4
    }
    return result


# Intents for Member logging:
intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.messages = True
intents.members = True
intents.reactions = True

# Logging Bot Information:
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
##########################

# Bot Startup:
bot = commands.Bot(command_prefix='$',
                   intents=intents)


@bot.command()  # Server Statistics
async def server(ctx):
    guild = await bot.fetch_guild(606206204699738135)
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


@bot.command()  # Update Hierarchy
async def update(ctx):
    start = datetime.datetime.now()
    guild = await bot.fetch_guild(606206204699738135)
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
        for key, value in temp.items():
            if value == 1:  # False Positive Reference Warning
                good_role = role_dex[key]
        member_roles = [role for role in member.roles if role.name in ["AN I", "AN II", "AN III", "AN IV+"]]
        if len(member_roles) == 0:
            await member.add_roles(good_role, reason="Adaugare rol.")
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


@bot.command()  # About the Bot
async def ver(ctx):
    embed = discord.Embed(color=0x000000)
    embed.set_author(name="About this Bot:")
    about_info_1 = \
        f"""
**Bot Developer:** <@276709808512696320> (중간끝#6826)
**UID:** 613154066662555648
**Latency:** {round(bot.latency * 1000, 2)}ms
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
중간끝 ( B O T ) este momentan la versiunea **2.00b.**

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


@bot.command()
async def clear(ctx, amount):
    try:
        if ctx.author.id in power_users[1:] and int(amount) > 5:
            admin = await bot.fetch_user(power_users[0])
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


@bot.event
async def on_ready():
    print("I'm ready to fight!")


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Bună {member.name}...")
    embed = discord.Embed(color=0x00ff00)
    embed.set_author(name="Bun venit pe Serverul de discord CSIE++ !!")
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Pentru inceput:", value=f"{os.getenv('DM_MESSAGE1')}", inline=False)
    embed.add_field(name="In concluzie:", value=f"{os.getenv('DM_MESSAGE2')}", inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/743466478707409037/744920174477443112/wat.gif")
    await member.dm_channel.send(embed=embed)


@bot.event
async def on_message(ctx):
    if ctx.author == bot.user:
        return

    # We appoint msg the ctx.content.lower() result for easy-typing later on.
    msg = ctx.content.lower()

    # Whois Inspection Tool:
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

    # Avatar Inspection Tool:
    if msg.startswith('avatar') and (ctx.mentions.__len__() > 0):
        for user in ctx.mentions:
            link = user.avatar_url
            await ctx.channel.send(link)

    # Role Selection Command:
    if msg in role_comms and ctx.channel.id == 613817796840914994:
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

    # Allow the bot to process commands:
    await bot.process_commands(ctx)


# keep_alive()
# bot.run(os.getenv('TOKEN'))
bot.run("NjEzMTU0MDY2NjYyNTU1NjQ4.XVsyOQ.C_0hLn4VIfZ5zOyI0Ba2PDDwyyI")
