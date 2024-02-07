import sqlite3

from aiogram import types, Dispatcher
from config import bot, MEDIA_DESTINATION
from database import db
from const import START_MENU, PROFILE_TEXT
from database.db import Database
from keyboards import inline_buttons
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class RegistrationStates(StatesGroup):
    nickname = State()
    biography = State()
    age = State()
    zodiac = State()
    gender = State()
    year = State()
    photo = State()


async def registration_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Send me ur Nickname, please!'
    )
    await RegistrationStates.nickname.set()
async def load_nickname(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data['nickname'] = message.text
        print(data)


    await bot.send_message(
       chat_id=message.from_user.id,
       text='Send me ur Bio!'
    )
    await RegistrationStates.next()


async def load_biography(message: types.Message,
                         state: FSMContext):
    async with state.proxy() as data:
        data['bio'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='How old r u ?\n'
             '(Only numeric age in text)\n'
             'Example: 27, 28'
    )
    await RegistrationStates.next()


async def load_age(message: types.Message,
                   state: FSMContext):
    try:
        type(int(message.text))
    except ValueError:
        await bot.send_message(
            chat_id=message.from_user.id,
            text='I told u send me ONLY numeric text\n'
                 'registration failed ❌\n'
                 'Restart registration!!!'
        )
        await state.finish()
        return

    async with state.proxy() as data:
        data['age'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='What is ur Zodiac Sign ?'
    )
    await RegistrationStates.next()


async def load_zodiac(message: types.Message,
                           state: FSMContext):
    async with state.proxy() as data:
        data['sign'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='What is your gender?'
    )
    await RegistrationStates.next()

async def load_gender(message: types.Message,
                           state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Which year are you?\n'
             'Example: year of the dog, rat, horse etc.'
    )
    await RegistrationStates.next()

async def load_year(message: types.Message,
                           state: FSMContext):
    async with state.proxy() as data:
        data['year'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Send me ur photo\n'
             '(only in photo mode sender)'
    )
    await RegistrationStates.next()
async def load_photo(message: types.Message,
                     state: FSMContext):
    db = Database()
    path = await message.photo[-1].download(
        destination_dir=MEDIA_DESTINATION
    )

    async with state.proxy() as data:
        db.sql_insert_profile(
            tg_id=message.from_user.id,
            nickname=data['nickname'],
            bio=data['bio'],
            age=data['age'],
            sign=data['sign'],
            gender=data['gender'],
            year=data['year'],
            photo=path.name,
        )

        with open(path.name, 'rb') as photo:
            await bot.send_photo(
                chat_id=message.from_user.id,
                photo=photo,
                caption=PROFILE_TEXT.format(
                    nickname=data['nickname'],
                    bio=data['bio'],
                    age=data['age'],
                    sign=data['sign'],
                    gender=data['gender'],
                    year=data['year']
                ),
            )
        await bot.send_message(
            chat_id=message.from_user.id,
            text='U have successfully Registered\n'
                 'Congratulations '
        )


def register_registration_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        registration_start,
        lambda call: call.data == "registration"
    )
    dp.register_message_handler(
        load_nickname,
        state=RegistrationStates.nickname,
        content_types=['text']
    )
    dp.register_message_handler(
        load_biography,
        state=RegistrationStates.biography,
        content_types=['text']
    )
    dp.register_message_handler(
        load_age,
        state=RegistrationStates.age,
        content_types=['text']
    )
    dp.register_message_handler(
        load_zodiac,
        state=RegistrationStates.zodiac,
        content_types=['text']
    )
    dp.register_message_handler(
        load_gender,
        state=RegistrationStates.gender,
        content_types=['text']
    )
    dp.register_message_handler(
        load_year,
        state=RegistrationStates.year,
        content_types=['text']
    )
    dp.register_message_handler(
        load_photo,
        state=RegistrationStates.photo,
        content_types=types.ContentTypes.PHOTO
    )
