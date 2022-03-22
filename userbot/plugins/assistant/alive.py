from telethon import events

from userbot import *

from . import *

PM_IMG = "https://te.legra.ph/file/8b012f55fc4238151d169.jpg"
pm_caption = f"⚜『Beta Baap』Is Ôñĺîne⚜ \n\n"
pm_caption += f"Ôwñêř ~ 『{legend_mention}』\n"
pm_caption += f"**╭───────────**\n"
pm_caption += f"┣Ťêlethon ~ `9.15.10` \n"
pm_caption += f"┣『Invisible LegendBot』~ `{LEGENDversion}` \n"
pm_caption += f"┣Çhâññel ~ [Channel](https://t.me/Official_Invisible_LegendBot)\n"
pm_caption += f"┣**License** ~ [License v3.0](github.com/MR-INVISIBLEBOY/INVISIBLEUSERBOT/blob/master/LICENSE)\n"
pm_caption += f"┣Mode ~ By [『LegendInvisibleBoy』 ](https://t.me/Invisible_LegendBot)\n"
pm_caption += f"┣Assistant ~ By [『InvisibleBoy』 ](https://t.me/MR_INVISIBLE_OFFICIAL)\n"
pm_caption += f"┣Linux ~ By  [『Legend X Pro』 ](https://t.me/LegendHacker_IIN)\n"
pm_caption += f"╰────────────\n"
pm_caption += f"       »»» [『InvisibleBot』](https://t.me/Invisible_LegendBot) «««"


@tgbot.on(events.NewMessage(pattern="^/alive"))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
