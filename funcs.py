import json
import os
import platform
import random

from asyncio import sleep

import wikipedia
from discord.ext import commands

from discord_utils import *


# The main functions class for the casino.py file
class CasinoFunc:

    def __init__(self, bot, ctx, user, amount, context):
        self.bot = bot
        self.ctx = ctx
        self.user = user
        self.amount = amount
        self.context = context

    # async function for the $ruleta command
    async def ruleta_func(self):
        emoji_dex = \
            {":one:": 1, ":two:": 2, ":three:": 3,
             ":four:": 4, ":five:": 5, ":six:": 6,
             ":seven:": 7, ":eight:": 8, ":nine:": 9}
        try:
            amount = int(self.amount)
        except ValueError:
            return await self.ctx.channel.send("Sigur ai formulat corect comanda?")
        print("1")
        user = str(self.ctx.author.id)

        if amount <= 0:
            return await self.ctx.channel.send("Nu poti paria o suma atat de mica.")
        print("2")

        # JSON Check if the user has enough credits.
        with open("credits.json", "r") as js:
            try:
                data = json.load(js)
                if user not in data.keys():
                    return await self.ctx.channel.send("Nu poti paria momentan. Contacteaza un moderator.")
                elif user in data.keys() and data[user] < 0:
                    return await self.ctx.channel.send("Nu poti paria. Balanta ta este 0.")
                elif user in data.keys() and data[user] < amount:
                    return await self.ctx.channel.send("Nu poti paria mai mult decat ai in portofel.")
            except ValueError:  # JSONDecodeError
                return await self.ctx.channel.send("Eroare interna. Contacteaza-l pe 중간끝#6826")

        print("3")

        # We play the main game, if we have not returned yet.
        temp = "NUMERE PE RULETA\n"
        first = random.choice(list(emoji_dex.keys()))
        embed = discord.Embed(title=":slot_machine: RULETA :slot_machine:",
                              color=0x00FF00,
                              description=temp + first)
        msg = await self.ctx.channel.send(embed=embed)

        # Now we get the second number.
        await sleep(0.3)
        second = random.choice(list(emoji_dex.keys()))
        embed.description = temp + first + "--" + second
        await msg.edit(embed=embed)

        print("4")

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
            result = amount * 2.23
            embed.description = \
                f"""
    Ai castigat!! (x2.23 suma pariata)
    SUMA PARIATA: {amount}
    SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)

        # If the user hit 2 identic numbers:
        elif len(numbers) == 2 and 7 not in numbers:
            result = amount * 1.97
            embed.description = \
                f"""
    Ai castigat!! (x1.97 suma pariata)
    SUMA PARIATA: {amount}
    SUMA CASTIGATA: {result}
                """
            await msg.edit(embed=embed)

        # If the user hit a lucky number:
        elif len(numbers) == 3 and 7 in numbers:
            result = amount * 1.23
            embed.description = \
                f"""
    Ai castigat!! (x1.23 suma pariata)
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

    # async function for the $slots command
    async def slots_func(self):
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
            amount = int(self.amount)
        except ValueError:
            return await self.ctx.channel.send("Sigur ai formulat corect comanda?")
        user = str(self.ctx.author.id)

        if amount < 0:
            return await self.ctx.channel.send("Nu poti paria o suma atat de mica.")

        # JSON Check if the user has enough credits.
        with open("credits.json", "r") as js:
            try:
                data = json.load(js)
                if user not in data.keys():
                    return await self.ctx.channel.send("Nu poti paria momentan. Contacteaza un moderator.")
                elif user in data.keys() and data[user] < 0:
                    return await self.ctx.channel.send("Nu poti paria. Balanta ta este 0.")
                elif user in data.keys() and data[user] < amount:
                    return await self.ctx.channel.send("Nu poti paria mai mult decat ai in portofel.")
            except ValueError:  # JSONDecodeError
                return await self.ctx.channel.send("Eroare interna. Contacteaza-l pe 중간끝#6826")

        # We play the main game, if we have not returned yet.
        temp = "Fructe pe slots:\n"
        first = random.choice(list(emoji_dex.keys()))
        embed = discord.Embed(title=":peach: SLOTS :eggplant:",
                              color=0x00FF00,
                              description=temp + first)
        msg = await self.ctx.channel.send(embed=embed)

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
        if len(numbers) == 2 and 11 in numbers and 15 in numbers:
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
        if len(numbers) == 3 and 11 in numbers and 12 in numbers and 13 in numbers:
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
        if len(numbers) == 4 and 2 in numbers and 4 in numbers and 14 in numbers:
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

    # async function for the $balance command
    async def balance_func(self):
        old_user = None
        if self.user is not None:
            try:
                old_user = self.bot.get_user(int(self.user[3:-1]))
                if old_user is None:
                    old_user = self.bot.get_user(int(self.user[2:-1]))
            except ValueError:
                return await self.ctx.channel.send("Sigur ai formulat bine comanda?")

        with open("credits.json", "r") as js:
            data = json.load(js)

        if old_user is None:
            embed = discord.Embed(color=0x00FF00,
                                  title=f"BALANTA: {self.ctx.author.name}",
                                  description=f"**{data[str(self.ctx.author.id)]}** credite."
                                  )
        else:
            embed = discord.Embed(color=0x0000FF,
                                  title=f"BALANTA: {old_user.name}",
                                  description=f"**{data[str(old_user.id)]}** credite.")

        return await self.ctx.channel.send(embed=embed)

    # async function for the $donate command
    async def donate_func(self):
        if self.user is None:
            return await self.ctx.channel.send("Sigur ai formulat bine comanda?")
        if int(self.amount) <= 0:
            return await self.ctx.channel.send("Nu poti sa donezi o suma atat de mica.")

        try:
            total = int(self.amount)
            old_user = self.bot.get_user(int(self.user[3:-1]))
            if old_user is None:
                old_user = self.bot.get_user(int(self.user[2:-1]))
        except ValueError:
            return await self.ctx.channel.send("Sigur ai formulat bine comanda?")

        # Load JSON file with credit scores:
        with open("credits.json", "r") as js:
            data = json.load(js)

        # Basic Checks for donation abuses:
        if old_user.id == self.ctx.author.id:
            return await self.ctx.channel.send("Nu poti sa iti dai bani singur.")
        if total == 0:
            return await self.ctx.channel.send("Nu poti sa oferi 0 credite.")
        if total < 0:
            return await self.ctx.channel.send("Nu poti oferi o suma negativa de credite.")
        if data[str(self.ctx.author.id)] < total:
            return await self.ctx.channel.send("Nu ai destule credite pentru a dona acea suma.")

        # Check if the receiver is in the credits.json file:
        if str(old_user.id) in data.keys():
            data[str(old_user.id)] += total
            data[str(self.ctx.author.id)] -= total
        else:
            return await self.ctx.channel.send(f"Persoana {old_user} nu exista pe aceast server.")

        with open("credits.json", "w") as js:
            json.dump(data, js, indent=2)

        embed = discord.Embed(title="DONATIE",
                              color=0xFAFAFA,
                              description=f"{self.ctx.author.name} a donat {total} credite catre {old_user}.")

        return await self.ctx.channel.send(embed=embed)

    # async function for the $deposit command
    async def deposit_func(self):
        try:
            total = int(self.amount)
        except ValueError:
            return await self.ctx.channel.send("Suma trebuie sa fie de tip intreg.")

        # Basic Checks for deposit abuses:
        if total == 0:
            return await self.ctx.channel.send("Nu poti sa depozitezi 0 credite.")
        if total < 0:
            return await self.ctx.channel.send("Nu poti depozita o suma negativa de credite.")

        # Load the current credits JSON file:
        with open("credits.json", "r") as js:
            balance = json.load(js)

        # Check if the user has a negative balance:
        if balance[str(self.ctx.author.id)] <= total:
            return await self.ctx.channel.send("Nu poti depozita mai multe credite decat ai. :)")
        if balance[str(self.ctx.author.id)] <= 0:
            return await self.ctx.channel.send("Nu poti depozita credite daca ai o balanta negativa. :)")

        # Subtract the amount:
        balance[str(self.ctx.author.id)] -= total

        # Save the modified credits JSON file:
        with open("credits.json", "w") as js:
            json.dump(balance, js, indent=2)

        # Load the current deposits JSON file:
        with open("deposits.json", "r") as dp:
            deposit = json.load(dp)

        # Check if the user has made another deposit in the past:
        try:
            deposit[str(self.ctx.author.id)] += total
        except KeyError:
            deposit[str(self.ctx.author.id)] = total

        # Save the modified deposits JSON file:
        with open("deposits.json", "w") as js:
            json.dump(deposit, js, indent=2)

        # Notify the user of the status of the deposit:
        embed = discord.Embed(color=0xABCDEF,
                              title=":money_with_wings: DEPOZIT BANCAR :money_with_wings:",
                              description=f"{self.ctx.author.name} a facut un depozit de {total} credite.")
        return await self.ctx.channel.send(embed=embed)

    # async function for the $loan command
    async def loan_func(self):
        try:
            total = int(self.amount)
        except ValueError:
            return await self.ctx.channel.send("Sigur ai formulat comanda corect?")

        # Check if the user wants to loan a negative amount of money:
        if total <= 0:
            return await self.ctx.channel.send("Nu poti scoate o suma negativa din depozit.")

        # Open the current deposits JSON file:
        with open("deposits.json", "r") as js:
            data = json.load(js)

        # Subtract the amount required:
        if total > data[str(self.ctx.author.id)]:
            return await self.ctx.channel.send("Nu poti scoate din depozit mai mult decat ai.")
        data[str(self.ctx.author.id)] -= total

        # Save the modified deposits JSON file:
        with open("deposits.json", "w") as js:
            json.dump(data, js, indent=2)

        # Open the current credits JSON file:
        with open("credits.json", "r") as js:
            data = json.load(js)

        # Save the new balance and exit:
        data[str(self.ctx.author.id)] += total
        with open("credits.json", "w") as js:
            json.dump(data, js, indent=2)

        # Notify the user of the command status:
        embed = discord.Embed(color=0xCACACA,
                              title=":star_struck: EXTRAGERE NUMERAR :star_struck:",
                              description=f"{self.ctx.author.name} a extras {total} credite din depozitul sau.")
        return await self.ctx.channel.send(embed=embed)

    # async function for the $check command
    async def check_func(self):
        # Open the current deposits json file:
        with open("deposits.json", "r") as js:
            data = json.load(js)

        # Check to see if the user exists:
        if str(self.ctx.author.id) in data.keys():
            embed = discord.Embed(color=0xBACADA,
                                  title=":bank: VIZUALIZARE DEPOZIT :bank:",
                                  description=f"{self.ctx.author.name} : **{data[str(self.ctx.author.id)]}** credite")
            await self.ctx.message.add_reaction("<:hehe_boi:749712297051553953>")
            return await self.ctx.channel.send(embed=embed, delete_after=3)
        return await self.ctx.channel.send(f"{self.ctx.author.name}, nu ai facut un depozit momentan.")

    # async function for the $clasament command
    async def clasament_func(self):
        with open("credits.json", "r") as js:
            data = json.load(js)

        top_12 = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))

        embed = discord.Embed(color=0xABBACD,
                              title="CLASAMENT CREDITE")
        iterator = 1

        # We iterate through the sorted dict:
        for key, value in top_12.items():
            if iterator == 13:
                return await self.ctx.channel.send(embed=embed)
            embed.add_field(name=f"Loc #{iterator}: {str(self.bot.get_user(int(key)))[:-5]}",
                            value=f"**{value}** credite",
                            inline=True)
            iterator += 1

    # async function for the $rob command
    async def rob_func(self):
        if self.user is None:
            return await self.ctx.channel.send("Pe cine vrei sa furi, mai exact?")
        try:
            old_user = self.bot.get_user(int(self.user[3:-1]))
            if old_user is None:
                old_user = self.bot.get_user(int(self.user[2:-1]))
        except ValueError:
            return await self.ctx.channel.send("Sigur ai formulat bine comanda?")

        # Load JSON file with credit scores:
        with open("credits.json", "r") as js:
            data = json.load(js)

        # Basic Checks for rob abuses:
        if old_user.id == self.ctx.author.id:
            return await self.ctx.channel.send("Nu poti sa te jefuiesti.")

        # Setup for the probabilities of stealing and not succeding:
        if str(old_user.id) in data.keys():
            probability_to_steal = random.randint(0, 100)
            probabilty_to_fail = random.randint(0, 100)
            lower_bound_of_credits = data[str(old_user.id)] // 7
            upper_bound_of_credits = data[str(old_user.id)] // 3
            amount_of_credits_stolen = random.randint(lower_bound_of_credits, upper_bound_of_credits)
        else:
            return await self.ctx.channel.send(f"Utilizatorul {str(old_user)[:-5]} nu exista in baza de date locala.")

        # Check if the robbed user has a negative balance:
        if data[str(old_user.id)] < 0:
            return await self.ctx.channel.send("Nu poti fura de la un utilizator ce are datorii.")

        if probabilty_to_fail <= probability_to_steal:
            data[str(old_user.id)] -= amount_of_credits_stolen
            data[str(self.ctx.author.id)] += amount_of_credits_stolen
            embed = discord.Embed(
                title=f":currency_exchange: FURT REUSIT (+{amount_of_credits_stolen} credite) :currency_exchange: ",
                color=0xBABAFF,
                description=f"{self.ctx.author.name} a furat {amount_of_credits_stolen} credite de la {str(old_user)[:-5]}.")
        else:
            embed = discord.Embed(
                title=f":exclamation: FURT DEPISTAT (-{amount_of_credits_stolen * 1.5} credite) :exclamation:",
                color=0xAFAFAF,
                description=f"{self.ctx.author.name} a vrut sa fure {amount_of_credits_stolen} credite de la {str(old_user)[:-5]}.")
            data[str(self.ctx.author.id)] -= (amount_of_credits_stolen * 1.5)

        with open("credits.json", "w") as js:
            json.dump(data, js, indent=2)

        return await self.ctx.channel.send(embed=embed)

    # async function for the $daily command
    async def daily_func(self):
        # Load JSON file with credit scores:
        with open("credits.json", "r") as js:
            data = json.load(js)

        # Give users 150 credits.
        if str(self.ctx.author.id) in data.keys():
            data[str(self.ctx.author.id)] += 350
        else:
            return await self.ctx.channel.send("A intervenit o eroare. Contacteaza-l pe @중간끝#6826")

        # Show the user a nice message:
        embed = discord.Embed(color=0x0AFFA0,
                              title=":champagne_glass: Bonus Zilnic! :champagne_glass:",
                              description=f"{self.ctx.author.name} a primit un bonus de 350 de credite!")

        # Save JSON file with new credit scores:
        with open("credits.json", "w") as js:
            json.dump(data, js, indent=2)

        return await self.ctx.channel.send(embed=embed)


