import os
import platform

from discord.ext import commands
from discord_utils import *


# To use: $ver in a channel.
class Ver(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Comanda $ver ofera informatii suplimentare despre robot.")
    async def ver(self, ctx):
        embed = discord.Embed(color=0x000000)
        embed.set_author(name="About this Bot:")
        about_info_1 = \
            f"""
    **Bot Developer:** <@276709808512696320> (중간끝#6826)
    **UID:** 613154066662555648
    **Latency:** {round(self.bot.latency * 1000, 2)}ms
    **Current Working Directory:** {os.getcwd()}
    **Operating Platform:** {platform.platform(aliased=True)}
    **Compiler being used:** {platform.python_compiler()}
    **Operating System:** {platform.system()}
    **OS version:** {platform.version()}
    **CPU type:** {platform.processor()}
    **CPU cores:** {os.cpu_count()} cores
            """
        about_info_2 = \
            f"""
    중간끝 ( B O T ) este momentan la versiunea **{VERSION_NUMBER} (Ultima actualizare: {VERSION_DATE})**

    **În această versiune:**
        ```
{VERSION_DATA}
        ```
    """
        embed.add_field(name="Bot Status:", value=about_info_1, inline=False)
        embed.add_field(name="Bot Description:", value=about_info_2, inline=False)
        embed.set_image(url=LOGO_GIF)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Ver(bot))
