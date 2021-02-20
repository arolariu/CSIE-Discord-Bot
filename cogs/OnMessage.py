import json
from discord.ext import commands


# Helper class for the on_message events.
class OnMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author == self.bot.user:
            return

        # On every message, a user gets 3 credits to spend.
        with open("credits.json", "r") as js:
            data = json.load(js)
        data[str(ctx.author.id)] += 3
        with open("credits.json", "w") as js:
            json.dump(data, js, indent=2)


def setup(bot):
    bot.add_cog(OnMessage(bot))
