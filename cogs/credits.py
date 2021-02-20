import random
import discord
import json

from asyncio import sleep
from discord.ext import commands


class Fun(commands.Cog, name="Casino"):
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
        data[user] += result

        with open("credits.json", "w") as js:
            json.dump(data, js, indent=2)

    # Error Handler for the above command:
    @ruleta.error
    async def ruleta_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title=f":exclamation: Deja ai pariat la ruleta, mai asteapta {error.retry_after:.2f} sec :exclamation:",
                                  color=0xFF0000)
            await ctx.channel.send(embed=embed, delete_after=5)

    # The $balance command shows users their current credit score balance.
    @commands.command(help="Arata cate credite are un utilizator.",
                      description="Poti specifica, optional, un user.\nSintaxa:")
    async def balance(self, ctx, *, user=None):
        old_user = user  # Just to remove the potential assignment error.
        if user is not None:
            try:
                old_user = self.bot.get_user(int(user[3:-1]))
                user = str(user[3:-1])
            except ValueError:
                return await ctx.channel.send("Sigur ai formulat bine comanda?")

        with open("credits.json", "r") as js:
            data = json.load(js)

        if user is None:
            embed = discord.Embed(color=0x00FF00,
                                  title=f"BALANTA: {ctx.author.name}",
                                  description=f"**{data[str(ctx.author.id)]}** credite."
                                  )
        else:
            embed = discord.Embed(color=0x0000FF,
                                  title=f"BALANTA: {old_user}",
                                  description=f"**{data[str(user)]}** credite.")

        return await ctx.channel.send(embed=embed)

    # The $donate command allows users to trade credits with each other.
    @commands.command(help="Doneaza o suma modica unui utilizator.",
                      description="Comanda $donate iti permite sa donezi credite unui alt utilizator.\nSINTAXA:")
    async def donate(self, ctx, user, amount):
        try:
            total = int(amount)
            old_user = user
            user = str(user[3:-1])
        except ValueError:
            return await ctx.channel.send("Sigur ai formulat bine comanda?")

        # Load JSON file with credit scores:
        with open("credits.json", "r") as js:
            data = json.load(js)

        # Basic Checks for donation abuses:
        if int(user) == int(ctx.author.id):
            return await ctx.channel.send("Nu poti sa iti dai bani singur.")
        if total == 0:
            return await ctx.channel.send("Nu poti sa oferi 0 credite.")
        if total < 0:
            return await ctx.channel.send("Nu poti oferi o suma negativa de credite.")
        if data[str(ctx.author.id)] < total:
            return await ctx.channel.send("Nu ai destule credite pentru a dona acea suma.")

        # Check if the receiver is in the credits.json file:
        if user in data.keys():
            data[str(user)] += total
            data[str(ctx.author.id)] -= total
        else:
            return await ctx.channel.send(f"Persoana {old_user} nu exista pe aceast server.")

        with open("credits.json", "w") as js:
            json.dump(data, js, indent=2)

        embed = discord.Embed(title="DONATIE",
                              color=0xFAFAFA,
                              description=f"{ctx.author.name} a donat {total} credite catre {old_user}.")

        return await ctx.channel.send(embed=embed)

    # The $clasament command shows the top 12 users by their credit score balance.
    @commands.command(help="Vezi cei mai bogati 12 oameni de pe server.",
                      description="Vrei sa vezi top 12 cei mai bogati oameni de pe server? Scrie $clasament!\n Sintaxa:")
    async def clasament(self, ctx):
        with open("credits.json", "r") as js:
            data = json.load(js)

        top_10 = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))

        embed = discord.Embed(color=0xABBACD,
                              title="CLASAMENT CREDITE")
        iterator = 1

        # We iterate through the sorted dict:
        for key, value in top_10.items():
            if iterator == 13:
                return await ctx.channel.send(embed=embed)
            embed.add_field(name=f"Loc #{iterator}: {str(self.bot.get_user(int(key)))[:-5]}",
                            value=f"**{value}** credite",
                            inline=True)
            iterator += 1


def setup(bot):
    bot.add_cog(Fun(bot))
