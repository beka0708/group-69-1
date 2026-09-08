from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from src.keyboards import keybord_main, inline
from src.questions import QUESTIONS


router = Router()


class Quiz(StatesGroup):
    waiting_answer = State()


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

# FSM - Finite State Machine

@router.callback_query(F.data == 'quiz_start')
async def quiz_start(callback: CallbackQuery, state: FSMContext):
    await callback.answer("Начинаем игру!", show_alert=True)
    await state.update_data(index=0, score=0)   # сохраняем прогресс
    await state.set_state(Quiz.waiting_answer)  # переходим в состояние

    await callback.message.answer('Вопрос 1: ' + QUESTIONS[0]['q'])


@router.message(Quiz.waiting_answer)
async def handle_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    index = data['index']
    score = data['score']

    if message.text.lower() == QUESTIONS[index]['a']:
        score += 1
        await message.answer("Крассавчик правильно, Бонжур! +1")
    else:
        await message.answer(f"Неверно. Правильный ответ: {QUESTIONS[index]['a']}")

    index += 1
    len_questions = len(QUESTIONS)
    if index == len_questions:
        await message.answer(f"Конец! Счет: {score}/{len_questions}")
        await state.clear()
    else:
        await state.update_data(index=index, score=score)
        await message.answer(f"Вопрос {index + 1}: " + QUESTIONS[index]['q'])


@router.message()
async def echo(message: Message):
    await message.answer(f"Ты написал: {message.text}")