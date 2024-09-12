import feedparser
from aiogram import Bot, Dispatcher, executor, types
from key import TELEGRAM_TOKEN
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

CHAT_ID = '123456789' # ID вашего чата

Bot = Bot(TELEGRAM_TOKEN)
dp = Dispatcher(Bot)

# A function for getting news from an RSS feed
def get_news():
    feed_url = 'https://lenta.ru/rss/last24'
    feed = feedparser.parse(feed_url)
    news_items = []
    for entry in feed.entries[:1]:  # We receive 1 latest news. Replace 1 with the required number of news items
        news_items.append(f"{entry.title}\n")
    print (news_items)
    return '\n'.join(news_items)

# The handler of the command /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi! I am a bot that sends the latest portal news Lenta.ru . To receive the news, type the command /news")

# The handler of the command /news
@dp.message_handler(commands=['news'])
async def send_news(message: types.Message):
    news = get_news()
    await Bot.send_message(chat_id=CHAT_ID, text=news)

def main():
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)

if __name__ == "__main__":
    main()
