"""
Apache License 2.0
Copyright (c) 2022 @PYRO_BOTZ 
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
Telegram Link : https://t.me/PYRO_BOTZ 
Repo Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT
License Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT/blob/main/LICENSE
"""

from os import environ
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
import humanize
from helper.txt import mr
from helper.database import insert 
from helper.utils import not_subscribed 

START_PIC = environ.get("START_PIC", "https://telegra.ph/file/27e9ed6b222498bd1c177.jpg")

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    buttons = [[ InlineKeyboardButton(text="π’ <b>πΉπΎπΈπ½ πΌπ ππΏπ³π°ππ΄π π²π·π°π½π½π΄π» </b>π’", url=client.invitelink) ]]
    text = "**π ππΎπππ π΅ππΈπ΄π½π³ ππΎπ ππ΄ππ΄ π½πΎπ πΉπΎπΈπ½π΄π³ πΌπ π²π·π°π½π½π΄π»...πΉπΎπΈπ½ πΌπ ππΏπ³π°ππ΄π π²π·π°π½π½π΄π» ππΎ πππ΄ ππ·πΈπ π±πΎπ π΅ππΈπ΄π½π³ π**"
    await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
           
@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    insert(int(message.chat.id))
    await message.reply_photo(
       photo=START_PIC,
       caption=f"""π <b>π·π°πΈ</b> {message.from_user.mention} \n\n<b>πΈ π°πΌ π° πΏπΎππ΄ππ΅ππ»π» ππ΄π½π°πΌπ΄π π±πΎπ ππΈππ· π²ππππΎπΌ π²π°πΏππΈπΎπ½ & πΏπ΄ππΌπ°π½π΄π½π ππ·ππΌπ±π½π°πΈπ» πππΏπΏπΎππ...π§βπ»</b>\n\nπ<b>πΌπ πΎππ½π΄π  :</b> <b><a href=https://t.me/ajay_king_x>βα΄α΄α΄Κβ</a></b>""",
       reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("πΌ π³π΄ππ πΌ", callback_data='dev')                
                ],[
                InlineKeyboardButton('π’ ππΏπ³π°ππ΄π π’', url='https://t.me/Tamil_movie_studio'),
                InlineKeyboardButton('πΏ πππΏπΏπΎππ πΏ', url='https://t.me/+8LCFCFGUy_JlNDhl')
                ],[
                InlineKeyboardButton('π» π°π±πΎππ π»', callback_data='about'),
                InlineKeyboardButton('βΉοΈ π·π΄π»πΏ βΉοΈ', callback_data='help')
                ]]
          )
       )
    return

@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size)
    fileid = file.file_id
    await message.reply_text(
        f"""**ππ·π°π π³πΎ ππΎπ ππ°π½π πΌπ΄ ππΎ π³πΎ ππΈππ· ππ·πΈπ π΅πΈπ»π΄.?**\n\n**π΅πΈπ»π΄ π½π°πΌπ΄** :- `{filename}`\n\n**π΅πΈπ»π΄ ππΈππ΄ :-** `{filesize}`""",
        reply_to_message_id = message.id,
        reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("π ππ΄π½π°πΌπ΄ π",callback_data = "rename")],
        [InlineKeyboardButton("βοΈ π²π°π½π²π΄π» βοΈ",callback_data = "cancel")  ]]))


@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=f"""π <b>π·π°πΈ</b> {message.from_user.mention} \n\n<b>πΈ π°πΌ π° πΏπΎππ΄ππ΅ππ»π» ππ΄π½π°πΌπ΄π π±πΎπ ππΈππ· π²ππππΎπΌ π²π°πΏππΈπΎπ½ & πΏπ΄ππΌπ°π½π΄π½π ππ·ππΌπ±π½π°πΈπ» πππΏπΏπΎππ...π§βπ»</b>\n\nπ<b>πΌπ πΎππ½π΄π  :</b> <b><a href=https://t.me/ajay_king_x>βα΄α΄α΄Κβ</a></b>""",
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("πΌ π³π΄ππ πΌ", callback_data='dev')                
                ],[
                InlineKeyboardButton('π’ ππΏπ³π°ππ΄π π’', url='https://t.me/Tamil_movie_studio'),
                InlineKeyboardButton('πΏ πππΏπΏπΎππ πΏ', url='https://t.me/+8LCFCFGUy_JlNDhl')
                ],[
                InlineKeyboardButton('π» π°π±πΎππ π»', callback_data='about'),
                InlineKeyboardButton('βΉοΈ π·π΄π»πΏ βΉοΈ', callback_data='help')
                ]]
                )
            )
        return
    elif data == "help":
        await query.message.edit_text(
            text=mr.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               #β οΈ don't change source code & source link β οΈ #
               InlineKeyboardButton("β£οΈ ππΎπππ²π΄ β£οΈ", url="https://t.me/ajay_king_x")
               ],[
               InlineKeyboardButton("π π²π»πΎππ΄ π", callback_data = "close")
               ]]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=mr.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup( [[
               #β οΈ don't change source code & source link β οΈ #
               InlineKeyboardButton("β£οΈ ππΎπππ²π΄ β£οΈ", url="https://t.me/ajay_king_x")
               ],[
               InlineKeyboardButton("π₯οΈ  π·πΎπ ππΎ πΌπ°πΊπ΄  π₯οΈ", url="https://t.me/ajay_king_x")
               ],[
               InlineKeyboardButton("π π²π»πΎππ΄ π", callback_data = "close")
               ]]
            )
        )
    elif data == "dev":
        await query.message.edit_text(
            text=mr.DEV_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               #β οΈ don't change source code & source link β οΈ #
               InlineKeyboardButton("β£οΈ ππΎπππ²π΄ β£οΈ", url="https://t.me/ajay_king_x")
               ],[
               InlineKeyboardButton("π₯οΈ  π·πΎπ ππΎ πΌπ°πΊπ΄  π₯οΈ", url="https://t.me/ajay_king_x")
               ],[
               InlineKeyboardButton("π π²π»πΎππ΄ π", callback_data = "close")
               ]]
            )
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            await query.message.delete()