# The main functions class for the general.py file
class GeneralFunc:

    def __init__(self, bot, ctx, user, amount, context):
        self.bot = bot
        self.ctx = ctx
        self.user = user
        self.amount = amount
        self.context = context

    # async function for the $avatar command
    async def avatar_func(self):
        if self.user is not None:
            old_user = self.bot.get_user(int(self.user[3:-1]))
            link = old_user.avatar_url
            return await self.ctx.channel.send(link)
        else:
            return await self.ctx.channel.send("Ai uitat sa specifici un utilizator.")

    # async function for the $whois command
    async def whois_func(self):
        if self.user is not None:
            converter = discord.ext.commands.MemberConverter()
            target_member = await converter.convert(ctx=self.ctx, argument="".join(self.user))
            old_user = target_member
            whois = discord.Embed(colour=0xff0000)
            whois.set_author(name=f" whois performed ~ {old_user}", icon_url=old_user.avatar_url)
            whois.set_thumbnail(url=old_user.avatar_url)
            whois.add_field(name="Nume de utilizator: ", value=old_user.name, inline=True)
            whois.add_field(name="User ID: ", value=old_user.id, inline=True)
            whois.add_field(name="Poreclă: ", value=old_user.nick, inline=False)
            whois.add_field(name="Activitate: ", value=old_user.activity, inline=True)
            whois.add_field(name="Status: ", value=old_user.status, inline=True)
            whois.add_field(name="Conectat la voce: ", value="DA" if old_user.voice is True else "NU", inline=False)
            whois.add_field(name="S-a alăturat pe server în data de: ",
                            value=old_user.joined_at.strftime("%A, %d %B %Y, %H:%M"), inline=False)
            whois.add_field(name="S-a alăturat pe discord în data de: ",
                            value=old_user.created_at.strftime("%A, %d %B %Y, %H:%M"), inline=False)
            whois.add_field(name="Cel mai mare rol: ", value=old_user.top_role.mention, inline=False)
            whois.set_footer(
                text=f'whois rulat de @{self.ctx.author}\nWHOIS tool creat de către 중간끝#6826.')
            return await self.ctx.channel.send(embed=whois)
        else:
            return await self.ctx.channel.send("Ai uitat sa specifici un utilizator.")

    # async function for the $wiki command
    async def wiki_func(self):
        total = " ".join(self.context)
        images = []
        wikipedia.set_lang("ro")
        ref = wikipedia.suggest(total)
        if ref is None:
            try:
                page = wikipedia.page(title=total)
                summary = wikipedia.summary(total, chars=2048)
                embed = discord.Embed(color=0xFABECA,
                                      title=total.title(),
                                      description=summary)

                # Image Attachment:
                if len(page.images) > 0:
                    for element in page.images:
                        if str(element)[-3:] == "jpg":
                            images.append(element)
                    for element in page.images:
                        if str(element)[-3:] == "png":
                            images.append(element)
                    if len(images) > 0:
                        embed.set_image(url=images[0])
                    elif len(page.images) > 2:
                        embed.set_image(url=page.images[2])

                # Reference Attachment:
                if len(page.references) > 0:
                    embed.set_footer(
                        text=f"Vezi si: \n{page.references[0]}\n{page.references[len(page.references) // 2]}\n{page.references[-1]}")

                return await self.ctx.channel.send(embed=embed)
            except wikipedia.DisambiguationError:
                return await self.ctx.channel.send("Nu inteleg la ce te referi...")
            except wikipedia.PageError:
                return await self.ctx.channel.send("Eroare contactare API Wikipedia. (API Timeout.)")

        else:
            msg = await self.ctx.channel.send(f"Te referi cumva la:\n'{ref}'?")
            await msg.add_reaction("✔")
            await msg.add_reaction("❌")
            async with self.ctx.typing():
                reaction, user = await self.bot.wait_for("reaction_add")
                if str(reaction) == "✔":
                    try:
                        page = wikipedia.page(title=ref)
                        summary = wikipedia.summary(ref, chars=2048, auto_suggest=True)
                        embed = discord.Embed(color=0xFABECA,
                                              title=str(ref).title(),
                                              description=summary)

                        # Image Attachment:
                        if len(page.images) > 0:
                            for element in page.images:
                                if str(element)[-3:] == "jpg":
                                    images.append(element)
                            for element in page.images:
                                if str(element)[-3:] == "png":
                                    images.append(element)
                        if len(images) > 0:
                            embed.set_image(url=images[0])
                        elif len(page.images) > 2:
                            embed.set_image(url=page.images[2])

                        # Reference Attachment:
                        if len(page.references) > 0:
                            embed.set_footer(
                                text=f"Vezi si: \n{page.references[0]}\n{page.references[len(page.references) // 2]}\n{page.references[-1]}")

                        return await self.ctx.channel.send(embed=embed)
                    except wikipedia.PageError:
                        return await self.ctx.channel.send("Eroare contactare API Wikipedia. (API Timeout.)")
                    except wikipedia.DisambiguationError:
                        return await self.ctx.channel.send("Eroare contactare API Wikipedia. (Suggestion not found.)")
                else:
                    return await self.ctx.channel.send("Te rog sa particularizezi cautarea mai mult atunci.")

    # async function for the $ref command
    async def ref_func(self):
        total = " ".join(self.context)
        wikipedia.set_lang("en")
        ref = wikipedia.suggest(total)
        ref_list = ""
        if ref is None:
            try:
                page = wikipedia.page(title=total)
                if len(page.references) > 0:
                    for item in page.references:
                        if len(ref_list) < 2000:
                            ref_list += item
                            ref_list += "\n"
                        else:
                            break
                else:
                    ref_list = "Nu am gasit materiale pentru subiectul specificat..."

                embed = discord.Embed(color=0xFEDCBA,
                                      title=f"Materiale despre {total.title()}",
                                      description=ref_list[:2048])
                return await self.ctx.channel.send(embed=embed)

            except wikipedia.PageError:
                return await self.ctx.channel.send("Eroare contactare API Wikipedia. (API Timeout.)")

            except wikipedia.DisambiguationError:
                return await self.ctx.channel.send("Eroare contactare API Wikipedia. (Suggestion not found.)")
        else:
            try:
                msg = await self.ctx.channel.send(f"Te referi cumva la:\n'{ref}'?")
                await msg.add_reaction("✔")
                await msg.add_reaction("❌")
                async with self.ctx.typing():
                    reaction, user = await self.bot.wait_for("reaction_add")
                    if str(reaction) == "✔":
                        page = wikipedia.page(title=ref)
                        if len(page.references) > 0:
                            for item in page.references:
                                if len(ref_list) < 2000:
                                    ref_list += item
                                    ref_list += "\n"
                                else:
                                    break
                        else:
                            ref_list = "Nu am gasit materiale pentru subiectul specificat..."

                        embed = discord.Embed(color=0xFEDCBA,
                                              title=f"Materiale despre {str(ref).title()}",
                                              description=ref_list[:2048])
                        return await self.ctx.channel.send(embed=embed)
                    else:
                        return await self.ctx.channel.send("Te rog sa particularizezi mai mult cautarea atunci.")

            except wikipedia.PageError:
                return await self.ctx.channel.send("Eroare contactare API Wikipedia. (API Timeout.)")

            except wikipedia.DisambiguationError:
                return await self.ctx.channel.send("Eroare contactare API Wikipedia. (Suggestion not found.)")


