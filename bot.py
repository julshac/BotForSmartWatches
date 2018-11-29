#!/usr/bin/python
# -*- coding: windows-1251 -*-

import config
import telebot
import time
import tickets
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, \
                          KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


if config.use_proxy:
    telebot.apihelper.proxy = {'https': 'socks5h://{}:{}@{}:{}'.format(config.proxy_user,
                                                                      config.proxy_pass,
                                                                      config.proxy_address,
                                                                      config.proxy_port)}

bot = telebot.TeleBot(config.token)


def string_parse(message, str):
    for i in range(0, len(str), 130):
        time.sleep(20)
        bot.send_message(message.chat.id, str[i: i + 130])
        time.sleep(20)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    print('start command incoming')
    bot.reply_to(message, "Send the ticket name to me")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "There is: Общезначимость, Кнф, Пнф, Скнф, Унификация, Сд, Атомы, Эу, Противоречивости, "
                          "Алгоритм, Метод")


@bot.message_handler(content_types=["text"])
def send_ticket(message):
    for i in tickets.ticket:
        if message.text == i:
            string_parse(message, tickets.ticket[i])


if __name__ == '__main__':
     bot.polling(none_stop=True)
