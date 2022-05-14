from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import *
from bd import *
from calc import *


bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


@dp.message_handler(content_types=['sticker'])
async def idk_message(msg: types.Message):
    print(msg.sticker.file_id)
    if selectScore(msg.sticker.file_id):
        score = selectScore(msg.sticker.file_id)
        addScorePeople(msg.reply_to_message.from_user.username, score)
        await bot.send_message(msg.chat.id,
                               '@{}  має  {} кредитів'.format(msg.reply_to_message.from_user.username,
                                                                      getScorePeople(msg.reply_to_message.from_user.username)))


@dp.message_handler(commands=['showtop'])
async def process_start_command(message: types.Message):
    show = showTop()
    sendStr = ''
    for i in show:
        sendStr += '@{}   має   {} кредитів    \n'.format(i[0], i[1])
    print(sendStr)

    await bot.send_message(message.chat.id, sendStr)

if __name__ == '__main__':
    executor.start_polling(dp)