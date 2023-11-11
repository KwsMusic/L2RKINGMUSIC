from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🦋ᴀᴅᴅ ᴍᴇ ɪɴ ɢʀᴘ ʙᴀʙᴜ🧸",              
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="❤️⃡˓⃝˓⃝˓⃝˓⃝˓⃝   ʜᴇʟᴩ   ˓⃝˓⃝˓⃝˓⃝˓⃝❤️",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="🇮🇳Sᴇᴛᴛɪɴɢs🇮🇳", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🦋ᴀᴅᴅ ᴍᴇ ɪɴ ɢʀᴘ ʙᴀʙᴜ🧸",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="❤️⃡˓⃝˓⃝˓⃝˓⃝˓⃝   ʜᴇʟᴩ   ˓⃝˓⃝˓⃝˓⃝˓⃝❤️", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="🍒̵̶⃰͟˶֟፝͟͝sᴜᴩᴩᴏʀᴛ⏎͟🝛꯭", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="👑ᴏᴡɴᴇʀ👑", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="🇮🇳ʀᴏᴘᴇ ʙωғ🇮🇳", callback_data="gib_source"
            )
        ],
     ]
    return buttons
