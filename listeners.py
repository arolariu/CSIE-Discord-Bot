from funcs import CasinoFunc
from funcs import GeneralFunc
from funcs import UtilsFunc
from funcs import FacultateFunc


async def casino_listener(bot, ctx):
    msg = ctx.content.lower().split()

    try:

        if msg[0] == "$ruleta":
            return await CasinoFunc(bot=bot,
                                    ctx=ctx,
                                    user=None,
                                    amount=5 if len(msg) == 1 else msg[1],
                                    context=None).ruleta_func()

        elif msg[0] == "$slots":
            return await CasinoFunc(bot=bot,
                                    ctx=ctx,
                                    user=None,
                                    amount=5 if len(msg) == 1 else msg[1],
                                    context=None).slots_func()

        elif msg[0] == "$balance":
            return await CasinoFunc(bot=bot,
                                    ctx=ctx,
                                    user=None if len(msg) == 1 else msg[1],
                                    amount=None,
                                    context=None).balance_func()

        elif msg[0] == "$donate":
            return await CasinoFunc(bot=bot,
                                    ctx=ctx,
                                    user=None if len(msg) == 1 else msg[1],
                                    amount=5 if len(msg) == 2 else msg[2],
                                    context=None).donate_func()

        elif msg[0] == "$deposit":
            return await CasinoFunc(bot=bot,
                                    ctx=ctx,
                                    user=None,
                                    amount=5 if len(msg) == 1 else msg[1],
                                    context=None).deposit_func()

        elif msg[0] == "$loan":
            return await CasinoFunc(bot=bot,
                                    ctx=ctx,
                                    user=None,
                                    amount=5 if len(msg) == 1 else msg[1],
                                    context=None).loan_func()

        elif msg[0] == "$check":
            return await CasinoFunc(bot=bot,
                                    ctx=ctx,
                                    user=None,
                                    amount=None,
                                    context=None).check_func()

        elif msg[0] == "$rob":
            return await CasinoFunc(bot=bot,
                                    ctx=ctx,
                                    user=None if len(msg) == 1 else msg[1],
                                    amount=None,
                                    context=None).rob_func()

        elif msg[0] == "$clasament":
            return await CasinoFunc(bot=bot,
                                    ctx=ctx,
                                    user=None,
                                    amount=None,
                                    context=None).clasament_func()

        elif msg[0] == "$daily":
            return await CasinoFunc(bot=bot,
                                    ctx=ctx,
                                    user=None,
                                    amount=None,
                                    context=None).daily_func()

    except IndexError:
        return


async def utils_listener(bot, ctx):
    msg = ctx.content.lower().split()
    try:

        if msg[0] == "$server":
            return await UtilsFunc(bot=bot,
                                   ctx=ctx,
                                   user=None,
                                   amount=None,
                                   context=None).server_func()

        elif msg[0] == "$ver":
            return await UtilsFunc(bot=bot,
                                   ctx=ctx,
                                   user=None,
                                   amount=None,
                                   context=None).ver_func()

        elif msg[0] == "$ping":
            return await UtilsFunc(bot=bot,
                                   ctx=ctx,
                                   user=None,
                                   amount=100 if len(msg) == 1 else msg[1],
                                   context=None).ping_func()

    except IndexError:
        return


async def general_listener(bot, ctx):
    msg = ctx.content.lower().split()

    try:

        if msg[0] == "$avatar":
            return await GeneralFunc(bot=bot,
                                     ctx=ctx,
                                     user=None if len(msg) == 1 else msg[1],
                                     amount=None,
                                     context=None).avatar_func()

        elif msg[0] == "$whois":
            return await GeneralFunc(bot=bot,
                                     ctx=ctx,
                                     user=None if len(msg) == 1 else msg[1],
                                     amount=None,
                                     context=None).whois_func()

        elif msg[0] == "$wiki":
            return await GeneralFunc(bot=bot,
                                     ctx=ctx,
                                     user=None,
                                     amount=None,
                                     context=msg[1:]).wiki_func()

        elif msg[0] == "$ref":
            return await GeneralFunc(bot=bot,
                                     ctx=ctx,
                                     user=None,
                                     amount=None,
                                     context=msg[1:]).ref_func()

    except IndexError:
        return


async def facultate_listener(bot, ctx):
    msg = ctx.content.lower().split()

    try:

        if msg[0] == "$ase":
            return await FacultateFunc(bot=bot,
                                       ctx=ctx,
                                       user=None,
                                       amount=None,
                                       context=None).ase_func()

        elif msg[0] == "$csie":
            return await FacultateFunc(bot=bot,
                                       ctx=ctx,
                                       user=None,
                                       amount=None,
                                       context=None).csie_func()

        elif msg[0] == "$faq":
            return await FacultateFunc(bot=bot,
                                       ctx=ctx,
                                       user=None,
                                       amount=None,
                                       context=None).faq_func()

        elif msg[0] == "$orar":
            return await FacultateFunc(bot=bot,
                                       ctx=ctx,
                                       user=None,
                                       amount=None,
                                       context=None).orar_func()

        elif msg[0] == "$gdrive":
            return await FacultateFunc(bot=bot,
                                       ctx=ctx,
                                       user=None,
                                       amount=None,
                                       context=None).gdrive_func()

    except IndexError:
        return
