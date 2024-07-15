from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart

import app.keybords as kb
import app.database.requests as rq

router = Router()

@router.message(CommandStart()) #Command('start')
async def cmd_start(message: Message):
    print(message.from_user)
    await rq.set_user(message.from_user.id)
    await message.answer('Добро пожаловать в магазин кроссовок! Прошу выбрать команду', reply_markup=kb.kb_main)
    # await message.reply('=()')

@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer(f'Выберите категорию товара', reply_markup=await kb.categories())

@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.answer(f'Вы выбрали категорию {callback.message.text}')
    await callback.message.answer('Выберите товар', reply_markup=await kb.category_items(callback.data.split('_')[1]))

@router.callback_query(F.data.startswith('item_'))
async def item(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.answer(f'Вы выбрали товар')
    await callback.message.answer(f'Название: {item_data.name}\nОписание: {item_data.description}\nЦена: {item_data.price} руб.',
                                  reply_markup=kb.kb_back_to_main)

@router.callback_query(F.data == 'to_main')
async def main(callback: CallbackQuery):
    await callback.answer('Главное меню')
    await callback.message.answer('Выберите команду', reply_markup=kb.kb_main)



# @router.message(Command('help')) #/help
# async def cmd_help(message: Message):
#     await message.answer('Здесь запишем полезные ссылки')
#
# @router.message(F.text == 'Каталог')
# async def catalog(message: Message):
#     await message.answer('Выберите категорию товара', reply_markup=kb.kb_main_catalog)
#
# @router.callback_query(F.data == 't-shirt')
# async def t_shirt(callback: CallbackQuery):
#     await callback.answer('Вы выбрали категорию') #, show_alert=True
#     await callback.message.answer('Вы выбрали категорию футболок.')