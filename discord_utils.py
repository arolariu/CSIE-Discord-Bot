import datetime
import discord

LOGO_GIF = "https://cdn.discordapp.com/attachments/743466478707409037/744920174477443112/wat.gif"

##################
# VERSION CONTROL:
##################

VERSION_NUMBER = "2.01d"
VERSION_DATA = \
    """
        ++ Actualizat toate librariile interne la ultima versiune, botul are toate functionalitatile posibile pentru Discord.
        ++ O restructurare majora a codului, de la versiunea 1.94 pana acum, codul a fost restructurat in proportie de 95%.
        ++ Actualizarile se pot face on-the-fly, nu mai este nevoie ca botul sa fie coborat si apoi urcat.
        ++ Nu mai are nevoie de mentenanta la finalul fiecarei luni, este 24/7 de acum in colo.
        ++ Simplificat logica pentru asignarea automata a rolului de an, pentru studenti.
        ++ Configuratia interna a botului a fost criptata pentru a spori securitatea.
        ++ Botul are un latency mult mai mic, de 40ms, comparativ cu 150ms.
        ++ Am adoptat o noua arhitectura pentru bot: Plugins + Modules.
        ++ Eficienta sporita cu pana la 100% in unele categorii.
        ++ Reparat si re-simplificat meniul de pe #roles.
        ++ Botul utilizeaza resursele mult mai eficient.
    """

##############################################################################
# Power Users are Users with Granted Privileges - Admins, Moderators, Helpers:
##############################################################################
power_users = \
    [
        276709808512696320,  # OLARIU ALEXANDRU-RAZVAN
        261216306894864396,  # BARGAU MATEI
        3075860320381829,  # DANILA DANIEL
        3422159595719884,  # BROTEA ALEXANDRU
        3760652865305313,  # ALEXANDRU BIANCA
        3241515951409070  # PINTILIE ANDREI
    ]

######################################################
# General Use Commands List (includes TO:DO commands):
######################################################
commands_list = \
    {
        "whois {tag_membru}": "Comanda whois este folosita pentru a analiza profilul unui utilizator Discord.",
        "avatar {tag_membru}": "Comanda avatar este folosita pentru a putea vedea avatarul unui utilizator Discord.",
        "$csie": "Comanda $csie ofera detalii importante despre facultatea de Cibernetica, Statistica si Informatica Economica. ",
        "$ase": "Comanda $ase ofera detalii importante despre Academia de Studii Economice din Bucuresti.",
        "$faq": "Comanda $faq ofera un panou stilizat de tip Frequently Asked Questions, ce sigur te va ajuta in studentie!",
        "$help": "Comanda $help iti prezinta acest meniu frumos redactat, la care deja te uiti! :)"
    }


###################
# Helper Functions:
###################
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


