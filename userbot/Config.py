import os

ENV = bool(os.environ.get("ENV", False))
if ENV:
    import os

    class Config(object):
        OWNER_ID = int(os.environ.get("OWNER_ID") or 0)
        NO_OF_COLUMNS = int(os.environ.get("NO_OF_COLUMNS", 2))
        BL_CHAT = os.environ.get("BL_CHAT", "-696535691")
        G_BAN_LOGGER_GROUP = int(os.environ.get("G_BAN_LOGGER_GROUP",  -696535691))
        FBAN_LOGGER_GROUP = os.environ.get("FBAN_LOGGER_GROUP", None)
        if FBAN_LOGGER_GROUP:
            FBAN_LOGGER_GROUP = int(FBAN_LOGGER_GROUP)
        HANDLER = os.environ.get("HANDLER", None) or "."
        # custom animation to kang plugin
        CUSTOM_STICKER_PACK_NAME = os.environ.get("CUSTOM_STICKER_PACK_NAME", None)
        # specify list of users allowed to use bot
        # WARNING: be careful who you grant access to your bot.
        # malicious users could do ".exec rm -rf /*"
        SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
        # VeryStream only supports video formats
        VERY_STREAM_LOGIN = os.environ.get("VERY_STREAM_LOGIN", None)
        VERY_STREAM_KEY = os.environ.get("VERY_STREAM_KEY", None)
        GROUP_REG_SED_EX_BOT_S = os.environ.get(
            "GROUP_REG_SED_EX_BOT_S", r"(regex|moku|BananaButler_|rgx|l4mR)bot"
        )
        TEMP_DIR = os.environ.get("TEMP_DIR", None)
        CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
        watermark_path = os.environ.get("watermark_path", None)
        # Google Chrome Stuff
        CHROME_DRIVER = os.environ.get(
            "CHROME_DRIVER", "/app/.chromedriver/bin/chromedriver"
        )
        GOOGLE_CHROME_BIN = os.environ.get(
            "GOOGLE_CHROME_BIN", "/app/.apt/usr/bin/google-chrome"
        )
        # Google Drive ()
        G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
        G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
        GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
        AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
        if AUTH_TOKEN_DATA != None:
            os.makedirs(TMP_DOWNLOAD_DIRECTORY)
            t_file = open(TMP_DOWNLOAD_DIRECTORY + "auth_token.txt", "w")
            t_file.write(AUTH_TOKEN_DATA)
            t_file.close()

        YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
        GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
        # MongoDB
        MONGO_URI = os.environ.get("MONGO_URI", None)
        # alive

        HELP_EMOJI1 = os.environ.get("HELP_EMOJI1", None) or "✥"
        HELP_EMOJI2 = os.environ.get("HELP_EMOJI2", None) or "✥"
        ALIVE_EMOJI = os.environ.get("ALIVE_EMOJI", None) or "✥"
        ALIVE_PIC = (
            os.environ.get("ALIVE_PIC", None)
            or "https://te.legra.ph/file/a8464b00a8489dbac3b8e.jpg"
        )
        PM_PIC = (
            os.environ.get("PM_PIC", None)
            or "https://te.legra.ph/file/655a5de5e0232d5d8e62b.jpg"
        )
        AWAKE_PIC = (
            os.environ.get("AWAKE_PIC", None)
            or "https://te.legra.ph/file/a8464b00a8489dbac3b8e.jpg"
        )
        HELP_PIC = (
            os.environ.get("HELP_PIC", None)
            or "https://te.legra.ph/file/8b012f55fc4238151d169.jpg"
        )
        PING_PIC = (
            os.environ.get("PING_PIC", None)
            or "https://te.legra.ph/file/996746ae9b0fa48bcbec3.jpg"
        )
        ALIVE_MSG = os.environ.get("ALIVE_MSG", None) or "Invisibleẞøt Is Online"
        CYBER_ID_PROTECTED = os.environ.get("CYBER_ID_PROTECTED", None)
        PM_MSG = os.environ.get("PM_MSG", None)
        INSTANT_BLOCK = os.environ.get("INSTANT_BLOCK", "OFF")
        YOUR_GROUP = os.environ.get("YOUR_GROUP", "@flamingchat")
        YOUR_CHANNEL = os.environ.get("YOUR_CHANNEL", "@flamingsupport")
        BOT_PIC = os.environ.get("ALIVE_PIC", None)
        # auto bio
        BIO_MSG = os.environ.get("ALIVE_MSG", None)
        DEEP_AI = os.environ.get("DEEP_AI", "87d64af9-3126-41e8-8765-726bdd134ec8")
        # Lydia API
        LYDIA_API = os.environ.get("LYDIA_API", None)
        PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL", None))
        UPSTREAM_REPO = os.environ.get(
            "UPSTREAM_REPO", "https://github.com/FLAMING-AI/userbot2"
        )
        APP_ID = os.environ.get("APP_ID", "14863874")
        API_HASH = os.environ.get("API_HASH", "3b5d73f27080334a1d730087b552519b")
        INVISIBLE_STRING = os.environ.get("INVISIBLE_STRING", "1BVtsOI0Bu1KzE2IKLu0WlntawbUG65qi6F5nRE0rTuqn9xb4INOrin5s70bkIrhXxam5wcn59g-LmI7l4hmqc49UQCwkzvAwe9hs_WweFhxP6oHZFXPXr037dQOceNVJ9t36P94lEPueZpYKt_6XfjrRUOCi0i8zS52I4JoLYgVe9gEvYtOQ9C3YFnHUzOwL1vBQNpMKnIBOzFAunUS3HwmfnzdwFMr4ZOqwARvlabuGMK7a1GlihAxWFldGcRxZyOY5qjZuJH4GzPQ3JtbFgvGUZg4P9T2QOHkTRTWyInAcqjfzV8TsOMe15TWjzEDcX2D0YGzPK3aAERvugmlQIqna1IXbe34=")
        LEGEND_LX = os.environ.get("LEGEND_LX", None)
        EXTRA_PLUGIN = os.environ.get("EXTRA_PLUGIN", "ON")
        ASSISTANT = os.environ.get("ASSISTANT", "ON")
        ABUSE = os.environ.get("ABUSE", 'None')
        LOGGER_ID = os.environ.get("LOGGER_ID", "-1001722877881")
        ALIVE_NAME = os.environ.get("ALIVE_NAME", "FLAMING BOY")
        BOY_OR_GIRL = os.environ.get("BOY_OR_GIRL", "BOY")
        BOT_TOKEN = os.environ.get("BOT_TOKEN", "5449951995:AAH0n-EZUc6H0iJJcSkxCs4lYQgWy17QcSU")
        BOT_USERNAME = os.environ.get("BOT_USERNAME", "@flaming_AI_bot")
        FORCE_SUB = os.environ.get("FORCE_SUB", None)
        FORCE_CHANNEL_UN = os.environ.get("FORCE_CHANNEL_UN", None)
        LOGGER_ID = int(os.environ.get("LOGGER_ID", "-1001722877881"))
        HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "c3870729-30d9-4e03-81b6-119e7bff6757")
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", "flamingassistant123")
        BOT_TOKEN = os.environ.get("BOT_TOKEN", "5449951995:AAH0n-EZUc6H0iJJcSkxCs4lYQgWy17QcSU")
        # can get from https://coffeehouse.intellivoid.net/
        RANDOM_STUFF_API_KEY = os.environ.get("RANDOM_STUFF_API_KEY", None)
        # github vars
        BOT_USERNAME = os.environ.get("BOT_USERNAME", "@flaming_AI_bot")
        FORCE_CHANNEL_ID = int(os.environ.get("FORCE_CHANNEL_ID", False))
        PM_DATA = os.environ.get("PM_DATA", "ON")
        GOOGLE_SEARCH_COUNT_LIMIT = int(os.environ.get("GOOGLE_SEARCH_COUNT_LIMIT", 9))
        # This is required for the speech to text module. Get your USERNAME from https://console.bluemix.net/docs/services/speech-to-text/getting-started.html
        IBM_WATSON_CRED_URL = os.environ.get("IBM_WATSON_CRED_URL", None)
        IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
        # This is required for the hash to torrent file functionality to work.
        HASH_TO_TORRENT_API = os.environ.get(
            "HASH_TO_TORRENT_API", "https://example.com/torrent/{}"
        )
        LOGGER = True
        LOCATION = os.environ.get("LOCATION", None)
        OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
        OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
        SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get(
            "SCREEN_SHOT_LAYER_ACCESS_KEY", None
        )
        # Send .get_id in any group to fill this value.
        SUDO_HANDLER = os.environ.get("SUDO_HANDLER", r"\,")
        TMP_DOWNLOAD_DIRECTORY = os.environ.get(
            "TMP_DOWNLOAD_DIRECTORY", "./userbot/DOWNLOADS/"
        )
        TELEGRAPH_SHORT_NAME = (
            os.environ.get("TELEGRAPH_SHORT_NAME", None) or "INVISIBLE_LEGENDBOT"
        )
        TG_GLOBAL_ALBUM_LIMIT = int(os.environ.get("TG_GLOBAL_ALBUM_LIMIT", 9))
        # MIRROR ACE API KEY AND TOKEN
        MIRROR_ACE_API_KEY = os.environ.get("MIRROR_ACE_API_KEY", None)
        MIRROR_ACE_API_TOKEN = os.environ.get("MIRROR_ACE_API_KEY", None)
        # Telegram BOT Token from @Bot
        # spootifie
        SPOTIFY_USERNAME = os.environ.get("SPOTIFY_USERNAME", None)
        SPOTIFY_PASS = os.environ.get("SPOTIFY_PASS", None)
        SPOTIFY_BIO_PREFIX = os.environ.get("SPOTIFY_BIO_PREFIX", None)
        # log
        DUAL_LOG = os.environ.get("DUAL_LOG", None)
        # DO NOT EDIT BELOW THIS LINE IF YOU DO NOT KNOW WHAT YOU ARE DOING
        # TG API limit. A message can have maximum 4096 characters!
        MAX_MESSAGE_SIZE_LIMIT = 4096
        # set blacklist_chats where you do not want userbot's features
        UB_BLACK_LIST_CHAT = set(
            int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split()
        )
        # Get your own API key from https://www.remove.bg/ or
        # feel free to use http://telegram.dog/Remove_BGBot
        REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
        # Set to True if you want to block users that are spamming your PMs.
        SLAP_USERNAME = os.environ.get("SLAP_USERNAME", None)
        GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
        GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
        NO_P_M_SPAM = bool(os.environ.get("NO_P_M_SPAM", True))
        # define "spam" in PMs
        NO_SONGS = bool(os.environ.get("NO_SONGS", False))
        MAX_FLOOD_IN_PM = int(os.environ.get("MAX_FLOOD_IN_PM", 7))
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
        HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
        # send .get_id in any channel to forward all your NEW PMs to this group
        # send .get_id in your private channel to forward all your Private messages
        DB_URI = os.environ.get("DATABASE_URL", None)
        # number of rows of buttons to be displayed in .legend command
        BUTTONS_IN_HELP = int(os.environ.get("NO_OF_BUTTONS", 7))
        NO_OF_BUTTONS = int(os.environ.get("NO_OF_BUTTONS", 7))
        BOT_HANDLER = os.environ.get("BOT_HANDLER", "^/")
        # open load
        OPEN_LOAD_LOGIN = os.environ.get("OPEN_LOAD_LOGIN", None)
        OPEN_LOAD_KEY = os.environ.get("OPEN_LOAD_KEY", None)
        # number of colums of buttons to be displayed in .mrx command

else:

    class Config(object):
        DB_URI = None


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
