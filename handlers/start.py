import sqlite3

from aiogram import types, Dispatcher
from config import bot, MEDIA_DESTINATION
from database import db
from const import START_MENU
from keyboards import inline_buttons

async def start_button(message: types.Message):
    datab = db.Database()
    datab.sql_insert_user(
        tg_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )
    print(message)
    with open(MEDIA_DESTINATION + "bot_pic.png", "rb") as photo:
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=photo,
            caption=START_MENU.format(
            name=message.from_user.first_name),
            reply_markup=await inline_buttons.start_keyboard())
def register_start_handlers(dp: Dispatcher):
     dp.register_message_handler(start_button, commands=['start'])