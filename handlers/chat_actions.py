import datetime
import sqlite3

from aiogram import types, Dispatcher
from config import bot, MEDIA_DESTINATION, GROUP_ID
from database import db
from const import BAN_USER_TEXT
from profanity_check import predict, predict_prob


async def chat_messages(message: types.Message):
    # ban_words_predict = predict([message.text])
    datab = db.Database()
    if message.chat.id == int(GROUP_ID ):
       ban_words_predict_prob = predict_prob([message.text])
       print(message.chat)
       if ban_words_predict_prob > 0.8:
           potential = datab.sql_select_ban_users(
               tg_id=message.from_user.id,
           )
           print(potential)
       if potential:
           if potential["count"] >= 3:
                   bot.ban_chat_member(
                       chat_id=message.chat.id,
                       user_id=message.from_user.id,
                       until_date=datetime.datetime.now() + datetime.timedelta(minutes=2)
                   )
           datab.sql_update_ban_count(
                tg_id=message.from_user.id,
                )
           await bot.send_message(
                chat_id=message.chat.id,
                text=BAN_USER_TEXT.format(
                    name=message.from_user.first_name,
                    count=potential['count'] + 1)
                )
       elif not potential:
              datab.sql_insert_ban_user(
                tg_id=message.from_user.id,
              )
              await bot.send_message(
                  chat_id=message.chat.id,
                  text=BAN_USER_TEXT.format(
                      name=message.from_user.first_name,
                      count=1)
              )
              await message.delete()



def register_chat_actions_handlers(dp: Dispatcher):
    dp.register_message_handler(chat_messages)