from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.database.requests import get_categories, get_category_items


kb_main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                                        [KeyboardButton(text='Корзина')],
                                        [KeyboardButton(text='Контакты'),
                                         KeyboardButton(text='О нас')
                                         ]
                                        ],
                              resize_keyboard=True,
                              input_field_placeholder='Выберите команду...')


async def categories():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f'category_{category.id}'))
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()


async def category_items(category_id):
    all_category_items = await get_category_items(category_id)
    keyboard = InlineKeyboardBuilder()
    for category_item in all_category_items:
        keyboard.add(InlineKeyboardButton(text=category_item.name, callback_data=f'item_{category_item.id}'))
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()

kb_back_to_main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='На главную', callback_data='to_main')]])







# kb_main_catalog = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Футболки', callback_data='t-shirt')],
#                                                         [InlineKeyboardButton(text='Кроссовки', callback_data='sneaker')],
#                                                         [InlineKeyboardButton(text='Кепки', callback_data='cap')]
#                                                         ]
#                                        )
#
# kb_phone_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер',
#                                                                 request_contact=True)]
#                                                 ],
#                                       resize_keyboard=True
#                                       )