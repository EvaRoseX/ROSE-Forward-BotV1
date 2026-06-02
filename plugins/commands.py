# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os
import sys
import asyncio 
from database import Db, db
from config import Config, temp
from script import Script
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant
import psutil
import time as time
from os import environ, execle, system

START_TIME = time.time()

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

main_buttons = [[
    InlineKeyboardButton('❣️ ᴅᴇᴠᴇʟᴏᴘᴇʀ ❣️', url='https://t.me/kingvj01')
],[
    InlineKeyboardButton('🔍 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ', url='https://t.me/vj_bot_disscussion'),
    InlineKeyboardButton('🤖 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ', url='https://t.me/vj_botz')
],[
    InlineKeyboardButton('💝 sᴜʙsᴄʀɪʙᴇ ᴍʏ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ', url='https://youtube.com/@Tech_VJ')
],[
    InlineKeyboardButton('👨‍💻 ʜᴇʟᴘ', callback_data='help'),
    InlineKeyboardButton('💁 ᴀʙᴏᴜᴛ', callback_data='about')
],[
    InlineKeyboardButton('⚙ sᴇᴛᴛɪɴɢs', callback_data='settings#main')
]]

# 📢 MULTI-FORCE SUBSCRIBE CHECK FUNCTION (FIXED)
async def check_force_subscribe(client, message):
    channels = getattr(Config, "FORCE_SUB_CHANNELS", None)
    if not channels:
        return None

    for channel_id in channels:
        try:
            await client.get_chat_member(chat_id=channel_id, user_id=message.from_user.id)
        except UserNotParticipant:
            try:
                chat = await client.get_chat(channel_id)
                invite_link = chat.invite_link or (await client.create_chat_invite_link(channel_id)).invite_link
                return invite_link
            except Exception as e:
                print(f"Error generating link for {channel_id}: {e}")
                return None
        except Exception as e:
            print(f"Error checking member for {channel_id}: {e}")
            continue
            
    return None

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

@Client.on_message(filters.private & filters.command(['start']))
async def start(client, message):
    user = message.from_user
    if not await db.is_user_exist(user.id):
        await db.add_user(user.id, user.first_name)
    
    # 📢 MULTI-FORCE SUBSCRIBE CHECK START
    invite_link = await check_force_subscribe(client, message)
    if invite_link:
        fsub_buttons = [
            [InlineKeyboardButton("📢 Join Channel", url=str(invite_link))],
            [InlineKeyboardButton("🔄 Try Again", url=f"https://t.me/{(await client.get_me()).username}?start=start")]
        ]
        
        # Aapka fsub poster imgbb wala link
        FSUB_IMG = "https://i.ibb.co/HLhnypGg/photo-2026-05-27-17-49-35-7644630238818730000.jpg" 
        
        try:
            await client.send_photo(
                chat_id=message.chat.id,
                photo=FSUB_IMG,
                reply_markup=InlineKeyboardMarkup(fsub_buttons),
                caption=f"👋 Hello {user.first_name},\n\nOur bot is premium! To use this bot, you must join our update channels first. Click the button below to join!"
            )
            return  
        except Exception as e:
            print(f"Error sending Fsub photo: {e}")
            return
    # 📢 MULTI-FORCE SUBSCRIBE CHECK END

    # Agar saare channels joined hain, toh ye normal start menu chalega:
    reply_markup = InlineKeyboardMarkup(main_buttons)
    
    # Yahan apni main photo (girl photo) ka asli link daal dena
    START_IMG = "https://i.ibb.co/Psbzdt8L/photo-2026-03-20-17-00-37-7619383841232257040.jpg"
    
    try:
        await client.send_photo(
            chat_id=message.chat.id,
            photo=START_IMG,
            reply_markup=reply_markup,
            caption=Script.START_TXT.format(message.from_user.first_name)
        )
    except Exception as e:
        print(f"Error sending Start photo: {e}")

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

@Client.on_message(filters.private & filters.command(['restart']) & filters.user(Config.BOT_OWNER))
async def restart(client, message):
    msg = await message.reply_text(text="<i>Trying to restarting.....</i>")
    await asyncio.sleep(5)
    await msg.edit("<i>Server restarted successfully ✅</i>")
    system("git pull -f && pip3 install --no-cache-dir -r requirements.txt")
    execle(sys.executable, sys.executable, "main.py", environ)
