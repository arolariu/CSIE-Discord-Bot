import random
import discord
import json

from asyncio import sleep
from discord.ext import commands


class Fun(commands.Cog, name="================================================\nCasino"):
    def __init__(self, bot):
        self.bot = bot

    # Ruleta is a fun mini-game where users can bet their credits away.
    @commands.command(help="Joaca la ruleta!",
                      description="Pentru a folosi $ruleta, ai nevoie de o balanta de credite pozitiva!\nSintaxa:")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def ruleta(self, ctx, amount):
        emoji_dex = \
            {":one:": 1, ":two:": 2, ":three:": 3,
             ":four:": 4, ":five:": 5, ":six:": 6,
             ":seven:": 7, ":eight:": 8, ":nine:": 9}
        try:
            amount = int(amount)
        except ValueError:
            return await ctx.channel.send("Sigur ai formulat corect comanda?")
        user = str(ctx.author.id)

        # JSON Check if the user has enough credits.
        with open("credits.json", "r") as js:
            try:
                data = json.load(js)
                if user not in data.keys():
                    return await ctx.channel.send("Nu poti paria momentan. Contacteaza un moderator.")
                elif user in data.keys() and data[user] < 0:
                    return await ctx.channel.send("Nu poti paria. Balanta ta este 0.")
                elif user in data.keys() and data[user] < amount:
                    return await ctx.channel.send("Nu poti paria mai mult decat ai in portofel.")
            except ValueError:  # JSONDecodeError
                return await ctx.channel.send("Eroare interna. Contacteaza-l pe 중간끝#6826")

        # We play the main game, if we have not returned yet.
        temp = "Numere pe ruleta:\n"
        first = random.choice(list(emoji_dex.keys()))
        embed = discord.Embed(title="RULETA",
                              color=0x00FF00,
                              description=temp + first)
        msg = await ctx.channel.send(embed=embed)

        # Now we get the second number.
        await sleep(0.3)
        second = random.choice(list(emoji_dex.keys()))
        embed.description = temp + first + "--" + second
        await msg.edit(embed=embed)

        # Now we get the third and final number.
        await sleep(0.3)
        third = random.choice(list(emoji_dex.keys()))
        embed.description = temp + first + "--" + second + "--" + third
        await msg.edit(embed=embed)

        # We do some setup for the final result:
        await sleep(0.6)
        numbers = (emoji_dex[first], emoji_dex[second], emoji_dex[third])
        numbers = set(numbers)
        result = amount * (-1)  # We initialize result with - amount for the else clause

        # If the user hit 777's:
        if len(numbers) == 1 and 7 in numbers:
            result = amount * 21
            embed.description = \
                f"""
Ai castigat jackpotul cel mare!! (x21 suma pariata)
SUMA PARIATA: {amount} 
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)

        # If the user hit a full line of 6's:
        elif len(numbers) == 1 and 6 in numbers:
            result = amount * 66.6
            embed.description = \
                f"""
Ai castigat jackpotul cel RAU!! (x66.6 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)

        # If the user hit a full line:
        elif len(numbers) == 1:
            result = amount * 13
            embed.description = \
                f"""
Ai castigat!! (x13 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)

        # If the user hit 2 lucky numbers:
        elif len(numbers) == 2 and 7 in numbers:
            result = amount * 2.3
            embed.description = \
                f"""
Ai castigat!! (x2.3 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)

        # If the user hit 2 identic numbers:
        elif len(numbers) == 2 and 7 not in numbers:
            result = amount * 1.7
            embed.description = \
                f"""
Ai castigat!! (x1.7 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)

        # If the user hit a lucky number:
        elif len(numbers) == 3 and 7 in numbers:
            result = amount * 1.3
            embed.description = \
                f"""
