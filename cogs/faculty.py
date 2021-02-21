from discord.ext import commands
from discord_utils import *


class Faculty(commands.Cog, name="================================================\nFacultate"):

    def __init__(self, bot):
        self.bot = bot

    # University Info Command
    @commands.command(help="Vezi informatii despre ASE.",
                      description="Vrei sa vezi detalii despre ASE? Nu mai ezita!\n Sintaxa este:")
    async def ase(self, ctx):
        embed = discord.Embed(color=0xACCAFF)
        pass

    # Faculty Info Command
    @commands.command(help="Vezi informatii despre CSIE.",
                      description="Vrei sa vezi detalii despre CSIE? Nu mai ezita!\n Sintaxa este:")
    async def csie(self, ctx):
        embed = discord.Embed(color=0xACCAFF)
        pass

    # Frequently asked Questions Command
    @commands.command(help="Vezi INTREBARI & RASPUNSURI.",
                      description="Ai cumva o intrebare legata de facultate si nu stii cum sa o adresezi?\nSINTAXA:")
    async def faq(self, ctx):
        embed = discord.Embed(color=0xACCAFF)
        pass

    # Secretary Information
    @commands.command(help="Vezi Informatii Secretariat.",
                      description="Vrei sa vizualizezi informatii despre secretariat?\nSINTAXA:")
    async def orar(self, ctx):
        embed = discord.Embed(color=0xACCAFF)
        pass

    # Get Google Drive Link
    @commands.command(help="Vezi GDrive CSIE++",
                      description="Vrei sa vezi ce materiale se studiaza la facultate?\nSINTAXA:")
    async def gdrive(self, ctx):
        embed = discord.Embed(color=0xACCAFF)
        pass


def setup(bot):
    bot.add_cog(Faculty(bot))
