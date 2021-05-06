import discord, os
from itertools import cycle
from datetime import datetime
from config import *
from roles import *

# UTILITY FUNCTIONS:
def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size


status = cycle(status_text)

comenzi = (
'''```diff
--> Robot creat de catre Olariu Alexandru-Razvan.
--> Acest robot este momentan la versiunea 1.94b
--> Ultima actualizare: 16/10/2020
        Changelog:
++ 1) Adăugat roluri noi.
++ 2) Îmbunătățit performanța.
++ 3) Îmbunătățit mesajul de bun venit.
++ 4) Botul este mult mai prietenos acum.
```
CONTACT INFO:
    >-- instagram: @ufcolonel
    >-- steam: <https://steamcommunity.com/id/M4rad3s>
    >-- discord: <@276709808512696320>
''',   # 0
''' 
Rector ASE: *** Nicolae Istudor ***
> Harta clădirilor din ASE: <http://student.ase.ro/harta-cladirilor/>
> Codificarea sălilor: <http://student.ase.ro/codificarea-salilor/>
> Informații despre facultăți: <https://www.ase.ro/?page=facultati>
> Cazare & Cantină: <http://social.ase.ro/>
''',   # 1
'''
Decan CSIE: *** Marian Dârdală ***
> Curriculum secții: <http://www.csie.ase.ro/programe-licenta>
> Orar facultate (SiSC): <https://orar.sisc.ro/>
> Contact secretariat (online): <http://www.csie.ase.ro/secretariat>
Program secretariat (sala 2011): 
    >> Lu-Ma 11:30-14:00 și 16:00-18:00
    >> Mi-Jo 11:30-14:00 iar Vineri OFF.
''',   # 2
'''
> Link Gdrive: <https://drive.google.com/drive/folders/1pPdBqCbyVWCxamDHlfv2XAAjoFxqj0rY?usp=sharing>
**Dacă dorești să ajuți cu materiale educaționale, te rog să contactezi pe <@276709808512696320>. 
''',   # 3
'''
În dreapta îți poți vedea colegii de secție. Adițional, ți s-a atribuit și un rol de AN. (vechime pe server)
Îți multumesc frumos pentru că faci parte din acestă comunitate minunată! Dacă ai sugestii, nu ezita să spui! :)
Invită-ți ceilalți colegi de secție! Un simplu share pe grupul seriei, din când în când, ajută enorm!
'''    # 4
)

# FREQUENTLY ASKED QUESTIONS:
faq = discord.Embed(color = discord.Color.purple())
faq.set_author(name="~~ Frequently asked Questions ~~")
for item in range(0, len(faq_list), 2):
    is_inline = True if (item + 1) % 3 != 2 else False
    faq.add_field(name = faq_list[item], value = faq_list[item+1], inline = is_inline)
faq.set_footer(text=text_footer)                                                 

# HELP COMMAND:
help = discord.Embed(color = discord.Color.orange())
help.set_author(name="~ Tabela de ajutor ~")
for item in range(0, len(help_list), 2):
    help.add_field(name = help_list[item], value = help_list[item+1], inline = False)
help.set_image(url=bot_footer)
help.set_footer(text=text_footer)                                                 

# COMMANDS AND REACTIONS TABLES:
commands = \
    {"ver!":comenzi[0],
     "ase!":comenzi[1],
     "csie!":comenzi[2],
     "gdrive!":comenzi[3],
     "help!":help,
     "faq!":faq,
     }
commands_list = list(commands.keys())
reactions = \
    {"da/nu":("<:vote_yes:742696068172480522>","<:vote_no:742696120328912936>"),
     "1/2":("1️⃣","2️⃣")
     }
reactions_list = list(reactions.keys())

# ROLES TABLES:
sectii = \
    {"cibe!":"CIBERNETICĂ",
     "info!":"INFORMATICĂ ECONOMICĂ",
     "stat!":"STATISTICĂ",
     "guest!":"VIZITATOR",
     "!cibe":"CIBERNETICĂ",
     "!info":"INFORMATICĂ ECONOMICĂ",
     "!stat":"STATISTICĂ",
     "!guest":"VIZITATOR"
     }