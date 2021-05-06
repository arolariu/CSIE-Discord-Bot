import discord
from config import *

# EMBED INITIALIZATION:
role_page_1 = discord.Embed(color = discord.Color.blurple())
role_page_1.set_author(name="~ Roluri de FUN 1/2~")
role_page_2 = discord.Embed(color = discord.Color.blurple())
role_page_2.set_author(name="~ Roluri de FUN 2/2 ~")
role_page_3 = discord.Embed(color = discord.Color.blurple())
role_page_3.set_author(name="~ Roluri speciale ~")
role_page_4 = discord.Embed(color = discord.Color.blurple())
role_page_4.set_author(name="~ Tehnologii cunoscute ~")
role_page_5 = discord.Embed(color = discord.Color.blurple())
role_page_5.set_author(name="~ Unde vrei să lucrezi? ~")
role_page_6 = discord.Embed(color = discord.Color.blurple())
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

## SKILL ROLES:
role_page_4.add_field(name='Pentru a vă asigna un rol de pe această pagină, apăsați pe o reacție mai jos ⬇',value="‏‏‎ ‎",inline=False)
role_page_4.add_field(name='1️⃣ <-> C/C++',value="‏‏‎ ‎",inline=False)
role_page_4.add_field(name='2️⃣ <-> C#',value="‏‏‎ ‎",inline=False)
role_page_4.add_field(name='3️⃣ <-> Python',value="‏‏‎ ‎",inline=False)
role_page_4.add_field(name='4️⃣ <-> Java',value="‏‏‎ ‎",inline=False)
role_page_4.add_field(name='5️⃣ <-> JavaScript',value="‏‏‎ ‎",inline=False)
role_page_4.set_footer(text=f'Pagina 4/6\nAi un rol nou? Contactează un @Moderator (font galben)')

## PATH ROLES:
role_page_5.add_field(name='Pentru a vă asigna un rol de pe această pagină, apăsați pe o reacție mai jos ⬇',value="‏‏‎ ‎",inline=False)
role_page_5.add_field(name='1️⃣ <-> Data Scientist',value="‏‏‎ ‎",inline=False)
role_page_5.add_field(name='2️⃣ <-> Software Developer',value="‏‏‎ ‎",inline=False)
role_page_5.add_field(name='3️⃣ <-> Graphics Industry',value="‏‏‎ ‎",inline=False)
role_page_5.add_field(name='4️⃣ <-> Web Developer',value="‏‏‎ ‎",inline=False)
role_page_5.add_field(name='5️⃣ <-> Game Industry',value="‏‏‎ ‎",inline=False)
role_page_5.set_footer(text=f'Pagina 5/6\nAi un rol nou? Contactează un @Moderator (font galben)')

## ORGANIZATION ROLES:
role_page_6.add_field(name='Pentru a vă asigna un rol de pe această pagină, apăsați pe o reacție mai jos ⬇',value="‏‏‎ ‎",inline=False)
role_page_6.add_field(name='1️⃣ <-> SiSC Member',value="‏‏‎ ‎",inline=False)
role_page_6.add_field(name='2️⃣ <-> MLSA Member',value="‏‏‎ ‎",inline=False)
role_page_6.add_field(name='3️⃣ <-> VIP Member',value="‏‏‎ ‎",inline=False)
role_page_6.set_footer(text=f'Pagina 6/6\nAi un rol nou? Contactează un @Moderator (font galben)')

def emoji_convert(current_page, emoji):
    if current_page > 1:
        table = \
           {"1️⃣":0 + (current_page - 1) * 5,
            "2️⃣":1 + (current_page - 1) * 5,
            "3️⃣":2 + (current_page - 1) * 5,
            "4️⃣":3 + (current_page - 1) * 5,
            "5️⃣":4 + (current_page - 1) * 5}
    else:
        table = \
           {"1️⃣":0,
            "2️⃣":1,
            "3️⃣":2,
            "4️⃣":3,
            "5️⃣":4}
    return table[emoji]


role_pages = [role_page_1, role_page_2, role_page_3,
             role_page_4, role_page_5, role_page_6]

