import os
import logging

import discord
from discord.ext import commands

# Intents for Member logging:
intents = discord.Intents().all()

# Logging Bot Information:
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
##########################

# Bot Startup:
bot = commands.Bot(command_prefix='$',
                   intents=intents,
                   description="Acest bot a fost creat de 중간끝#6826 de la zero (0%).",
                   activity=discord.Activity(type=discord.ActivityType.watching, name="pe cei care scriu $help"))


@bot.command(help="Incarca un plugin.")
async def load(ctx, extension):
    if ctx.author.id == 276709808512696320:
        bot.load_extension(f'cogs.{extension}')
    else:
        return ctx.channel.send("Doar 중간끝#6826 are acces la aceasta comanda.")


@bot.command(help="Descarca un plugin.")
async def unload(ctx, extension):
    if ctx.author.id == 276709808512696320:
        bot.unload_extension(f'cogs.{extension}')
    else:
        return ctx.channel.send("Doar 중간끝#6826 are acces la aceasta comanda.")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

#keep_alive()
#bot.run(os.getenv('TOKEN'))
