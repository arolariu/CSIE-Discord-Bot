import discord, asyncio, time, os, platform
from discord.utils import get
from discord.ext import tasks, commands
from datetime import datetime
from config import *
from utility import *
from roles import *

client = discord.Client()
current_year = int(datetime.now().year)

def check(member_year, member_month, member_roles):
    if member_year == current_year and member_month > 6:
        return "AN I"
    elif member_year == (current_year - 1) or (member_year == current_year and member_month <= 6):
        return "AN II"
    else:
        return "AN III"


@client.event # Start Bot
async def on_ready():
    global current_page
    channel = client.get_channel(744513142188670977)
    msg = await channel.fetch_message(id=744562841276645457)
    await msg.edit(embed = role_pages[0])
    current_page = 1
    channel = client.get_channel(744632571471855807)
    await channel.send("Am primit restart...")
    if datetime.now().day >= 25:
        await channel.send("O să fiu offline pentru mentenață, până luna viitoare.")
    change_status.start()
    unmute_members.start()


@client.event # DMs
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Bună {member.name}...")
    await member.dm_channel.send(dm_message)


@client.event 
async def on_message(message):
    if message.author == client.user:
        return
    sent_message = (message.content.lower()).split()

        # AUTOMATION COMMAND:
    if message.content.lower().startswith('update!'):
        year_roles = (discord.utils.get(message.guild.roles, name="AN I"),
                      discord.utils.get(message.guild.roles, name="AN II"),
                      discord.utils.get(message.guild.roles, name="AN III"))
        start = datetime.now()
        for member in message.guild.members:
            temp = str(member.joined_at)
            member_year = int(temp[0:4])
            member_month = int(temp[5:7])
            temp = check(member_year,member_month,member.roles)
            member_roles = [role.name for role in member.roles if role in year_roles]
            for role in member_roles:
                if role != temp:
                    await member.remove_roles(discord.utils.get(message.guild.roles, name=role))
                    member_roles.remove(role)
            if len(member_roles) < 1:
                await member.add_roles(discord.utils.get(message.guild.roles, name=temp))
        end = datetime.now()
        elapsed = end - start
        embed=discord.Embed(colour=discord.Colour.red())
        embed.set_footer(text=f'Procedura de update a durat aproximativ {round(elapsed.seconds, 2)} de secunde..')
        await message.channel.send(embed=embed, delete_after=30)

        # WHOIS COMMAND:
    if message.content.lower().startswith('whois') > 0 and (message.mentions.__len__() > 0):
        for user in message.mentions:
            whois=discord.Embed(colour=0xff0000)
            whois.set_author(name=f" whois performed ~ {user}", icon_url = user.avatar_url)
            whois.set_thumbnail(url = user.avatar_url)
            whois.add_field(name="Username: ", value=user.name, inline=True)
            whois.add_field(name="User ID: ", value=user.id, inline=True)
            whois.add_field(name="Nickname: ", value=user.nick, inline=False)
            whois.add_field(name="Activity: ", value=user.activity, inline=True)
            whois.add_field(name="Status: ", value=user.status, inline=True)
            whois.add_field(name="Voice connected: ", value=user.voice, inline=False)
            whois.add_field(name="Joined server at date: ", value=user.joined_at.strftime("%A, %#d %B %Y, %H:%M"), inline=False)
            whois.add_field(name="Joined discord at date: ", value=user.created_at.strftime("%A, %#d %B %Y, %H:%M"), inline=False)
            whois.add_field(name="Highest role: ", value=user.top_role.mention, inline=False)
            whois.set_image(url=bot_footer)
            whois.set_footer(text=f'whois rulat de @{message.author}\nWHOIS tool creat de către Olariu Alexandru-Răzvan.')
            await message.channel.send(embed=whois)

         # ROLE COMMANDS:
    role_content = ["cibe!", "!cibe", "info!", "!info", "stat!", "!stat", "guest!", "!guest"]
    if role_content.count(message.content.lower()) > 0 and message.channel.id == 613817796840914994:
        try:
            await message.author.add_roles(discord.utils.get(message.guild.roles, name=sectii[message.content.lower()]))
            await message.add_reaction(emoji="✔")
        except:
            await message.add_reaction(emoji="❌")
            await message.channel.send("O eroare necunoscută a apărut...te rog mai încearcă!!")
   
        # AVATAR COMMAND:
    if message.content.lower().startswith('avatar') and (message.mentions.__len__() > 0):
        for user in message.mentions:
            link = user.avatar_url
            await message.channel.send(link)

        # USER COMMANDS:
    if sent_message[0] in commands_list:
        await message.add_reaction(emoji="❤")
        try:
            await message.channel.send(embed=commands[sent_message[0]])
        except:
            await message.channel.send(commands[sent_message[0]])

        # VOTE REACTIONS:
    if sent_message[-1] in reactions_list:
        await message.add_reaction(emoji=reactions[reactions_list[reactions_list.index(sent_message[-1])]][0])
        await message.add_reaction(emoji=reactions[reactions_list[reactions_list.index(sent_message[-1])]][1])

        # ABOUT COMMAND:
    if message.content.lower().startswith("about!"):
        an1, an2, an3, an4 = 0, 0, 0, 0
        for member in message.guild.members:
            if discord.utils.get(message.guild.roles, name="AN I") in member.roles:
                an1 += 1
            elif discord.utils.get(message.guild.roles, name="AN II") in member.roles:
                an2 += 1
            elif discord.utils.get(message.guild.roles, name="AN III") in member.roles:
                an3 += 1
            else:
                an4 += 1
        embed_icon = "https://cdn.discordapp.com/avatars/613154066662555648/a12968ad8870fe87fa4446b79036542a.webp?size=1024"
        ping = round(client.latency * 1000, 2)
        try:
            about_value_1 = \
