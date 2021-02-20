from discord.ext import commands


# To use: automatically when the bot is ready to perform his tasks.
class OnReady(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel = self.bot.get_channel(744632571471855807)
        await channel.send("Am primit restart.")


def setup(bot):
    bot.add_cog(OnReady(bot))
