import datetime
import discord

role_page_1 = discord.Embed(color = discord.Color.blurple(), description="Pagina 1/6")
role_page_1.set_author(name="~ Roluri de FUN 1/2~")
role_page_2 = discord.Embed(color = discord.Color.blurple(), description="Pagina 2/6")
role_page_2.set_author(name="~ Roluri de FUN 2/2 ~")
role_page_3 = discord.Embed(color = discord.Color.blurple(), description="Pagina 3/6")
role_page_3.set_author(name="~ Roluri speciale ~")
role_page_4 = discord.Embed(color = discord.Color.blurple(), description="Pagina 4/6")
role_page_4.set_author(name="~ Tehnologii cunoscute ~")
role_page_5 = discord.Embed(color = discord.Color.blurple(), description="Pagina 5/6")
role_page_5.set_author(name="~ Unde vrei să lucrezi? ~")
role_page_6 = discord.Embed(color = discord.Color.blurple(), description="Pagina 6/6")
role_page_6.set_author(name="~ Membru la o comunitate? ~")

# FUN ROLES PART 1/2:
role_page_1.add_field(name='Pentru a vă asigna un rol de pe această pagină, apăsați pe o reacție mai jos ⬇',value="‏‏‎ ‎",inline=False)
role_page_1.add_field(name='1️⃣ <-> Ofițer',value="‏‏‎ ‎",inline=False)
role_page_1.add_field(name='2️⃣ <-> Drogat',value="‏‏‎ ‎",inline=False)
role_page_1.add_field(name='3️⃣ <-> Scîrțar',value="‏‏‎ ‎",inline=False)
role_page_1.add_field(name='4️⃣ <-> Weeb',value="‏‏‎ ‎",inline=False)
role_page_1.add_field(name='5️⃣ <-> Chad',value="‏‏‎ ‎",inline=False)
role_page_1.set_footer(text=f'Pagina 1/6\nAi un rol nou? Contactează un @Moderator (font galben)')

# FUN ROLES PART 2/2:
role_page_2.add_field(name='Pentru a vă asigna un rol de pe această pagină, apăsați pe o reacție mai jos ⬇',value="‏‏‎ ‎",inline=False)
role_page_2.add_field(name='1️⃣ <-> Bercenar',value="‏‏‎ ‎",inline=False)
role_page_2.add_field(name='2️⃣ <-> Covid-20',value="‏‏‎ ‎",inline=False)
role_page_2.add_field(name='3️⃣ <-> Nașul',value="‏‏‎ ‎",inline=False)
role_page_2.add_field(name='4️⃣ <-> Gay',value="‏‏‎ ‎",inline=False)
role_page_2.add_field(name='5️⃣ <-> Sărac',value="‏‏‎ ‎",inline=False)
role_page_2.set_footer(text=f'Pagina 2/6\nAi un rol nou? Contactează un @Moderator (font galben)')

# SERVER ROLES PART 2/2:
role_page_3.add_field(name='Pentru a vă asigna un rol de pe această pagină, apăsați pe o reacție mai jos ⬇',value="‏‏‎ ‎",inline=False)
role_page_3.add_field(name='1️⃣ <-> DJ',value="Asculti muzica des? Alege acest rol!",inline=False)
role_page_3.add_field(name='2️⃣ <-> Party',value="Te joci des? Alege acest rol!‎",inline=False)
role_page_3.add_field(name='3️⃣ <-> Memer',value="‏‏‎ ‎",inline=False)
role_page_3.add_field(name='4️⃣ <-> LOL-ist',value="Te joci LOL? Alege acest rol!",inline=False)
role_page_3.add_field(name='5️⃣ <-> CSGO-ist',value="Te joci CS:GO? Alege acest rol!",inline=False)
role_page_3.set_footer(text=f'Pagina 3/6\nAi un rol nou? Contactează un @Moderator (font galben)')

# SKILL ROLES:
role_page_4.add_field(name='Pentru a vă asigna un rol de pe această pagină, apăsați pe o reacție mai jos ⬇',value="‏‏‎ ‎",inline=False)
role_page_4.add_field(name='1️⃣ <-> C/C++',value="‏‏‎ ‎",inline=False)
role_page_4.add_field(name='2️⃣ <-> C#',value="‏‏‎ ‎",inline=False)
role_page_4.add_field(name='3️⃣ <-> Python',value="‏‏‎ ‎",inline=False)
role_page_4.add_field(name='4️⃣ <-> Java',value="‏‏‎ ‎",inline=False)
role_page_4.add_field(name='5️⃣ <-> JavaScript',value="‏‏‎ ‎",inline=False)
role_page_4.set_footer(text=f'Pagina 4/6\nAi un rol nou? Contactează un @Moderator (font galben)')

# PATH ROLES:
role_page_5.add_field(name='Pentru a vă asigna un rol de pe această pagină, apăsați pe o reacție mai jos ⬇',value="‏‏‎ ‎",inline=False)
role_page_5.add_field(name='1️⃣ <-> Data Scientist',value="‏‏‎ ‎",inline=False)
role_page_5.add_field(name='2️⃣ <-> Software Developer',value="‏‏‎ ‎",inline=False)
role_page_5.add_field(name='3️⃣ <-> Graphics Industry',value="‏‏‎ ‎",inline=False)
role_page_5.add_field(name='4️⃣ <-> Web Developer',value="‏‏‎ ‎",inline=False)
role_page_5.add_field(name='5️⃣ <-> Game Industry',value="‏‏‎ ‎",inline=False)
role_page_5.set_footer(text=f'Pagina 5/6\nAi un rol nou? Contactează un @Moderator (font galben)')

# ORGANIZATION ROLES:
role_page_6.add_field(name='Pentru a vă asigna un rol de pe această pagină, apăsați pe o reacție mai jos ⬇',value="‏‏‎ ‎",inline=False)
role_page_6.add_field(name='1️⃣ <-> SiSC Member',value="‏‏‎ ‎",inline=False)
role_page_6.add_field(name='2️⃣ <-> MLSA Member',value="‏‏‎ ‎",inline=False)
role_page_6.add_field(name='3️⃣ <-> VIP Member',value="‏‏‎ ‎",inline=False)
role_page_6.set_footer(text=f'Pagina 6/6\nAi un rol nou? Contactează un @Moderator (font galben)')

# Role Pages:
role_pages = [role_page_1, role_page_2, role_page_3,
              role_page_4, role_page_5, role_page_6]

role_comms = ["cibe!", "!cibe", "info!", "!info", "stat!", "!stat", "guest!", "!guest"]
reactions = \
    {
        "da/nu": ("<:vote_yes:742696068172480522>", "<:vote_no:742696120328912936>"),
        "1/2": ("1️⃣", "2️⃣")

    }

power_users = \
    [
        276709808512696320,  # RAZVAN
        261216306894864396,  # BARGAU
        3075860320381829,  # DANIEL
        3422159595719884,  # LOWENT
        3760652865305313,  # BIENCU
        3241515951409070  # OBAMAG
    ]

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

