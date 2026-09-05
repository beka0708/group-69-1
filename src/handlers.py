from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router

from src.keyboards import keybord_main, inline


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}",
        reply_markup=keybord_main
    )

    print(f"Написал пользователь {message.from_user.full_name} его ID, {message.from_user.id} его ник, {message.from_user.username}")


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        '/start - приветсвие\n'
        '/help - список команд',
        reply_markup=inline
    )


@router.message(F.text.lower() == 'группа')
async def cmd_group(message: Message):
    await message.answer("Твоя группа это 69-1")


@router.message(F.text == 'Каталог')
async def cmd_catalog(message: Message):
    await message.answer("Наш каталог к сожалению пуст :(")


@router.callback_query(F.data == 'quiz_start')
async def quiz_start(callback: CallbackQuery):
    await callback.answer("Начинаем игру!", show_alert=True)
    await callback.message.answer('Do you speak English?')


@router.message()
async def echo(message: Message):
    await message.answer(f"Ты написал: {message.text}")