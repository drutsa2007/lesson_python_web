import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters.command import Command
from aiogram.filters import CommandStart
from aiogram.types.input_file import FSInputFile
from aiogram.types.message import ContentType
from token_tg import API_TOKEN


bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# amount в копейках
PRICE = types.LabeledPrice(label='Заголовок для оплаты', amount=200*100)
cover = FSInputFile("files/cover_guide.jpg")


@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.reply("Набери команду /buy.")


# функция для покупки
@dp.message(Command('buy'))
async def buy_guide(message: types.Message):
    await message.answer("Тестовый платеж")
    await message.answer_invoice(
        title="Название товара",
        description="Описание товара",
        provider_token="381764678:TEST:66115",  # тестовый токен
        currency="RUB",
        is_flexible=False,  # если конечная цена, зависит от доставки то True
        prices=[PRICE],  # название и цена
        photo_url="https://drive.google.com/file/d/1V1Y6m_77qNg2N3h_N205M_vWgm3l42DL/view?usp=drivesdk",  # картинка
        photo_width=300,
        photo_height=400,
        photo_size=400,
        payload="invoice-payload-guide",  # текст оплаты
        start_parameter="qaz",  # если пустым то оплата в любом боте
        need_name=True,  # передать имя пользователя
        need_phone_number=True,  # передать телефон пользователя
        need_shipping_address=False,  # если нужен адрес то True
    )


# pre checkout  (must be answered in 10 seconds)
@dp.pre_checkout_query()
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    # принимание каких-то решений в этом блоке, например есть ли в наличии
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


# successful payment
@dp.message()
async def successful_payment(message: types.Message):
    # print(message.successful_payment)  # придет информация ниже для обработки
    # currency='RUB' total_amount=20000 invoice_payload='invoice-payload-guide'
    # telegram_payment_charge_id='5204511405_1322265845_9925'
    # provider_payment_charge_id='2cb0c215-000f-5000-a000-171f5fde129e'
    # shipping_option_id=None
    # order_info=OrderInfo(name='Указанное имя', phone_number='Указанный телефон', email=None, shipping_address=None)

    await message.answer(f"Платеж на сумму {message.successful_payment.total_amount // 100} "
                         f"{message.successful_payment.currency} прошел успешно!!!")


async def main():
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
   asyncio.run(main())

