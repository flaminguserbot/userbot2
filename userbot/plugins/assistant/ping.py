import os

from telethon import Button, events

from userbot import *
from userbot.Config import Config
from userbot.plugins import *

LEGEND_IMG = os.environ.get(
    "BOT_PING_PIC", "https://te.legra.ph/file/8b012f55fc4238151d169.jpg"
)
ms = 4
ALIVE = Config.ALIVE_NAME

MR_INVISIBLE_OFFICIAL = f"**꧁•⊹٭Ping٭⊹•꧂**\n\n   ⚜ {ms}\n   ⚜ ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『{ALIVE}』"


@tgbot.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    GOOD = [[Button.url("⚜ Invisible Legends ⚜", "https://t.me/Invisible_LegendBot")]]
    await tgbot.send_file(event.chat_id, LEGEND_IMG, caption=MR_INVISIBLE_OFFICIAL, buttons=GOOD)
