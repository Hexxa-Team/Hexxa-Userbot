from time import sleep
from userbot.events import register
from userbot import ALIVE_NAME, UMUR, WEATHER_DEFCITY


@register(outgoing=True, pattern='^.saya(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(f"`Hai Perkenalkan Namaku {ALIVE_NAME}`")
    sleep(3)
    await typew.edit(f"`Umurku {UMUR}`")
    sleep(1)
    await typew.edit(f"`Tinggal Di {WEATHER_DEFCITY}, Salam Kenal :)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(1)
    await typew.edit("`I LOVE YOU 💞`")
    sleep(1)
    await typew.edit("`I LOVE YOU SO MUCH 🥰`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
    sleep(1)
    await typew.edit("`Hahaha`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.aku(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Aku Userbot`")
    sleep(3)
    await typew.edit("`Jangan Main Main`")
    sleep(2)
    await typew.edit("`Aku Gban Nanti Nangesss Lu`")
# Create by myself @localheart
