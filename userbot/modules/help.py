# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register
from platform import uname

plugins = CMD_HELP

# Ported by apisuserbot (Hexxa-Userbot)
# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit(f"`{args}` **Bukan Plugin Yang Valid**")
            await asyncio.sleep(200)
            await event.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t|  "
        await event.edit("๐ฅ๐๐๐ญ๐ญ๐-๐๐๐๐๐ฝ๐๐๐ฅ\n\n"
                         f"**โยป User** {DEFAULTUSER}\n**โยป Plugins :** `{len(plugins)}`\n\n"
                         "**โ Main Menu โฏ**\n"
                         f"โฐโบ| {string} โโ")
        await event.reply(
            f"**โยป Perintah Plugin** \n\n"
            f"**Contoh : Ketik** `.help afk` **Untuk Informasi Pengunaan Plugin Afk\nAtau Bisa Juga Ketik** `.helpme` **Untuk Help Button Lain-Nya** \n\n"
            f"**USERBOT TELEGRAM** ")
        await asyncio.sleep(1000)
        await event.delete()
# fixes by apis
# Jan Di Clone Help Nya , Usaha Lah Asu :)
