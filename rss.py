import feedparser
from aiogram import Bot, Dispatcher, executor, types

# Параметры для Telegram
from key import TELEGRAM_TOKEN
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
# Параметры для Telegram

CHAT_ID = '1232578036' # ID вашего чата

Bot = Bot(TELEGRAM_TOKEN)
dp = Dispatcher(Bot)


# Функция для получения новостей из RSS-ленты
def get_news():
    feed_url = 'https://lenta.ru/rss/last24'
    feed = feedparser.parse(feed_url)
    news_items = []
    for entry in feed.entries[:1]:  # Получаем 1 последнюю новость
        #news_items.append(f"{entry.title}\n{entry.link}\n")
        news_items.append(f"{entry.title}\n")
    print (news_items)
    return '\n'.join(news_items)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот, который отправляет последнюю новость портала Lenta.ru. Для получения новости наберите команду /news")

# Обработчик команды /news
@dp.message_handler(commands=['news'])
async def send_news(message: types.Message):
    news = get_news()
    await Bot.send_message(chat_id=CHAT_ID, text=news)

# Главная функция
def main():
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)

if __name__ == "__main__":
    main()