###############################
# FaQ Embed Setup (very long!):
###############################
faq_list = \
    (
        # 0 & 1
        "Q: Cât costă o restanță?",
        "A: 75 RON.",
        # 2 & 3
        "Q: De câte ori pot să dau o restanță?",
        "A: Până ajungi, într-un final, să treci acel examen!",
        # 4 & 5
        "Q: Ce se întâmplă dacă nu reușesc să promovez o materie?",
        "A: Pentru a continua și a nu fi exmatriculat, trebuie să plătești un an suplimentar!",
        # 6 & 7
        "Q: Cât costă un an suplimentar?",
        "A: Anul suplimentar diferă la cost, în funcție de câte restanțe ai și pe ce semestre sunt.",
        # 8 & 9
        "Q: De câte ori îmi pot lua acest an suplimentar?",
        "A: Doar o singură dată.",
        # 10 & 11
        "Q: Ce se întâmplă dacă tot nu reușesc să promovez unele restanțe, în anul suplimentar?",
        "A: Va trebui să te reînscrii la facultate, în anul cel mai mic posibil, acolo unde se predă restanța.",
        # 12 & 13
        "Q: Există un mod de a tranzita din clădirea CSIE în clădirea ASE, rapid?",
        "A: Desigur, la etajul 1 există un pod care leagă cele 3 clădiri principale între ele.",
        # 14 & 15
        "Q: Există un magazin în apropiere de facultate?",
        "A: Da, recomand Carrefour fix de lângă clădirea CSIE, e super bun și are prețuri foarte decente!",
        # 16 & 17
        "Q: Cum pot să verific pe ce dată și în ce sală am examenele?",
        "A: 98% din timp, o să vă arate șeful/șefa de grupă/serie, dacă totuși, nu știe nici ea/el, poți contacta platforma webstudent.ase.ro!",
        # 18 & 19
        "Q: Care lift merge mai bine din cele două din clădire?",
        "A: Cel din dreapta, cel din stânga mereu e ocupat.",
        # 20 & 21
        "Q: Pot recupera seminarele pierdute la alt profesor?",
        "A: În 95% din cazuri, nu vor fi punctate.",
        # 22 & 23
        "Q: Pot recupera seminarele pierdute la altă grupă, cu același profesor?",
        "A: În 70% din cazuri, nu vor fi punctate.",
        # 24 & 25
        "Q: Am nevoie să recuperez cursurile?",
        "A: Cel mai probabil, da. Deoarece se predă foarte multă materie, necesară pentru examen.",
        # 26 & 27
        "Q: Câte prezențe trebuie să am la un seminar? Dar la un curs?",
        "A: La seminar este indicat să ai cel puțin 10 prezențe. La curs, depinde de profesor.",
        # 28 & 29
        "Q: Pot să stau in foișor dacă nu am ce face?",
        "A: Desigur, atâta timp cât gășești și loc :)",
        # 30 & 31
        "Q: Am unde să îmi parchez bicicleta/mașina?",
        "A: Bicicleta desigur, mașina doar pe trotuar, nu recomand.",
        # 32 & 33
        "Q: Mă pot duce la secretariatul din altă cladire dacă am nevoie de ajutor?",
        "A: Cel mai probabil îți va fi spus să te duci la secretariatul din CSIE.",
        # 34 & 35
        "Q: Este obligatorie prezența la cursuri? Dar seminare?",
        "A: Prezența la cursuri este impusă de profesorul de curs. La seminare este obligatorie prezența.",
        # 36 & 37
        "Q: Merită să aștept liftul dacă am multe etaje de urcat?",
        "A: Nu prea merita, decât dacă aveți un profesor care întarzie și el.",
        # 38 & 39
        "Q: Trebuie să vin cu legitimația la examen?",
        "A: Da, este recomandat să aduci și cartea de identitate.",
        # 40 & 41
        "Q: Pot să vin la sala de sport din ASE să mă antrenez?",
        "A: Trebuie să vorbești mai întâi cu profesorul tău de sport.",
        # 42 & 43
        "Q: Pic la taxa dacă am restanță la sport?",
        "A: Da, dacă nu ai reușit să iei celelalte examene.",
        # 44 & 45
        "Q: Pot să închiriez orice carte de la bibliotecă?",
        "A: Desigur, atâta timp cât o înapoiezi în maxim două săptămâni.",
        # 46 & 47
        "Q: Pot să stau cât vreau la bibliotecă?",
        "A: Fiecare bibliotecă din ASE are un program de funcționare.",
        # 48 & 49
        "Q: Pot să merg la alte cămine în vizită?",
        "A: Desigur, dar asigură-te că ai totuși legitimația la tine.",
        # 50 & 51
        "Q: Pot să plătesc taxa/chiria cu cardul/online banking?",
        "A: Desigur! Doar trebuie să completezi corect IBAN-ul și câmpurile necesare."
    )

################################
# Role Pages Setup (very long!):
################################
role_page_1 = discord.Embed(color=discord.Color.blurple(), description="Pagina 1/6")
role_page_1.set_author(name="~ Roluri de FUN 1/2~")
role_page_2 = discord.Embed(color=discord.Color.blurple(), description="Pagina 2/6")
role_page_2.set_author(name="~ Roluri de FUN 2/2 ~")
role_page_3 = discord.Embed(color=discord.Color.blurple(), description="Pagina 3/6")
role_page_3.set_author(name="~ Roluri speciale ~")
role_page_4 = discord.Embed(color=discord.Color.blurple(), description="Pagina 4/6")
role_page_4.set_author(name="~ Tehnologii cunoscute ~")
role_page_5 = discord.Embed(color=discord.Color.blurple(), description="Pagina 5/6")
role_page_5.set_author(name="~ Unde vrei să lucrezi? ~")
role_page_6 = discord.Embed(color=discord.Color.blurple(), description="Pagina 6/6")
role_page_6.set_author(name="~ Membru la o comunitate? ~")

# FUN ROLES PART 1/2:
role_page_1.add_field(name='Pentru a vă asigna un rol de pe această pagină, apăsați pe o reacție mai jos ⬇',
                      value="‏‏‎ ‎", inline=False)
role_page_1.add_field(name='1️⃣ <-> Ofițer', value="‏‏‎ ‎", inline=False)
role_page_1.add_field(name='2️⃣ <-> Drogat', value="‏‏‎ ‎", inline=False)
role_page_1.add_field(name='3️⃣ <-> Scîrțar', value="‏‏‎ ‎", inline=False)
role_page_1.add_field(name='4️⃣ <-> Weeb', value="‏‏‎ ‎", inline=False)
role_page_1.add_field(name='5️⃣ <-> Chad', value="‏‏‎ ‎", inline=False)
role_page_1.set_footer(text=f'Ai un rol nou? Contactează un @Moderator (font galben)')

