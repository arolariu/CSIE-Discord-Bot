from discord.ext import commands
from discord_utils import *


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author == self.bot.user:
            return
        msg = ctx.content.lower()
        if msg.startswith("help"):
            embed = discord.Embed(color=0xabcdef)
            embed.set_author(name="TABELA DE AJUTOR pentru server CSIE++")
            embed.set_image(url=LOGO_GIF)
            for key, value in commands_list.items():
                embed.add_field(name=key, value=value, inline=False)
            embed.set_footer(text="Vă mulțumim pentru că faceți parte din această comunitate minunată!")
            await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