Ai castigat!! (x1.3 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)

        # If the user did not hit any winning numbers:
        else:
            embed.colour = 0xFF0000
            embed.description = f"Ai pierdut {amount} credite.."
            await msg.edit(embed=embed)

        # We update the JSON file:
        data[user] += round(result, 3)

        with open("credits.json", "w") as js:
            json.dump(data, js, indent=2)

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
    async def slots(self, ctx, amount):
        emoji_dex = \
            {
                ":apple:": 1,
                ":tangerine:": 2,
                ":pear:": 3,
                ":lemon:": 4,
                ":watermelon:": 5,
                ":grapes:": 6,
                ":strawberry:": 7,
                ":cherries:": 8,
                ":melon:": 9,
                ":avocado:": 10,
                ":eggplant:": 11,
                ":cucumber:": 12,
                ":corn:": 13,
                ":mango:": 14,
                ":peach:": 15,
                ":garlic:": 16
            }
        try:
            amount = int(amount)
        except ValueError:
            return await ctx.channel.send("Sigur ai formulat corect comanda?")
        user = str(ctx.author.id)

        # JSON Check if the user has enough credits.
        with open("credits.json", "r") as js:
            try:
                data = json.load(js)
                if user not in data.keys():
                    return await ctx.channel.send("Nu poti paria momentan. Contacteaza un moderator.")
                elif user in data.keys() and data[user] < 0:
                    return await ctx.channel.send("Nu poti paria. Balanta ta este 0.")
                elif user in data.keys() and data[user] < amount:
                    return await ctx.channel.send("Nu poti paria mai mult decat ai in portofel.")
            except ValueError:  # JSONDecodeError
                return await ctx.channel.send("Eroare interna. Contacteaza-l pe 중간끝#6826")

        # We play the main game, if we have not returned yet.
        temp = "Fructe pe slots:\n"
        first = random.choice(list(emoji_dex.keys()))
        embed = discord.Embed(title="SLOTS",
                              color=0x00FF00,
                              description=temp + first)
        msg = await ctx.channel.send(embed=embed)

        # Now we get the second symbol.
        await sleep(0.3)
        second = random.choice(list(emoji_dex.keys()))
        embed.description = temp + first + second
        await msg.edit(embed=embed)

        # Now we get the third symbol.
        await sleep(0.3)
        third = random.choice(list(emoji_dex.keys()))
        embed.description = temp + first + second + third
        await msg.edit(embed=embed)

        # Now we get the fourth symbol.
        await sleep(0.3)
        fourth = random.choice(list(emoji_dex.keys()))
        embed.description = temp + first + second + third + fourth
        await msg.edit(embed=embed)

        # Now we get the fifth and final symbol.
        await sleep(0.3)
        fifth = random.choice(list(emoji_dex.keys()))
        embed.description = temp + first + second + third + fourth + fifth
        await msg.edit(embed=embed)

        # We do some setup for the final result:
        await sleep(1)
        numbers = (emoji_dex[first], emoji_dex[second], emoji_dex[third], emoji_dex[fourth], emoji_dex[fifth])
        numbers = set(numbers)
        result = amount * (-1)  # We initialize result with - amount for the else clause

        # Winning Stategies:
        # Five Cherries:
        if len(numbers) == 1 and 8 in numbers:
            result = amount * 80085
            embed.description = \
                f"""
Ai castigat!! (x80085 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)
        # Five Eggplants:
        elif len(numbers) == 1 and 11 in numbers:
            result = amount * 6996
            embed.description = \
                f"""
Ai castigat!! (x6996 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)
        # Five Peaches:
        elif len(numbers) == 1 and 15 in numbers:
            result = amount * 6969
            embed.description = \
                f"""
Ai castigat!! (x6969 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)
        # Some Eggplants and some Peaches:
        elif len(numbers) == 2 and 11 in numbers and 15 in numbers:
            result = amount * 69
            embed.description = \
                f"""
Ai castigat!! (x69 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)
        # Some Peaches and some Watermelons:
        elif len(numbers) == 2 and 15 in numbers and 5 in numbers:
            result = amount * 69
            embed.description = \
                f"""
Ai castigat!! (x69 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)
        # Some Avocados and some Eggplants:
        elif len(numbers) == 2 and 10 in numbers and 11 in numbers:
            result = amount * 8080
            embed.description = \
                f"""
Ai castigat!! (x8080 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)
        # Some Apples and some Garlics:
        elif len(numbers) == 2 and 1 in numbers and 16 in numbers:
            result = amount * 1661
            embed.description = \
                f"""
Ai castigat!! (x1661 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)
        # Some Cherries and some Peaches:
        elif len(numbers) == 2 and 8 in numbers and 15 in numbers:
            result = amount * 800.85
            embed.description = \
                f"""
Ai castigat!! (x800.85 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)
        # Some Long Fruits:
        elif len(numbers) == 3 and 11 in numbers and 12 in numbers and 13 in numbers:
            result = amount * 669.9
            embed.description = \
                f"""
Ai castigat!! (x669.9 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)
        # Some Small Fruits:
        elif len(numbers) == 3 and 2 in numbers and 3 in numbers and 6 in numbers:
            result = amount * 666.6
            embed.description = \
                f"""
Ai castigat!! (x666.6 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)
        # Some Unused Fruits:
        elif len(numbers) == 3 and 14 in numbers and 9 in numbers and 7 in numbers:
            result = amount * 350
            embed.description = \
                f"""
Ai castigat!! (x350 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)
        # Some Other Fruits v1:
        elif len(numbers) == 4 and 2 in numbers and 4 in numbers and 14 in numbers:
            result = amount * 30
            embed.description = \
                f"""
