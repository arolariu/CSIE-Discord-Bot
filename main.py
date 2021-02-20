import os
import logging

import discord
from discord.ext import commands

# Intents for Member logging:
intents = discord.Intents().all()

# Logging Bot Information:
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
##########################

# Bot Startup:
bot = commands.Bot(command_prefix='$',
                   intents=intents,
                   description="Acest bot a fost creat de Olariu Alexandru-Razvan de la zero.")


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


@bot.event  # When a user types in a message on the Discord Server.
async def on_message(ctx):
    if ctx.author == bot.user:
        return

    # Allow the bot to process commands:
    await bot.process_commands(ctx)


#keep_alive()
#bot.run(os.getenv('TOKEN'))
