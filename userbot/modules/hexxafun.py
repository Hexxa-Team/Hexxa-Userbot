# Based Plugins
# Ported For Hexxa-Userbot By PacarFerdilla/Apis
# If You Kang It Don't Delete / Warning!! Jangan Hapus Ini Anjenggg!!!
# Done!
from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.xogame(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    noob = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob)
    await tap[0].click(event.chat_id)
    await event.delete()

# Apis Gans


@register(outgoing=True, pattern=r"^\.wp(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    wwwspr = event.pattern_match.group(1)
    botusername = "@whisperBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, wwwspr)
    await tap[0].click(event.chat_id)
    await event.delete()

# Apis Gans


@register(outgoing=True, pattern=r"^\.mod(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    modr = event.pattern_match.group(1)
    botusername = "@PremiumAppBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, modr)
    await tap[0].click(event.chat_id)
    await event.delete()

# Ported For Hexxa-Userbot By Apis

CMD_HELP.update(
    {
        "fun": "**✘ Plugin :** `Fun`\
        \n\n  •  **Perintah :** `.xogame`\
        \n  •  **Function : **Mainkan game XO bersama temanmu\
        \n\n  •  **Perintah :** `.mod` <nama app>\
        \n  •  **Function : **Dapatkan applikasi mod\
        \n\n  •  **Perintah :** `.wp` <teks> <username/ID>\
        \n  •  **Function : **Berikan pesan rahasia\
    "
    }
)