Ai castigat!! (x30 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)
        # Some Other Fruits v2:
        elif len(numbers) == 4 and 16 in numbers and 9 in numbers and 4 in numbers:
            result = amount * 30
            embed.description = \
                f"""
Ai castigat!! (x30 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)
        # Some Other Fruits v3:
        elif len(numbers) == 4 and 6 in numbers and 7 in numbers and 8 in numbers:
            result = amount * 30
            embed.description = \
                f"""
Ai castigat!! (x30 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)
        # Some Other Fruits v4:
        elif len(numbers) == 4 and 12 in numbers and 11 in numbers and 13 in numbers:
            result = amount * 30
            embed.description = \
                f"""
Ai castigat!! (x30 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)
        # Some Other Fruits v5:
        elif len(numbers) == 4 and 9 in numbers and 13 in numbers and 6 in numbers:
            result = amount * 30
            embed.description = \
                f"""
Ai castigat!! (x30 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)
        # Some Other Fruits v6:
        elif len(numbers) == 4 and 2 in numbers and 7 in numbers and 12 in numbers:
            result = amount * 30
            embed.description = \
                f"""
Ai castigat!! (x30 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)
        # Some Other Fruits v7:
        elif len(numbers) == 4 and 13 in numbers and 2 in numbers and 6 in numbers:
            result = amount * 30
            embed.description = \
                f"""
Ai castigat!! (x30 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)
        # Some Other Fruits v8:
        elif len(numbers) == 4 and 10 in numbers and 14 in numbers and 16 in numbers:
            result = amount * 30
            embed.description = \
                f"""
Ai castigat!! (x30 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)
        # Some Other Fruits v9:
        elif len(numbers) == 4 and 1 in numbers and 11 in numbers and 7 in numbers:
            result = amount * 30
            embed.description = \
                f"""
Ai castigat!! (x30 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)
        # Some Other Fruits v10:
        elif len(numbers) == 4 and 7 in numbers and 3 in numbers and 15 in numbers:
            result = amount * 30
            embed.description = \
                f"""
Ai castigat!! (x30 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)
        # If they have at least a long fruit:
        elif len(numbers) <= 4 and (11 in numbers or 13 in numbers or 12 in numbers):
            result = amount * 1.073
            embed.description = \
                f"""
Ai castigat!! (x1.073 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)
        # If they have at least a small fruit:
        elif len(numbers) <= 4 and (8 in numbers or 6 in numbers or 7 in numbers):
            result = amount * 1.073
            embed.description = \
                f"""
Ai castigat!! (x1.073 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)
        # If they have at least a seed fruit:
        elif len(numbers) <= 4 and (10 in numbers or 2 in numbers or 16 in numbers):
            result = amount * 1.073
            embed.description = \
                f"""
