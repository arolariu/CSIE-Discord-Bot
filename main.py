import os
import logging

import discord
import cogs

from discord.ext import commands

# Intents for Member logging:
intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.messages = True
intents.members = True
intents.reactions = True

# Logging Bot Information:
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
##########################

# Bot Startup:
bot = commands.Bot(command_prefix='$',
                   intents=intents)


@bot.event
async def on_ready():
    print("I'm ready to fight!")


@bot.event  # When a user types in a message on the Discord Server.
async def on_message(ctx):
    if ctx.author == bot.user:
        return

    # Allow the bot to process commands:
    await bot.process_commands(ctx)


keep_alive()
bot.run(os.getenv('TOKEN'))

# Whois Cog
bot.add_cog(cogs.Whois(bot))
bot.add_cog(cogs.Avatar(bot))
bot.add_cog(cogs.RoleAssign(bot))
bot.add_cog(cogs.PollReactions(bot))
bot.add_cog(cogs.ServerInfo(bot))
bot.add_cog(cogs.UpdateMembers(bot))
bot.add_cog(cogs.BotVersion(bot))
bot.add_cog(cogs.ClearMessages(bot))
bot.add_cog(cogs.CustomRoles(bot))
bot.add_cog(cogs.MemberJoin(bot))
