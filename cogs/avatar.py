from discord.ext import commands


# To use: avatar {member_tag}
class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author == self.bot.user:
            return
        msg = ctx.content.lower()
        if msg.startswith('avatar') and (ctx.mentions.__len__() > 0):
            for user in ctx.mentions:
                link = user.avatar_url
                await ctx.channel.send(link)


def setup(bot):
    bot.add_cog(Avatar(bot))
