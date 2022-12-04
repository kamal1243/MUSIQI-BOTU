from Zaid import Zaid, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
SALAM! {}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ **MƏN TELEGRAM ÜÇÜN YARADILMIŞ MUSİQİ BOTUYAM**.
‣ **MƏN SƏNİN QRUPUNDA MAHNI OXUMAQ İSTƏYİRƏM**.
‣ **MƏN SÜRƏTLİ VƏ DONMASI OLMUYAN BOTAM**
‣ **MƏNİ YARADAN TEZ-TEZ YENİLİKLƏR EDİR**!
‣ **NƏNİMLƏ BİRLİKDƏ OLDUĞUN ZAMAN MAHNINI MP3 KİMİ YÜKLƏYƏ BİLƏRSƏN**.
‣ **ƏGƏR MAHNI OXUMURAMSA @GROOTMUSIC_BOT  USERIN QURUPA ƏLAVƏ EDİN**!
‣ **REKLAM VƏ İŞ BİRLİYİ ÜÇÜN @RafaelGray_DARKWEB - LƏ ƏLAQƏ YARADIN**!
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ **KÖMƏK BUTONUNA BAS 🔘 ƏLAVƏ MƏLUMAT ÜÇÜN ℹ️**.
"""

@Zaid.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("➕ QURUPA ƏLAVƏ ET", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👨‍💻 DEVELOPER", "https://www.t.me/RafaelGray_DARKWEB")],
        [Button.url("🗣️ DƏSTƏK", f"https://t.me/{Config.SUPPORT}"), Button.url("📣 GÜNCƏLLƏMƏ", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("ƏLAVƏ MƏLUMAT ÜÇÜN", data="help")]])
       return

    if event.is_group:
       await event.reply("**ʜᴇʏ! ɪ'ᴍ ꜱᴛɪʟʟ ᴀʟɪᴠᴇ ✅**")
       return



@Zaid.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ QURUPA ƏLAVƏ ET", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👨‍💻 DEVELOPER", "https://www.t.me/RafaelGray_DARKWEB")],
        [Button.url("🗣️ DƏSTƏK", f"https://t.me/{Config.SUPPORT}"), Button.url("📣 GÜNCƏLLƏMƏ", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("ƏLAVƏ MƏLUMAT ÜÇÜN", data="help")]])
       return
