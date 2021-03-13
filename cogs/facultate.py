from discord.ext import commands

from funcs import FacultateFunc
from listeners import facultate_listener


class Faculty(commands.Cog, name="================================================\nFacultate"):

    def __init__(self, bot):
        self.bot = bot

    # University Info Command
    @commands.command(help="Vezi informatii despre ASE.",
                      description="Vrei sa vezi detalii despre ASE? Nu mai ezita!\n Sintaxa este:")
    async def ase(self, ctx):
        return await FacultateFunc(bot=self.bot,
                                   ctx=ctx,
                                   user=None,
                                   amount=None,
                                   context=None).ase_func()

    # Faculty Info Command
    @commands.command(help="Vezi informatii despre CSIE.",
                      description="Vrei sa vezi detalii despre CSIE? Nu mai ezita!\n Sintaxa este:")
    async def csie(self, ctx):
        return await FacultateFunc(bot=self.bot,
                                   ctx=ctx,
                                   user=None,
                                   amount=None,
                                   context=None).csie_func()

    # Frequently asked Questions Command
    @commands.command(help="Vezi INTREBARI & RASPUNSURI.",
                      description="Ai cumva o intrebare legata de facultate si nu stii cum sa o adresezi?\nSINTAXA:")
    async def faq(self, ctx):
        return await FacultateFunc(bot=self.bot,
                                   ctx=ctx,
                                   user=None,
                                   amount=None,
                                   context=None).faq_func()

    # Secretary Information
    @commands.command(help="Vezi Informatii Secretariat.",
                      description="Vrei sa vizualizezi informatii despre secretariat?\nSINTAXA:")
    async def orar(self, ctx):
        return await FacultateFunc(bot=self.bot,
                                   ctx=ctx,
                                   user=None,
                                   amount=None,
                                   context=None).orar_func()

    # Get Google Drive Link
    @commands.command(help="Vezi GDrive CSIE++",
                      description="Vrei sa vezi ce materiale se studiaza la facultate?\nSINTAXA:")
    async def gdrive(self, ctx):
        return await FacultateFunc(bot=self.bot,
                                   ctx=ctx,
                                   user=None,
                                   amount=None,
                                   context=None).gdrive_func()

    # Listener for the DEBUG $print command
    @commands.Cog.listener()
    async def on_message(self, ctx):
        await facultate_listener(bot=self.bot, ctx=ctx)


def setup(bot):
    bot.add_cog(Faculty(bot))
