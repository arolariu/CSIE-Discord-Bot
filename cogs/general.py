from discord.ext import commands

from funcs import GeneralFunc
from listeners import general_listener


# General Commands Class
class General(commands.Cog, name="================================================\nGeneral"):
    def __init__(self, bot):
        self.bot = bot

    # The command $avatar {user} shows the user's current avatar.
    @commands.command(help="Vezi avatarul unui utilizator.",
                      description="Un avatar tare? Foloseste $avatar {member_tag} pentru a il vedea mai bine!\nSintaxa:")
    async def avatar(self, ctx, user=None):
        return await GeneralFunc(bot=self.bot,
                                 ctx=ctx,
                                 user=user,
                                 amount=None,
                                 context=None).avatar_func()

    # The command $whois {user} provides detailed information about a user.
    @commands.command(help="Vezi detalii despre un anumit utilizator.",
                      description="Vrei sa afli mai multe detalii despre un user? Comanda $whois {member_tag} te rezolva!")
    async def whois(self, ctx, user=None):
        return await GeneralFunc(bot=self.bot,
                                 ctx=ctx,
                                 user=user,
                                 amount=None,
                                 context=None).whois_func()

    # The command $wiki {context} provides detailed information about a specified context.
    @commands.command(help="Cauta pe Wikipedia despre ceva!",
                      description="Comanda $wiki cauta pe wikipedia despre contextul specificat.\nSINTAXA:")
    async def wiki(self, ctx, *context):
        return await GeneralFunc(bot=self.bot,
                                 ctx=ctx,
                                 user=None,
                                 amount=None,
                                 context=context).wiki_func()

    # The command $ref {context} provides references to the specified context.
    @commands.command(help="Vezi referinte pentru un subiect.",
                      description="Comanda $ref arata referinte, gasite de pe wikipedia, pentru un context.\nSINTAXA:")
    async def ref(self, ctx, *context):
        return await GeneralFunc(bot=self.bot,
                                 ctx=ctx,
                                 user=None,
                                 amount=None,
                                 context=context).ref_func()

    # Listener for the DEBUG $print command
    @commands.Cog.listener()
    async def on_message(self, ctx):
        await general_listener(bot=self.bot, ctx=ctx)


def setup(bot):
    bot.add_cog(General(bot))