# FUN ROLES PART 2/2:
role_page_2.add_field(name='Pentru a vă asigna un rol de pe această pagină, apăsați pe o reacție mai jos ⬇',
                      value="‏‏‎ ‎", inline=False)
role_page_2.add_field(name='1️⃣ <-> Bercenar', value="‏‏‎ ‎", inline=False)
role_page_2.add_field(name='2️⃣ <-> Covid-20', value="‏‏‎ ‎", inline=False)
role_page_2.add_field(name='3️⃣ <-> Nașul', value="‏‏‎ ‎", inline=False)
role_page_2.add_field(name='4️⃣ <-> Gay', value="‏‏‎ ‎", inline=False)
role_page_2.add_field(name='5️⃣ <-> Sărac', value="‏‏‎ ‎", inline=False)
role_page_2.set_footer(text=f'Ai un rol nou? Contactează un @Moderator (font galben)')

# SERVER ROLES PART 2/2:
role_page_3.add_field(name='Pentru a vă asigna un rol de pe această pagină, apăsați pe o reacție mai jos ⬇',
                      value="‏‏‎ ‎", inline=False)
role_page_3.add_field(name='1️⃣ <-> DJ', value="Asculti muzica des? Alege acest rol!", inline=False)
role_page_3.add_field(name='2️⃣ <-> Party', value="Te joci des? Alege acest rol!‎", inline=False)
role_page_3.add_field(name='3️⃣ <-> Memer', value="‏‏‎ ‎", inline=False)
role_page_3.add_field(name='4️⃣ <-> LOL-ist', value="Te joci LOL? Alege acest rol!", inline=False)
role_page_3.add_field(name='5️⃣ <-> CSGO-ist', value="Te joci CS:GO? Alege acest rol!", inline=False)
role_page_3.set_footer(text=f'Ai un rol nou? Contactează un @Moderator (font galben)')

# SKILL ROLES:
role_page_4.add_field(name='Pentru a vă asigna un rol de pe această pagină, apăsați pe o reacție mai jos ⬇',
                      value="‏‏‎ ‎", inline=False)
role_page_4.add_field(name='1️⃣ <-> C/C++', value="‏‏‎ ‎", inline=False)
role_page_4.add_field(name='2️⃣ <-> C#', value="‏‏‎ ‎", inline=False)
role_page_4.add_field(name='3️⃣ <-> Python', value="‏‏‎ ‎", inline=False)
role_page_4.add_field(name='4️⃣ <-> Java', value="‏‏‎ ‎", inline=False)
role_page_4.add_field(name='5️⃣ <-> JavaScript', value="‏‏‎ ‎", inline=False)
role_page_4.set_footer(text=f'Ai un rol nou? Contactează un @Moderator (font galben)')

# PATH ROLES:
role_page_5.add_field(name='Pentru a vă asigna un rol de pe această pagină, apăsați pe o reacție mai jos ⬇',
                      value="‏‏‎ ‎", inline=False)
role_page_5.add_field(name='1️⃣ <-> Data Scientist', value="‏‏‎ ‎", inline=False)
role_page_5.add_field(name='2️⃣ <-> Software Developer', value="‏‏‎ ‎", inline=False)
role_page_5.add_field(name='3️⃣ <-> Graphics Industry', value="‏‏‎ ‎", inline=False)
role_page_5.add_field(name='4️⃣ <-> Web Developer', value="‏‏‎ ‎", inline=False)
role_page_5.add_field(name='5️⃣ <-> Game Industry', value="‏‏‎ ‎", inline=False)
role_page_5.set_footer(text=f'Ai un rol nou? Contactează un @Moderator (font galben)')

# ORGANIZATION ROLES:
role_page_6.add_field(name='Pentru a vă asigna un rol de pe această pagină, apăsați pe o reacție mai jos ⬇',
                      value="‏‏‎ ‎", inline=False)
role_page_6.add_field(name='1️⃣ <-> SiSC Member', value="‏‏‎ ‎", inline=False)
role_page_6.add_field(name='2️⃣ <-> MLSA Member', value="‏‏‎ ‎", inline=False)
role_page_6.add_field(name='3️⃣ <-> VIP Member', value="‏‏‎ ‎", inline=False)
role_page_6.set_footer(text=f'Ai un rol nou? Contactează un @Moderator (font galben)')

# Role Pages:
role_pages = [role_page_1, role_page_2, role_page_3,
              role_page_4, role_page_5, role_page_6]

role_comms = ["cibe!", "!cibe", "info!", "!info", "stat!", "!stat", "guest!", "!guest"]
reactions = \
    {
        "da/nu": ("<:vote_yes:742696068172480522>", "<:vote_no:742696120328912936>"),
        "1/2": ("1️⃣", "2️⃣")

    }
