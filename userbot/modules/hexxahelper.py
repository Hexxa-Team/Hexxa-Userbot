""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.khelp$")
async def usit(e):
    await e.edit(
        f"      ╔════════════╗\n     **__🔥BANTUAN🔥__**     \n╚════════════╝ \n"
        f"**Hai {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "═⎆ developer  : [Kyy](t.me/sokapgblg) \n"
        "═⎆ Repository : [Hexxa-Userbot](https://github.com/Hexxa-Team/Hexxa-Userbot) \n"
        "═⎆ Telegram   : [Telegram Kyy](https://t.me/sokapgblg) \n"
        "═⎆ Grup Support : [Hexxa Userbot Support](https://t.me/HexxaUserbotSupport)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"      ╔════════════╗\n  **__🔥DAFTAR VARS🔥__**     \n╚════════════╝ \n"
        f"**Disini Daftar Vars Dari Hexxa-Userbot** {DEFAULTUSER} :\n"
        "═⎆ Daftar Vars : [DAFTAR VARS](https://raw.githubusercontent.com/apisuserbot/Hexxa-Userbot/Hexxa-Userbot/varshelper.txt)")


CMD_HELP.update(
    {
        "helper": "**✘ Plugin :** `Helper`\
        \n\n  •  **Perintah :** `.khelp`\
        \n  •  **Function : **Bantuan Untuk Hexxa-Userbot🔥\
        \n\n  •  **Perintah :** `.vars`\
        \n  •  **Function : **Melihat Daftar Vars\
    "
    }
)
