from platform import uname
from time import sleep
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.P(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Assalamu'alaikum...`")


@register(outgoing=True, pattern=r"^\.p(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Assalamu'alaikum...`")


@register(outgoing=True, pattern="^.Ass(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(f"**Halo bro saya {DEFAULTUSER} salam kenal š**")
    sleep(2)
    await typew.edit("`Assalamualaikum Waruhmatulahi Wabarukatuh...`")


@register(outgoing=True, pattern="^.Waa(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**iyaa bro**")
    sleep(2)
    await typew.edit("`Walaikumsalam Waruhmatulahi Wabarukatuh...`")


@register(outgoing=True, pattern="^.L(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wa'alaikumsalam...`")


@register(outgoing=True, pattern=r"^\.l(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wa'alaikumsalam...`")


CMD_HELP.update(
    {
        "salam": "**ā Plugin : **`salam`\
        \n\n  ā¢  **Perintah :** `.P` | `.p`\
        \n  ā¢  **Function :** Untuk salam ke semua orang\
        \n\n  ā¢  **Perintah :** `.Ass`\
        \n  ā¢  **Function :** Salam kenal dan salam\
        \n\n  ā¢  **Perintah :** `.Waa`\
        \n  ā¢  **Function :** Menjawab salam panjang\
        \n\n  ā¢  **Perintah :** `.L` | `.l`\
        \n  ā¢  **Function :** Untuk menjawab salam\
        \n\n\n  ā¢  **Pesan untuk salam dan menjawab salam ke semua orang , dimanapun Hexxa berada.**\nā  **Pesan dari developer Hexxa Apis , enjoy userbot:D**\
    "
    }
)
