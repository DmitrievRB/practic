import telebot
from config import keys, TOKEN
from extensions import APIException, ConvertionExpeption
# Импортируем библиотеки и доп. файлы проекта
bot = telebot.TeleBot(TOKEN)
# Запускаем бот


@bot.message_handler(commands=["start", "help"]) #Обработка  команды /start и  /help
def help_start(message: telebot.types.Message):
    text = "Для конвертации наберите через пробел сообщение :\n <Валюту приобретения> \
<Валюту оплаты> <количество > \n Увидеть список всех доступных валют : /values"
    bot.reply_to(message, text)


@bot.message_handler(commands=["values"]) # Обработка команды /values
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = "\n".join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=["text", ])# Обработка запроса пользователя на конвертацию
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(" ")
        if len(values) != 3:
            raise ConvertionExpeption("Слишком много параметров")#Исключение при количестве параметров не равном 3
        quote, base, amount = values
        total_base = APIException.get_price(quote, base, amount)
        total_sum = total_base * float(amount)
    except ConvertionExpeption as e:
        bot.reply_to(message, f"Ошибка пользователя.\n{e}") # Обработка исключений  для отделения ошибок пользователя от ошибок 
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду {e}")
    else:
        text = f" Стоимость   {amount}  {quote}  в {base} - {round(total_sum,2)}"
        bot.send_message(message.chat.id, text)


bot.polling()
