import os
import platform

from discord.ext import commands
from discord_utils import *


class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Helper function for the #roles-page on the discord server.
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        guild = await self.bot.fetch_guild(606206204699738135)
        channel = self.bot.get_channel(744513142188670977)
        msg = await channel.fetch_message(id=744562841276645457)
        reaction_dex = \
            {
                "1️⃣": 1,
                "2️⃣": 2,
                "3️⃣": 3,
                "4️⃣": 4,
                "5️⃣": 5
            }
        embed = msg.embeds
        embed_desc = embed[0].description
        role_page = [embed_desc.count(f"Pagina {i}/6") for i in range(1, 7)]
        start_page = role_page.index(1)
        await msg.edit(embed=role_pages[start_page])

        if payload.message_id == 744562841276645457:

            # The user has hit the back page reaction:
            if payload.emoji.name == "👈":
                try:
                    if (start_page - 1) > 0:
                        start_page -= 1
                    else:
                        start_page = 5
                    await msg.edit(embed=role_pages[start_page])
                except Exception as e:
                    print(e)
                await msg.remove_reaction(member=payload.member, emoji="👈")

            # The user has hit the next page reaction:
            elif payload.emoji.name == "👉":
                try:
                    if (start_page + 1) > 5:
                        start_page = 0
                    else:
                        start_page += 1
                    await msg.edit(embed=role_pages[start_page])
                except Exception as e:
                    print(e)
                await msg.remove_reaction(member=payload.member, emoji="👉")

            # The user has hit a role reaction.
            else:
                try:
                    role_dex = \
                        {
                            1: ["Ofițer", "Drogat", "Scîrțar", "Weeb", "Chad"],
                            2: ["Bercenar", "Covid-20", "Nașul", "Gay", "Sărac"],
                            3: ["DJ", "Party", "Memer", "LOL-ist", "CSGO-ist"],
                            4: ["C/C++", "C#", "Python", "Java", "JavaScript"],
                            5: ["Data Scientist", "Software Developer", "Graphics Industry", "Web Developer",
                                "Game Industry"],
                            6: ["SiSC Member", "MLSA Member", "VIP Member", None, None]
                        }
                    custom_role = discord.utils.get(guild.roles,
                                                    name=role_dex[start_page + 1][reaction_dex[payload.emoji.name] - 1])
                    await payload.member.add_roles(custom_role)
                    await msg.remove_reaction(member=payload.member, emoji=payload.emoji.name)
                except Exception as e:
                    print(e)

    # The command $server provides member and server statistics to the users.
    @commands.command(help="Vezi statistici interesante despre server.",
                      description="Comanda $server ofera statistici interesante despre server.\nSINTAXA:")
    async def server(self, ctx):
        guild = await self.bot.fetch_guild(606206204699738135)
        members = await guild.fetch_members(limit=None).flatten()
        year_results = server_years(members)
        role_results = server_roles(members)
        year_values = \
            f"""
**AN I  :** {year_results["AN I"]} membri. ({round(year_results["AN I"] * 100 / len(members), 2)}% din total.)
**AN II :** {year_results["AN II"]} membri. ({round(year_results["AN II"] * 100 / len(members), 2)}% din total.)
**AN III:** {year_results["AN III"]} membri. ({round(year_results["AN III"] * 100 / len(members), 2)}% din total.)
**Alumni:** {year_results["AN IV+"]} membri. ({round(year_results["AN IV+"] * 100 / len(members), 2)}% din total.)
            """

        role_values = \
            f"""
**CIBERNETICĂ:** {role_results["CIBERNETICĂ"]} membri. ({round(role_results["CIBERNETICĂ"] * 100 / len(members), 2)}% din total.)
**INFORMATICĂ:** {role_results["INFORMATICĂ ECONOMICĂ"]} membri. ({round(role_results["INFORMATICĂ ECONOMICĂ"] * 100 / len(members), 2)}% din total.)
**STATISTICĂ :** {role_results["STATISTICĂ"]} membri. ({round(role_results["STATISTICĂ"] * 100 / len(members), 2)}% din total.)
**VIZITATORI :** {role_results["VIZITATOR"]} membri. ({round(role_results["VIZITATOR"] * 100 / len(members), 2)}% din total.) 
            """

        result = discord.Embed(color=0xff0000)
        result.set_author(name="Statistica Server CSIE++")
        result.add_field(name="După vechime:", value=year_values, inline=False)
        result.add_field(name="După secție :", value=role_values, inline=False)
        result.add_field(name=f"TOTAL MEMBRI: {len(members)}", value="Vă mulțumim tuturor!!!", inline=False)
        return await ctx.send(embed=result)

    # The command $ver provides useful information about the bot to the users.
    @commands.command(help="Vezi informatii suplimentare despre robot.",
                      description="Comanda $ver ofera informatii suplimentare despre robot.\nSINTAXA:")
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
        return await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Utils(bot))