Ai castigat!! (x1.073 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)

        # If the user did not hit any winning numbers:
        else:
            embed.colour = 0xFF0000
            embed.description = f"Ai pierdut {amount} credite.."
            await msg.edit(embed=embed)

        # We update the JSON file:
        data[user] += round(result, 3)

        with open("credits.json", "w") as js:
            json.dump(data, js, indent=2)

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
        old_user = None
        if user is not None:
            try:
                old_user = self.bot.get_user(int(user[3:-1]))
                if old_user is None:
                    old_user = self.bot.get_user(int(user[2:-1]))
            except ValueError:
                return await ctx.channel.send("Sigur ai formulat bine comanda?")

        with open("credits.json", "r") as js:
            data = json.load(js)

        if old_user is None:
            embed = discord.Embed(color=0x00FF00,
                                  title=f"BALANTA: {ctx.author.name}",
                                  description=f"**{data[str(ctx.author.id)]}** credite."
                                  )
        else:
            embed = discord.Embed(color=0x0000FF,
                                  title=f"BALANTA: {old_user.name}",
                                  description=f"**{data[str(old_user.id)]}** credite.")

        return await ctx.channel.send(embed=embed)

    # The $donate command allows users to trade credits with each other.
    @commands.command(help="Doneaza o suma modica unui utilizator.",
                      description="Comanda $donate iti permite sa donezi credite unui alt utilizator.\nSINTAXA:")
    async def donate(self, ctx, user, amount):
        try:
            total = int(amount)
            old_user = self.bot.get_user(int(user[3:-1]))
            if old_user is None:
                old_user = self.bot.get_user(int(user[2:-1]))
        except ValueError:
            return await ctx.channel.send("Sigur ai formulat bine comanda?")

        # Load JSON file with credit scores:
        with open("credits.json", "r") as js:
            data = json.load(js)

        # Basic Checks for donation abuses:
        if old_user.id == ctx.author.id:
            return await ctx.channel.send("Nu poti sa iti dai bani singur.")
        if total == 0:
            return await ctx.channel.send("Nu poti sa oferi 0 credite.")
        if total < 0:
            return await ctx.channel.send("Nu poti oferi o suma negativa de credite.")
        if data[str(ctx.author.id)] < total:
            return await ctx.channel.send("Nu ai destule credite pentru a dona acea suma.")

        # Check if the receiver is in the credits.json file:
        if str(old_user.id) in data.keys():
            data[str(old_user.id)] += total
            data[str(ctx.author.id)] -= total
        else:
            return await ctx.channel.send(f"Persoana {old_user} nu exista pe aceast server.")

        with open("credits.json", "w") as js:
            json.dump(data, js, indent=2)

        embed = discord.Embed(title="DONATIE",
                              color=0xFAFAFA,
                              description=f"{ctx.author.name} a donat {total} credite catre {old_user}.")

        return await ctx.channel.send(embed=embed)

    # The $rob command allows uses to attempt to rob other users.
    @commands.command(help="Incearca sa furi credite de la cineva.",
                      description="Comanda $rob iti permite sa incerci sa furi creditele altui utilizator.\nSINTAXA:")
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def rob(self, ctx, user):
        try:
            old_user = self.bot.get_user(int(user[3:-1]))
            if old_user is None:
                old_user = self.bot.get_user(int(user[2:-1]))
        except ValueError:
            return await ctx.channel.send("Sigur ai formulat bine comanda?")

        # Load JSON file with credit scores:
        with open("credits.json", "r") as js:
            data = json.load(js)

        # Basic Checks for rob abuses:
        if old_user.id == ctx.author.id:
            return await ctx.channel.send("Nu poti sa te jefuiesti.")

        # Setup for the probabilities of stealing and not succeding:
        if str(old_user.id) in data.keys():
            probability_to_steal = random.randint(0, 100)
            probabilty_to_fail = random.randint(0, 100)
            lower_bound_of_credits = data[str(old_user.id)] // 7
            upper_bound_of_credits = data[str(old_user.id)] // 3
            amount_of_credits_stolen = random.randint(lower_bound_of_credits, upper_bound_of_credits)
        else:
            return await ctx.channel.send(f"Utilizatorul {str(old_user)[:-5]} nu exista in baza de date locala.")

        if probabilty_to_fail <= probability_to_steal:
            data[str(old_user.id)] -= amount_of_credits_stolen
            data[str(ctx.author.id)] += amount_of_credits_stolen
            embed = discord.Embed(
                title=f":currency_exchange: FURT REUSIT (+{amount_of_credits_stolen} credite) :currency_exchange: ",
                color=0xBABAFF,
                description=f"{ctx.author.name} a furat {amount_of_credits_stolen} credite de la {str(old_user)[:-5]}.")
        else:
            embed = discord.Embed(
                title=f":exclamation: FURT DEPISTAT (-{amount_of_credits_stolen * 2.5} credite) :exclamation:",
                color=0xAFAFAF,
                description=f"{ctx.author.name} a vrut sa fure {amount_of_credits_stolen} credite de la {str(old_user)[:-5]}.")
            data[str(ctx.author.id)] -= (amount_of_credits_stolen * 2.5)

        with open("credits.json", "w") as js:
            json.dump(data, js, indent=2)

        return await ctx.channel.send(embed=embed)

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
        with open("credits.json", "r") as js:
            data = json.load(js)

        top_12 = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))

        embed = discord.Embed(color=0xABBACD,
                              title="CLASAMENT CREDITE")
        iterator = 1

        # We iterate through the sorted dict:
        for key, value in top_12.items():
            if iterator == 13:
                return await ctx.channel.send(embed=embed)
            embed.add_field(name=f"Loc #{iterator}: {str(self.bot.get_user(int(key)))[:-5]}",
                            value=f"**{value}** credite",
                            inline=True)
            iterator += 1

    # The $daily command gives users a daily bonus of 150 credits.
    @commands.command(help="Scrie $daily pentru o doza de credite!",
                      description="Primeste 150 credite in fiecare zi, cand activezi aceasta comanda!")
    @commands.cooldown(1, 43200, commands.BucketType.user)
    async def daily(self, ctx):

        # Load JSON file with credit scores:
        with open("credits.json", "r") as js:
            data = json.load(js)

        # Give users 150 credits.
        if str(ctx.author.id) in data.keys():
            data[str(ctx.author.id)] += 150
        else:
            return await ctx.channel.send("A intervenit o eroare. Contacteaza-l pe @중간끝#6826")

        # Show the user a nice message:
        embed = discord.Embed(color=0x0AFFA0,
                              title=":champagne_glass: Bonus Zilnic! :champagne_glass:",
                              description=f"{ctx.author.name} a primit un bonus de 150 de credite!")

        # Save JSON file with new credit scores:
        with open("credits.json", "w") as js:
            json.dump(data, js, indent=2)

        return await ctx.channel.send(embed=embed)

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
