import random
import discord
import json

from asyncio import sleep
from discord.ext import commands


# To use: $ruleta {credits_amount} in a text channel.
class Ruleta(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Pentru a putea folosi comanda ruleta, ai nevoie de o balanta de credite pozitiva!")
    async def ruleta(self, ctx, amount):
        emoji_dex = \
            {":one:": 1, ":two:": 2, ":three:": 3,
             ":four:": 4, ":five:": 5, ":six:": 6,
             ":seven:": 7, ":eight:": 8, ":nine:": 9}
        amount = int(amount)
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
            except Exception:
                return await ctx.channel.send("Eroare interna. Contacteaza-l pe 중간끝#6826")

        # We play the main game, if we have not returned yet.
        temp = "Numere pe ruleta:\n"
        first = random.choice(list(emoji_dex.keys()))
        embed = discord.Embed(title="RULETA",
                              color=0x00FF00,
                              description=temp + first)
        msg = await ctx.channel.send(embed=embed)

        # Now we get the second number.
        await sleep(0.7)
        second = random.choice(list(emoji_dex.keys()))
        embed.description = temp + first + "--" + second
        await msg.edit(embed=embed)

        # Now we get the third and final number.
        await sleep(0.7)
        third = random.choice(list(emoji_dex.keys()))
        embed.description = temp + first + "--" + second + "--" + third
        await msg.edit(embed=embed)

        # We do some setup for the final result:
        await sleep(2)
        numbers = (emoji_dex[first], emoji_dex[second], emoji_dex[third])
        numbers = set(numbers)
        result = -amount  # We initialize result with - amount for the else clause

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
            result = 1.3
            embed.description = \
                f"""
Ai castigat!! (x1.3 suma pariata)
SUMA PARIATA: {amount}
SUMA CASTIGATA: {amount * 1.3}
                """
            await msg.edit(embed=embed)

        # If the user did not hit any winning numbers:
        else:
            embed.color = 0xFF0000
            embed.description = f"Ai pierdut {amount} credite.."
            await msg.edit(embed=embed)

        # We update the JSON file:
        data[user] += result
        with open("credits.json", "w") as js:
            json.dump(data, js, indent=2)


def setup(bot):
    bot.add_cog(Ruleta(bot))
