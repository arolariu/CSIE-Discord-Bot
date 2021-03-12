from funcs import *


# General Commands Class
class General(commands.Cog, name="================================================\nGeneral"):
    def __init__(self, bot):
        self.bot = bot

    # The command $avatar {user} shows the user's current avatar.
    @commands.command(help="Vezi avatarul unui utilizator.",
                      description="Un avatar tare? Foloseste $avatar {member_tag} pentru a il vedea mai bine!\nSintaxa:")
    async def avatar(self, ctx, user=None):
        await avatar_func(self.bot, ctx, user)

    # The command $whois {user} provides detailed information about a user.
    @commands.command(help="Vezi detalii despre un anumit utilizator.",
                      description="Vrei sa afli mai multe detalii despre un user? Comanda $whois {member_tag} te rezolva!")
    async def whois(self, ctx, user=None):
        await whois_func(ctx, user)

    # The command $wiki {context} provides detailed information about a specified context.
    @commands.command(help="Cauta pe Wikipedia despre ceva!",
                      description="Comanda $wiki cauta pe wikipedia despre contextul specificat.\nSINTAXA:")
    async def wiki(self, ctx, *context):
        await wiki_func(self.bot, ctx, *context)

    # The command $ref {context} provides references to the specified context.
    @commands.command(help="Vezi referinte pentru un subiect.",
                      description="Comanda $ref arata referinte, gasite de pe wikipedia, pentru un context.\nSINTAXA:")
    async def ref(self, ctx, *context):
        await ref_func(self.bot, ctx, *context)


def setup(bot):
    bot.add_cog(General(bot))
