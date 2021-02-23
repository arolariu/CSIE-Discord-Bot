import discord
import wikipedia
from discord.ext import commands


# General Commands Class
class General(commands.Cog, name="================================================\nGenerale"):
    def __init__(self, bot):
        self.bot = bot

    # The command $avatar {user} shows the user's current avatar.
    @commands.command(help="Vezi avatarul unui utilizator.",
                      description="Un avatar tare? Foloseste $avatar {member_tag} pentru a il vedea mai bine!\nSintaxa:")
    async def avatar(self, ctx, *, user=None):
        if user is not None:
            old_user = self.bot.get_user(int(user[3:-1]))
            link = old_user.avatar_url
            return await ctx.channel.send(link)
        else:
            return await ctx.channel.send("Ai uitat sa specifici un utilizator.")

    # The command $whois {user} provides detailed information about a user.
    @commands.command(help="Vezi detalii despre un anumit utilizator.",
                      description="Vrei sa afli mai multe detalii despre un user? Comanda $whois {member_tag} te rezolva!")
    async def whois(self, ctx, *, user=None):
        if user is not None:
            converter = commands.MemberConverter()
            target_member = await converter.convert(ctx=ctx, argument="".join(user))
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
                text=f'whois rulat de @{ctx.author}\nWHOIS tool creat de către 중간끝#6826.')
            return await ctx.channel.send(embed=whois)
        else:
            return await ctx.channel.send("Ai uitat sa specifici un utilizator.")

    # The command $wiki {context} provides detailed information about a specified context.
    @commands.command(help="Cauta pe Wikipedia despre ceva!",
                      description="Comanda $wiki cauta pe wikipedia despre contextul specificat.\nSINTAXA:")
    async def wiki(self, ctx, *context):
        total = " ".join(context)
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
                    embed.set_footer(text=f"Vezi si: \n{page.references[0]}\n{page.references[len(page.references) // 2]}\n{page.references[-1]}")

                return await ctx.channel.send(embed=embed)
            except wikipedia.DisambiguationError:
                return await ctx.channel.send("Nu inteleg la ce te referi...")
            except wikipedia.PageError:
                return await ctx.channel.send("Eroare contactare API Wikipedia. (API Timeout.)")

        else:
            msg = await ctx.channel.send(f"Te referi cumva la:\n'{ref}'?")
            await msg.add_reaction("✔")
            await msg.add_reaction("❌")
            async with ctx.typing():
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
                            embed.set_footer(text=f"Vezi si: \n{page.references[0]}\n{page.references[len(page.references) // 2]}\n{page.references[-1]}")

                        return await ctx.channel.send(embed=embed)
                    except wikipedia.PageError:
                        return await ctx.channel.send("Eroare contactare API Wikipedia. (API Timeout.)")
                    except wikipedia.DisambiguationError:
                        return await ctx.channel.send("Eroare contactare API Wikipedia. (Suggestion not found.)")
                else:
                    return await ctx.channel.send("Te rog sa particularizezi cautarea mai mult atunci.")

    # The command $ref {context} provides references to the specified context.
    @commands.command(help="Vezi referinte pentru un subiect.",
                      description="Comanda $ref arata referinte, gasite de pe wikipedia, pentru un context.\nSINTAXA:")
    async def ref(self, ctx, *context):
        total = " ".join(context)
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
                return await ctx.channel.send(embed=embed)

            except wikipedia.PageError:
                return await ctx.channel.send("Eroare contactare API Wikipedia. (API Timeout.)")

            except wikipedia.DisambiguationError:
                return await ctx.channel.send("Eroare contactare API Wikipedia. (Suggestion not found.)")
        else:
            try:
                msg = await ctx.channel.send(f"Te referi cumva la:\n'{ref}'?")
                await msg.add_reaction("✔")
                await msg.add_reaction("❌")
                async with ctx.typing():
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
                        return await ctx.channel.send(embed=embed)
                    else:
                        return await ctx.channel.send("Te rog sa particularizezi mai mult cautarea atunci.")

            except wikipedia.PageError:
                return await ctx.channel.send("Eroare contactare API Wikipedia. (API Timeout.)")

            except wikipedia.DisambiguationError:
                return await ctx.channel.send("Eroare contactare API Wikipedia. (Suggestion not found.)")


def setup(bot):
    bot.add_cog(General(bot))
