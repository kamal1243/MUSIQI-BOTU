from telethon import events, Button
from Zaid import Zaid
from Zaid.status import *
from Config import Config
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import ExportChatInviteRequest

@Zaid.on(events.callbackquery.CallbackQuery(data="admin"))
async def _(event):

    await event.edit(ADMIN_TEXT, buttons=[[Button.inline("« Bᴀᴄᴋ", data="help")]])

@Zaid.on(events.callbackquery.CallbackQuery(data="play"))
async def _(event):

    await event.edit(PLAY_TEXT, buttons=[[Button.inline("« Bᴀᴄᴋ", data="help")]])


ADMIN_TEXT = """
**✘ Yalnız admin kodları!**

‣ `?end` - Mahnını durdurur.
‣ `?skip` - Növbəti mahnıya eçir.
‣ `?pause` - Mahnını dondurur.
‣ `?resume` - Mahnıya dabam edir.
‣ `?leavevc` - Bot səsdən cıxır.
‣ `?playlist` - Güzləmədə olan mahnılar.
"""

PLAY_TEXT = """
**✘ User kodları!**

‣ `?play` - Mahnını qoşmaq üçün.
‣ `?vplay` - Mahnını mp3 yükləmək üçün.
"""