f"""
**Developer:** <@276709808512696320> (중간끝#2369)
**Bot UID:** 613154066662555648
**Directory:** {os.getcwd()}
**Latency:** {round(client.latency * 1000 , 2)}ms
**Operating System:** {platform.system()}
**OS version:** {platform.release()}
**CPU type:** {platform.processor()}
**Available RAM:** 256 GB DDR4 RAM
**Available HDD Space:** {round(round(get_size() / (1024* 1024) * 100 + 90, 4) / 1024, 2)} TB
**Uptime:** N/A. (Bot restarts at the end of the month)
"""
            about_value_2 = \
f"""
**Bot created at:** Monday, 19 August 2019, 23:35
**Bot joined at:** Monday, 19 August 2019, 23:44
**Users served:** {len(message.guild.members)}
**Moderators:** {len(moderatori)}
**AN I Members:** {an1} Members. ({round(an1 * 100 / len(message.guild.members), 2)}% of total)
**AN II Members:** {an2} Members. ({round(an2 * 100 / len(message.guild.members), 2)}% of total) 
**AN III Members:** {an3} Members. ({round(an3 * 100 / len(message.guild.members), 2)}% of total)
**New Members:** {an4} Members. 
"""
        except Exception:
            about_value_1, about_value_2 = "Could not retrieve HOST DATA.", "Could not retrieve SERVER DATA."
        about = discord.Embed(color=discord.Color.default())
        about.set_author(name="중간끝 BOT | v1.93c",icon_url=embed_icon)
        about.add_field(name="General Information",value=about_value_1, inline=False)
        about.add_field(name="‏‏‎ ‎",value="‏‏‎ ‎",inline=False)
        about.add_field(name="Server Statistics",value=about_value_2,inline=False)
        about.set_image(url=bot_footer)
        about.set_footer(text="중간끝 BOT is standalone bot that uses Python and C libs.\n‏‏‎ ‎‏‏‎ ‎‏‏‎‏‏‎     ‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎Graphic Designer: Doysler#6490")
        await message.channel.send(embed=about)


    # MODERATOR COMMANDS:     
    if message.author.id in moderatori:

            # MUTE COMMAND:
        if message.content.lower().startswith(".mute") and (message.mentions.__len__() > 0):
            number = message.content.split()
            for user in message.mentions:
                try:
                    muted_members.append(user)
                    muted_members.append(int(number[2]))
                    embed=discord.Embed(colour=discord.Colour.red())
                    embed.set_footer(text=f'Membrul @{user.name} cu ID-ul {user.id} a primit *MUTE* pentru {int(number[2])} de minute...')
                    await user.add_roles(discord.utils.get(message.guild.roles, name="MUTED"))
                    await message.channel.send(embed = embed, delete_after = 180)
                except Exception:
                    pass

            # UNMUTE COMMAND:
        if message.content.lower().startswith(".unmute") and (message.mentions.__len__() > 0):
            for user in message.mentions:
                try:
                    await user.remove_roles(discord.utils.get(message.guild.roles, name="MUTED"))
                    muted_members.clear()
                    await message.channel.send(f"Membrul @{user.name} a primit unmute..")
                except Exception:
                    pass


            # CLEAR COMMAND:
        if message.content.lower().startswith(".clear") :
            number = message.content.split()
            if message.author.id != server_owner and int(number[2]) > 5:
                channel = message.channel
                admin = await client.fetch_user(server_owner)
                istorie = []
                messages = await channel.history(limit=int(number[2])).flatten()
                for msg in messages:
                    istorie.append(f"{msg.author} : {msg.content}")
                    istorie.append("\n")
                istorie = [message for message in istorie[::-1]]
                full_history = "".join(istorie)
                abuse = await admin.create_dm()
                await abuse.send(full_history)
                if int(number[2]) <= 50:
                    await message.channel.purge(limit = int(number[2]))
                else:
                    await message.channel.send("Maximul de mesaje șterse simultan este de 50.", delete_after=5)
            else:
                await message.channel.purge(limit = int(number[2]))


@client.event
async def on_raw_reaction_add(payload):
    global current_page
    channel = client.get_channel(744513142188670977)
    message_id = payload.message_id
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
    member_id = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
    msg = await channel.fetch_message(id=744562841276645457)
    if message_id == 744562841276645457:
        if payload.emoji.name == "👈":
            if current_page > 1:
                current_page -= 1
                await msg.edit(embed = role_pages[current_page - 1])
            else:
                current_page = 6
                await msg.edit(embed = role_pages[current_page - 1])
            await msg.remove_reaction(member=member_id, emoji="👈")
        elif payload.emoji.name == "👉":
            if current_page < 6:
                current_page += 1
                await msg.edit(embed = role_pages[current_page - 1])
            else:
                current_page = 1
                await msg.edit(embed = role_pages[current_page - 1])
            await msg.remove_reaction(member=member_id, emoji="👉")
        else:
            try:
                switch = emoji_convert(current_page, payload.emoji.name)
                custom_role = discord.utils.get(guild.roles, name=role_addons[switch])
                await member_id.add_roles(custom_role)
                await msg.remove_reaction(member=member_id, emoji=payload.emoji.name)
            except Exception:
                pass
    
@tasks.loop(seconds=status_timer)
async def change_status():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name = next(status) ))

@tasks.loop(minutes=10)
async def unmute_members():
    if len(muted_members) > 0 and muted_members[1] <= 0:
        guild = discord.utils.find(lambda g: g.id == 606206204699738135, client.guilds)
        for user in muted_members:
            await user.remove_roles(discord.utils.get(guild.roles, name="MUTED"))
            muted_members.clear()
    else:
        try:
            muted_members[1] -= 10
        except Exception:
            pass
client.run(token)