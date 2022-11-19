import telebot

from BackendRu import Grammar

bot = telebot.TeleBot('5671126981:AAEgvW5T4KLsyP8_yi7P38bO21SmpZvxze8')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Приветствую вас ,{message.from_user.first_name}. Я могу проверить слово "
                                      f"на написание приставок -пре и - при.\n"
                                      f"Для проверки написания слова, необходимо ввести слово"
                                      f" с нижним подчёркиванием в конце приставок -пре и - при "
                                      f"\nПримеры:  пр_бить, пр_зидент, пр_открыть, и т.д.")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    a = Grammar(message.text.lower(), 'и', 'е')
    bot.send_message(message.chat.id, a.FindTheRightWord())


bot.infinity_polling()