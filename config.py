# WELCOME TO THE CONFIGURATION PAGE 
# ON THIS PAGE YOU CAN CONFIGURE EVERY
# SETTING FOR THE BOT. (+ TOKEN)

# Enter your discord bot token here:
token = 'YOUR_TOKEN'

# Enter the user ID of the server owner:
server_owner = 0000000

# Footers that appear on some commands:
#
# bot_footer: 
#   -- It can be a GIF, a photo, everything that Discord supports!
#   -- Be careful, format must be: cdn.discordapp.com/attachments/.....
#
# text_footer:
#   -- It should ONLY contain TEXT.
#   -- It will be used whenever the bot can't use bot_footer.
bot_footer = "https://cdn.discordapp.com/attachments/743466478707409037/744920174477443112/wat.gif"
text_footer = "Tabelă de ajutor creată de către Olariu Alexandru-Răzvan."

# Bot activity status text.
# The bot will put a random text from this list
# Every X seconds (status_change). You can change as you wish.
status_timer = 15 # The status will change every 15 seconds.
status_text = \
[
    'Respectați regulamentul !!',               
    'Sunt un mic roboțel !!',                   
    'Fii pozitiv!',                             
    'Mult succes în sesiune !!',                
    'Am fost creat de Olariu Alexandru-Răzvan.',
    'Nu uita să te distrezi!',                  
    'Ai grijă de sănătatea ta!',                
    'Mult succes în continuare!'                
]

# This is the moderators list.
# Moderators have special commands like .mute and .clear
# You just need to enter the user ID and the user becomes a moderator.
moderatori = \
(
    276709808512696320, # RAZVAN
    286208556112412682, # CHRIST
    307586032038182913, # DANIEL
    342215959571988480, # LOWENT
    376065286530531369, # BIENCU
    324151595140907008  # OBAMAG
)

# This is the muted members list.
# Muted members can't speak or type in any channel.
# They shouldn't be able to see any, anyway.
muted_members = []
# This is the DM Message menu.
# When a new user joins your server, he will receive a DM.
# The DM starts with "Hello, @user..." and follows with the below text.
dm_message = \
'''✅
|-> Bun venit pe serverul de discord al facultății CSIE!
|-> Poti purta discuții cu ceilalți membrii, să asculți muzică, să te joci cu colegii de facultate.
|-> Pentru început, trebuie să te duci pe server și să cauți canalul numit #✅│sectie-csie 
|-> Apoi, scrie la ce secție ai fost repartizat/ă ! Cum poți face acest lucru? Simplu:
|-> cibe! pentru cibernetică, info! pentru informatică și stat! pentru statistică!
|-> ATENȚIE: Dacă faci parte de la o altă facultate, atunci scrie vizitator!
|-> Aceste roluri contribuie la structurarea serverului și la o performanță cât mai bună.
|-> Tot ce a mai rămas de făcut este să te distrezi ! Pentru comenzi, scrie help! (pe server)
|-> Dacă ai sugestii sau îți dorești să contribui la acest server, uite cum se procedează:
|-> Un simplu tag de genul @Moderator sau @Admin, însoțit cu mesajul tău, este tot ce trebuie! 
|-> BOT CONTACT:
--------------------------------------------------------
    -- Instagram: @ufcolonel
    -- Steam: https://steamcommunity.com/id/M4rad3s/ 
    -- Discord: 중간끝#2369
--------------------------------------------------------
WARNING: Vă rugăm să nu folosiți @everyone pentru a nu deranja ceilalți membri, mulțumim și spor în continuare!
One last thing, te poți introduce pe canalul #intros, dacă dorești :D'''

# This is the HELP menu.
# It works as follows:
#   -- the commands are paired with their info box;
#   -- this means that when a user types help!
#   -- they can see the available commands and their info;
# Currently, there are 9 available commands.
# To disable a command, it's enough to clear it from the list.
help_list = \
(
    # 1
"help!",
"Comanda help! te aduce aici, la tabela de ajutor, din nou.",
    
    # 2
"faq!",
"Comanda faq! oferă o tabelă cu cele mai uzuale întrebări despre facultate.",

    # 3
"ver!",
"Comanda ver! afișează versiunea actuală a robotului.",    
    
    # 4
"ase!",
"Comanda ase! oferă informații generale despre ASE.",

    # 5
"csie!",
"Comanda csie! oferă informații generale despre CSIE.",
    # 6
"gdrive!",
"Puteți scrie gdrive! pentru a accesa materiale gratuite de învățat.",
    # 7
"about!",
"Comanda about! arată toate statisticile botului.",
    # 8
"avatar @{utilizator}",
"Comanda avatar @utilizator permite vizualizarea unui avatar al unei persoane.",
    # 9
"whois @{utilizator}",
"Comanda whois @utilizator ofera informații generale despre un utilizator."
)

# This is the Frequently asked Questions menu.
# A user can type faq! and this menu will appear.
# Currently, there are 25 sets of QnA.
# You can modify them as you wish.
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
"A: Da, recomand Carrefour fix de lângă clădirea CSIE, e super bun și are prețuri decente!",
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

# You can also set up custom roles for your server.
# To be able to add custom roles to your server you MUST:
# 1) Edit the role_addons with what custom roles you want;
# 2) Add them to the server, EXACTLY as you typed them here;
# 3) Be careful! You can ONLY have 5 custom roles PER line.
# There are currently 6 (six) pages of custom roles.
# If you wish to only have two pages, then the structure of role_addons should be:
# line 1: 5 custom roles.
# line 2: 1-5 custom roles.
# line 3-6: 5 x None.
role_addons = \
[
    "Ofițer", "Drogat", "Scîrțar", "Weeb", "Chad",                #1
    "Bercenar", "Covid-20", "Nașul", "Gay", "Sărac",              #2
    "DJ", "Party", "Memer", "LOL-ist", "CSGO-ist",                #3
    "C/C++", "C#", "Python", "Java", "JavaScript",                #4
    "Data Scientist", "Software Developer", "Graphics Industry", "Web Developer", "Game Industry",
    "SiSC Member", "MLSA Member", "VIP Member", None, None        #6
]