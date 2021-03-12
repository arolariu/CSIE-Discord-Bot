from discord.ext import commands
from funcs import *


class Fun(commands.Cog, name="================================================\nCasino"):
    def __init__(self, bot):
        self.bot = bot

    # Ruleta is a fun mini-game where users can bet their credits away.
    @commands.command(help="Joaca la ruleta!",
                      description="Pentru a folosi $ruleta, ai nevoie de o balanta de credite pozitiva!\nSintaxa:")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def ruleta(self, ctx, amount=5):
        await ruleta_func(ctx, amount)

    # Ruleta Command Error Handler:
    @ruleta.error
    async def ruleta_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(
                title=f":exclamation: Deja ai pariat la ruleta, mai asteapta {error.retry_after:.2f} sec :exclamation:",
                color=0xFF0000)
            await ctx.channel.send(embed=embed, delete_after=5)

    @commands.command(help="Joaca la slots!",
                      description="Pentru a folosi $slots, ai nevoie de o balanta de credite pozitiva!\nSintaxa:")
    @commands.cooldown(1, 6, commands.BucketType.user)
    async def slots(self, ctx, amount=5):
        await slots_func(ctx, amount)

    # Slots Command Error Handler:
    @slots.error
    async def slots_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(
                title=f":exclamation: Deja ai pariat la slots, mai asteapta {error.retry_after:.2f} sec :exclamation:",
                color=0xFF0000)
            await ctx.channel.send(embed=embed, delete_after=5)

    # The $balance command shows users their current credit score balance.
    @commands.command(help="Arata cate credite are un utilizator.",
                      description="Poti specifica, optional, un user.\nSintaxa:")
    async def balance(self, ctx, user=None):
        await balance_func(self.bot, ctx, user)

    # The $donate command allows users to trade credits with each other.
    @commands.command(help="Doneaza o suma modica unui utilizator.",
                      description="Comanda $donate iti permite sa donezi credite unui alt utilizator.\nSINTAXA:")
    async def donate(self, ctx, user=None, amount=0):
        await donate_func(self.bot, ctx, user, amount)

    # The $deposit command allows users to safely stash away credits in an account.
    @commands.command(help="Depoziteaza-ti creditele intr-un loc sigur!",
                      description="Comanda $deposit te ajuta sa iti depozitezi banii intr-un loc sigur, unde nu pot fi furati.\nSINTAXA:")
    async def deposit(self, ctx, amount=0):
        await deposit_func(ctx, amount)

    # The $loan command allows users to retrieve some credits from their account.
    @commands.command(help="Scoate niste credite din depozit.",
                      description="Comanda $loan iti permite sa scoti credite din contul tau bancar (depozit).\nSINTAXA:")
    async def loan(self, ctx, amount=0):
        await loan_func(ctx, amount)

    # The $check command allows users to check their bank account.
    @commands.command(help="Vezi cati bani ai in depozit.",
                      description="Comanda $check iti permite vizualizarea numerarului din depozit.\nSINTAXA:")
    async def check(self, ctx):
        await check_func(ctx)

    # The $rob command allows uses to attempt to rob other users.
    @commands.command(help="Incearca sa furi credite de la cineva.",
                      description="Comanda $rob iti permite sa incerci sa furi creditele altui utilizator.\nSINTAXA:")
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def rob(self, ctx, user=None):
        await rob_func(self.bot, ctx, user)

    # Rob Command Error Handler:
    @rob.error
    async def rob_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(
                title=f":exclamation: Nu poti fura instant, mai asteapta {error.retry_after:.2f} secunde :exclamation:",
                color=0xFF0000)
            await ctx.channel.send(embed=embed, delete_after=15)

    # The $clasament command shows the top 12 users by their credit score balance.
    @commands.command(help="Vezi cei mai bogati 12 oameni de pe server.",
                      description="Vrei sa vezi top 12 cei mai bogati oameni de pe server? Scrie $clasament!\n Sintaxa:")
    async def clasament(self, ctx):
        await clasament_func(self.bot, ctx)

    # The $daily command gives users a daily bonus of 150 credits.
    @commands.command(help="Scrie $daily pentru o doza de credite!",
                      description="Primeste 350 credite in fiecare zi, cand activezi aceasta comanda!")
    @commands.cooldown(1, 43200, commands.BucketType.user)
    async def daily(self, ctx):
        await daily_func(ctx)

    # Daily Command Error Handler
    @daily.error
    async def daily_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(
                title=f":exclamation: Comanda daily merge odata la 12h, mai asteapta {(error.retry_after / 60):.2f} minute :exclamation:",
                color=0xFF0000)
            await ctx.channel.send(embed=embed, delete_after=30)


def setup(bot):
    bot.add_cog(Fun(bot))
