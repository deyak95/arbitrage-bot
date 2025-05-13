import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart

API_TOKEN = '7928008482:AAE8cEeT31MrOh9J22rRO5Tn-O3kTWzc4P8'
INVITE_LINK = 'https://t.me/+fIe-UKecsw0xN2Ey'

bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# Кнопки
subscribe_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Подписаться на канал", url=INVITE_LINK)],
    [InlineKeyboardButton(text="Я подписался", callback_data="confirm_subscription")]
])

start_lesson_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Начать урок", callback_data="start_lesson")]
])

next_lesson_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Урок 2: Как выбрать оффер", callback_data="lesson_2")]
])

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Привет! Чтобы получить доступ к уроку по арбитражу, подпишись на канал:",
        reply_markup=subscribe_keyboard
    )

@dp.callback_query(F.data == "confirm_subscription")
async def confirm_subscription(callback: CallbackQuery):
    await callback.message.answer("Отлично! Теперь ты можешь начать обучение:", reply_markup=start_lesson_keyboard)

@dp.callback_query(F.data == "start_lesson")
async def start_lesson(callback: CallbackQuery):
    lesson = [
        "Урок 1: Что такое арбитраж трафика?\n\nЭто заработок на разнице между покупкой трафика и оплатой за действия. "
        "Например: ты покупаешь 1000 переходов за 10$, а за 5 покупок получаешь 25$.",

        "Кто участвует в арбитраже:\n- Арбитражник (ты)\n- Рекламодатель\n- CPA-сеть\n- Источник трафика (FB, TikTok, Push)",

        "Как начать:\n1. Зарегистрируйся в CPA-сети\n2. Выбери оффер\n3. Запусти рекламу\n4. Получай выплаты за действия",

        "Рекомендации:\n- Начни с простого источника (например, Push)\n- Обязательно используй трекер (Keitaro, Binom)\n- Следи за ROI и не бойся тестировать"
    ]

    for part in lesson:
        await callback.message.answer(part)

    await callback.message.answer(
        "Урок 1 завершён. Хочешь перейти к следующему?",
        reply_markup=next_lesson_keyboard
    )

@dp.callback_query(F.data == "lesson_2")
async def lesson_2(callback: CallbackQuery):
    await callback.message.answer("Урок 2 будет доступен скоро!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())