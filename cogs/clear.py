from discord_utils import *
from discord.ext import commands


# To use: $clear {amount_of_messages_to_be_deleted} in a channel.
class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Comanda clear sterge mesaje scrise din canal.")
    async def clear(self, ctx, amount):
        try:
            if ctx.author.id in power_users[1:] and int(amount) > 5:
                admin = await self.bot.fetch_user(power_users[0])
                chat_history = []
                messages = await ctx.channel.history(limit=int(amount)).flatten()
                for msg in messages:
                    chat_history.append(f"{msg.author} : {msg.content}")
                    chat_history.append("\n")
                chat_history = [msg for msg in chat_history[::-1]]
                full_history = "".join(chat_history)
                abuse = await admin.create_dm()
                await abuse.send(full_history)
                if int(amount) <= 15:
                    await ctx.channel.purge(limit=int(amount))
                else:
                    await ctx.send(f"Maximul de mesaje șterse simultan este 50. (WARNING: @{ctx.author})")
            elif ctx.author.id == power_users[0]:
                await ctx.channel.purge(limit=int(amount))
            else:
                await ctx.send("Nu aveți drepturile necesare pentru a rula această comandă. Îmi pare rău!")
        except ValueError:
            await ctx.send(
                "Parametrii tăi nu se aseamănă cu cei ceruți. Comanda trebuie să fie de genul $clear {@tu} {nr}")


def setup(bot):
    bot.add_cog(Clear(bot))
