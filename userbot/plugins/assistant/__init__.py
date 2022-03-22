# Invisible Legend XBot Assistant
from telethon import Button, custom

from userbot import ALIVE_NAME, bot

from . import *

OWNER_NAME = ALIVE_NAME
OWNER_ID = bot.uid


LEGEND_USER = bot.me.first_name
MR_INVISIBLE_OFFICIAL = bot.uid

legend_mention = f"[{LEGEND_USER}](tg://user?id={MR_INVISIBLE_OFFICIAL})"
gban_pic = "./userbot/resources/pics/gban.mp4"
main_pic = "./userbot/resources/pics/main.jpg"
core_pic = "./userbot/resources/pics/core.jpg"
chup_pic = "./userbot/resources/pics/chup.mp4"
bsdk_pic = "./userbot/resources/pics/bsdk.jpg"
bsdkwale_pic = "./userbot/resources/pics/bsdk_wale.jpg"
chutiya_pic = "./userbot/resources/pics/chutiya.jpg"
LEGENDversion = "1.0"

perf = "[ Invisible Legendẞø† ]"


DEVLIST = ["5267090352"]


async def setit(event, name, value):
    try:
        event.set(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    button = [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
    return button
