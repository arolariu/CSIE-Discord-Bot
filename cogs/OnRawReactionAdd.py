from discord.ext import commands
from discord_utils import *


# To use: react to a *SPECIFIC* message in a *SPECIFIC* channel.
class OnRawReactionAdd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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


def setup(bot):
    bot.add_cog(OnRawReactionAdd(bot))
