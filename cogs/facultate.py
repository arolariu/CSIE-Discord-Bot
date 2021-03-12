from discord.ext import commands
from discord_utils import *


class Faculty(commands.Cog, name="================================================\nFacultate"):

    def __init__(self, bot):
        self.bot = bot

    # University Info Command
    @commands.command(help="Vezi informatii despre ASE.",
                      description="Vrei sa vezi detalii despre ASE? Nu mai ezita!\n Sintaxa este:")
    async def ase(self, ctx):
        description = \
            """
Rector ASE: *** Nicolae Istudor ***
> Harta clădirilor din ASE: <http://student.ase.ro/harta-cladirilor/>
> Codificarea sălilor: <http://student.ase.ro/codificarea-salilor/>
> Informații despre facultăți: <https://www.ase.ro/?page=facultati>
> Cazare & Cantină: <http://social.ase.ro/>        
            """
        title = ":bank: ASE INFO :bank: "
        embed = discord.Embed(color=0xACCAFF,
                              title=title,
                              description=description)
        return await ctx.channel.send(embed=embed)

    # Faculty Info Command
    @commands.command(help="Vezi informatii despre CSIE.",
                      description="Vrei sa vezi detalii despre CSIE? Nu mai ezita!\n Sintaxa este:")
    async def csie(self, ctx):
        description = \
            """
Decan CSIE: *** Marian Dârdală ***
> Curriculum secții: <http://www.csie.ase.ro/programe-licenta>
> Orar facultate (SiSC): <https://orar.sisc.ro/>
> Contact secretariat (online): <http://www.csie.ase.ro/secretariat>            
            """
        title = ":bank: CSIE INFO :bank:"
        embed = discord.Embed(color=0xACCAFF,
                              title=title,
                              description=description)
        return await ctx.channel.send(embed=embed)

    # Frequently asked Questions Command
    @commands.command(help="Vezi INTREBARI & RASPUNSURI.",
                      description="Ai cumva o intrebare legata de facultate si nu stii cum sa o adresezi?\nSINTAXA:")
    async def faq(self, ctx):
        title = ":bank: Cele mai frecvente intrebari, alaturi de raspunsuri! :bank:"
        embed = discord.Embed(color=0xACCAFF,
                              title=title,
                              description="Iata cele mai frecvente intrebari ale noilor studenti din CSIE:")
        for item in range(0, len(faq_list), 2):
            is_inline = True if (item + 1) % 3 != 2 else False
            embed.add_field(name=faq_list[item], value=faq_list[item+1], inline=is_inline)
        return await ctx.channel.send(embed=embed)

    # Secretary Information
    @commands.command(help="Vezi Informatii Secretariat.",
                      description="Vrei sa vizualizezi informatii despre secretariat?\nSINTAXA:")
    async def orar(self, ctx):
        description = \
            """
Program secretariat (sala 2011): 
    >> Lu-Ma 11:30-14:00 și 16:00-18:00
    >> Mi-Jo 11:30-14:00 iar Vineri OFF.
            """
        title = ":bank: ORAR SECRETARIAT :bank:"
        embed = discord.Embed(color=0xACCAFF,
                              title=title,
                              description=description)
        return await ctx.channel.send(embed=embed)

    # Get Google Drive Link
    @commands.command(help="Vezi GDrive CSIE++",
                      description="Vrei sa vezi ce materiale se studiaza la facultate?\nSINTAXA:")
    async def gdrive(self, ctx):
        description = "TBA"
        title = ":books: Materiale GDrive :books:"
        embed = discord.Embed(color=0xACCAFF,
                              title=title,
                              description=description)
        return await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Faculty(bot))
