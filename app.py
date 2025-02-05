
import telebot
from config import currencies, TOKEN, CryptoConverter, APIException

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Я люблю майнкрафт!!! \n Можешь написать /values, если тебе заняться нечем'

    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Че надо?'
    for key in currencies:
        text += '\n' + key
    text += '\n ПИШИ ТАК ЖЕ, КАК В ПРИМЕРЕ И ЧЕРЕЗ - БЕЗ ПРОБЕЛОВ!!! ПХУ!'

    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convertor(message: telebot.types.Message):
    values = message.text.split('-')

    try:
        if len(values) != 3:
            raise APIException('Неверно введены параметры')
        base, quote, amount = values
        total_base = CryptoConverter.get_price(base, quote, amount)
    except APIException as e:
        bot.reply_to(message, f'ДЛлиод3р81с.')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {base} в {quote}: {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)