# The main functions class for the utils.py file
class UtilsFunc:

    def __init__(self, bot, ctx, user, amount, context):
        self.bot = bot
        self.ctx = ctx
        self.user = user
        self.amount = amount
        self.context = context

    # async function for the $server command
    async def server_func(self):
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
        return await self.ctx.send(embed=result)

    # async function for the $ver command
    async def ver_func(self):
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
    **CPU architecture:** {platform.machine()}
    **CPU type:** {platform.processor()}
    **CPU cores:** {os.cpu_count()} cores
            """
        about_info_2 = \
            f"""
    중간끝 ( B O T ) este momentan la versiunea **{VERSION_NUMBER}** (Ultima actualizare: **{VERSION_DATE}**)
    
    **În această versiune:**
        ```
    {VERSION_DATA}
        ```
    """
        embed.add_field(name="Bot Status:", value=about_info_1, inline=False)
        embed.add_field(name="Bot Description:", value=about_info_2, inline=False)
        embed.set_image(url=LOGO_GIF)
        return await self.ctx.send(embed=embed)

    # async function for the $ping command
    async def ping_func(self):
        try:
            total = int(self.amount)
        except ValueError:
            return await self.ctx.channel.send("Sigur ai formulat corect comanda?")

        # Check if user wants more than 500 tests:
        if int(self.amount) > 500:
            total = 100

        async with self.ctx.typing():
            latency_list = []
            for _ in range(total):
                latency = self.bot.latency
                latency_list.append(latency)
            latency_average = sum(latency_list) / total

            embed = discord.Embed(color=0xBBFFAA,
                                  title=f"PING BOT (din {total} teste)",
                                  description=f"PING: **{round(latency_average * 1000, 2)}ms**")
        return await self.ctx.channel.send(embed=embed)


# The main functions class for the facultate.py file
class FacultateFunc:

    def __init__(self, bot, ctx, user, amount, context):
        self.bot = bot
        self.ctx = ctx
        self.user = user
        self.amount = amount
        self.context = context

    # async function for the $ase command
    async def ase_func(self):
        description = \
            """
    Rector ASE: *** Nicolae Istudor ***
    > Harta clădirilor din ASE: <http://student.ase.ro/harta-cladirilor/>
    > Codificarea sălilor: <http://student.ase.ro/codificarea-salilor/>
    > Informații despre facultăți: <https://www.ase.ro/?page=facultati>
    > Cazare & Cantină: <http://social.ase.ro/>        
            """

        title = ":bank: ASE INFO :bank: "

        embed = discord.Embed(color=0xACCAFF,
                              title=title,
                              description=description)

        return await self.ctx.channel.send(embed=embed)

    # async function for the $csie command
    async def csie_func(self):
        description = \
            """
    Decan CSIE: *** Marian Dârdală ***
    > Curriculum secții: <http://www.csie.ase.ro/programe-licenta>
    > Orar facultate (SiSC): <https://orar.sisc.ro/>
    > Contact secretariat (online): <http://www.csie.ase.ro/secretariat>            
            """

        title = ":bank: CSIE INFO :bank:"

        embed = discord.Embed(color=0xACCAFF,
                              title=title,
                              description=description)

        return await self.ctx.channel.send(embed=embed)

    # async function for the $faq command
    async def faq_func(self):
        title = ":bank: Cele mai frecvente intrebari, alaturi de raspunsuri! :bank:"

        embed = discord.Embed(color=0xACCAFF,
                              title=title,
                              description="Iata cele mai frecvente intrebari ale noilor studenti din CSIE:")

        for item in range(0, len(faq_list), 2):
            is_inline = True if (item + 1) % 3 != 2 else False
            embed.add_field(name=faq_list[item], value=faq_list[item + 1], inline=is_inline)

        return await self.ctx.channel.send(embed=embed)

    # async function for the $orar command
    async def orar_func(self):
        description = \
            """
    Program secretariat (sala 2011): 
        >> Lu-Ma 11:30-14:00 și 16:00-18:00
        >> Mi-Jo 11:30-14:00 iar Vineri OFF.
                """

        title = ":bank: ORAR SECRETARIAT :bank:"

        embed = discord.Embed(color=0xACCAFF,
                              title=title,
                              description=description)

        return await self.ctx.channel.send(embed=embed)

    # async function for the $gdrive command
    async def gdrive_func(self):
        description = "TBA"

        title = ":books: Materiale GDrive :books:"

        embed = discord.Embed(color=0xACCAFF,
                              title=title,
                              description=description)

        return await self.ctx.channel.send(embed=embed)


# async function for the $print command
async def print_func(ctx, *args):
    if ctx.author.id in power_users:
        result = " ".join([i for i in args])
        return await ctx.channel.send(result)
    else:
        return await ctx.channel.send("Nu aveti permisiunile necesare.")
