import telebot
from dotenv import load_dotenv
import os

TG_TOKEN2 = os.environ["TG_TOKEN2"]
bot2 = telebot.TeleBot(TG_TOKEN2)


@bot2.message_handler(commands=["start"])
def start_message(message):
    bot2.send_message(
        message.chat.id,
        "Здравствуйте, {0.first_name}! Напишите свой вопрос что бы вам смогли помочь ."
        .format(message.from_user))


@bot2.message_handler(content_types=['text'])
def answer_text(message):
    bot2.send_message(
        message.chat.id,
        "Ваш вопрос был принят на рассмотрение, скоро вам ответит админ")


def main():
    load_dotenv()
    bot2.infinity_polling()


if __name__ == "__main__":
    main()
