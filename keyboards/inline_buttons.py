from aiogram.types import (
   InlineKeyboardMarkup,
   InlineKeyboardButton
)

async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Questionnaire",
        callback_data="start_questionnaire"
    )
    markup.add(questionnaire_button)
    return markup

async def questionnaire_first_answers():
    markup = InlineKeyboardMarkup()
    Laptop_button = InlineKeyboardButton(
        "Laptop",
        callback_data="Laptop"
    )
    Computer_button=InlineKeyboardButton(
        "Computer",
        callback_data="Computer"
    )
    markup.add(Laptop_button)
    markup.add(Computer_button)
    return markup

async def continue_keyboard():
    markup = InlineKeyboardMarkup()
    continue_questionnaire_button = InlineKeyboardButton(
        "second_questionnaire",
        callback_data="start_questionnaire"
    )
    markup.add(continue_questionnaire_button)
    return markup
async def questionnaire_second_answers():
    markup = InlineKeyboardMarkup()
    mouse_button = InlineKeyboardButton(
        "mouse",
        callback_data="mouse"
    )
    touchpad_button = InlineKeyboardButton(
        "touchpad",
        callback_data="touchpad"
    )
    markup.add(mouse_button)
    markup.add(touchpad_button)
    return markup

async def end_keyboard():
    markup = InlineKeyboardMarkup()
    end_questionnaire_button = InlineKeyboardButton(
        "third_questionnaire",
        callback_data="start_questionnaire"
    )
    markup.add(end_questionnaire_button)
    return markup
async def questionnaire_third_answers():
    markup = InlineKeyboardMarkup()
    iphone_button = InlineKeyboardButton(
        "iphone",
        callback_data="iphone"
    )
    samsung_button = InlineKeyboardButton(
        "samsung",
        callback_data="samsung"
    )
    markup.add(iphone_button)
    markup.add(samsung_button)
    return markup