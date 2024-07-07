from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keybords as kb

router = Router()

class Register(StatesGroup):
    name = State()
    age = State()
    phone_number = State()

@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Введите ваше имя')

@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer('Введите ваш возраст')

@router.message(Register.age)
async def register_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.phone_number)
    await message.answer('Введите ваш номер телефона', reply_markup=kb.kb_phone_number)

@router.message(Register.phone_number, F.contact) #F.contact - условме, что пользователь нажмет на кнопку kb.kb_phone_number
async def register_phone_number(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f"Ваше имя: {data['name']}\nВаш возраст: {data['age']}\nНомер телефона: {data['phone_number']}")
    await state.clear()