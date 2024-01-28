from aiogram import types, Dispatcher
from config import bot
from database import db
from keyboards import inline_buttons


async def first_questionnaire(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text=f"Laptop or Computer?",
        reply_markup = await inline_buttons.questionnaire_first_answers()
    )
async def Laptop_answer(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text=f"Cool cuz laptop is comfortable",
        reply_markup = await inline_buttons.questionnaire_first_answers()
    )
async def Computer_answer(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text=f"Cool cuz computer is more powerful",
        reply_markup = await inline_buttons.questionnaire_first_answers()
    )


async def second_questionnaire(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text=f"mouse or touchpad?",
        reply_markup = await inline_buttons.questionnaire_second_answers()
    )
async def mouse_answer(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text=f"mouse is fast and cool",
        reply_markup=await inline_buttons.questionnaire_second_answers()
    )
async def touchpad_answer(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text=f"touchpad is basic",
        reply_markup=await inline_buttons.questionnaire_second_answers()
    )

async def third_questionnaire(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text=f"iphone or samsung?",
        reply_markup=await inline_buttons.questionnaire_third_answers()
    )

async def iphone_answer(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text=f"iphone is cool",
        reply_markup=await inline_buttons.questionnaire_third_answers()
    )

async def samsung_answer(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text=f"samsung is an old school",
        reply_markup=await inline_buttons.questionnaire_third_answers()
    )
def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(first_questionnaire,
                                        lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(Laptop_answer,
                                        lambda call: call.data == "Laptop",)
    dp.register_callback_query_handler(Computer_answer,
                                        lambda call: call.data == "Computer")
def continue_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(second_questionnaire,
                                        lambda call: call.data == "continue_questionnaire")
    dp.register_callback_query_handler(mouse_answer,
                                        lambda call: call.data == "mouse")
    dp.register_callback_query_handler(touchpad_answer,
                                        lambda call: call.data == "touchpad")

def end_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(third_questionnaire,
                                        lambda call: call.data == "end_questionnaire")
    dp.register_callback_query_handler(iphone_answer,
                                        lambda call: call.data == "iphone")
    dp.register_callback_query_handler(samsung_answer,
                                        lambda call: call.data == "samsung")
