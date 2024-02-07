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
    registration_button = InlineKeyboardButton(
        "Registration ",
        callback_data="registration"
    )
    my_profile_button = InlineKeyboardButton(
        "Profile",
        callback_data="my_profile"
    )
    view_profiles_button = InlineKeyboardButton(
        "View Profiles",
        callback_data="view_profiles"
    )
    reference_button = InlineKeyboardButton(
        "Referral Menu 🐉",
        callback_data="reference_menu"
    )
    markup.add(questionnaire_button, registration_button)
    markup.add(reference_button)
    markup.add(my_profile_button, view_profiles_button)

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
async def like_dislike_keyboard(owner):
    markup = InlineKeyboardMarkup()
    like_button = InlineKeyboardButton(
        "Like 👍🏻",
        callback_data=f"like_{owner}"
    )
    dislike_button = InlineKeyboardButton(
        "Dislike 👎🏻",
        callback_data=f"dislike_{owner}"
    )
    markup.add(like_button, dislike_button)
    return markup
async def my_profile_keyboard():
    markup = InlineKeyboardMarkup()
    update_button = InlineKeyboardButton(
        "Update 💵",
        callback_data=f"update_profile"
    )
    delete_button = InlineKeyboardButton(
        "Delete ❌",
        callback_data="delete_profile"
    )
    markup.add(update_button)
    markup.add(delete_button)
    return markup
async def referral_keyboard():
    markup = InlineKeyboardMarkup()
    generate_button = InlineKeyboardButton(
        "Generate Link 🔗",
        callback_data="generate_link"
    )
    markup.add(generate_button)
    return markup