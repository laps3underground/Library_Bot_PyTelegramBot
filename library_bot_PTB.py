#coding: utf-8
#!/usr/bin/python3.7

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.ext.dispatcher import run_async
from telegram.error import NetworkError, Unauthorized, BadRequest
import logging
import requests
import json
import shodan
import random
import sys
import os
import re
import datetime
import socket
from pytz import timezone
import unicodedata as ud

updater = Updater(token='')

logging.basicConfig(level=logging.INFO)


def init(bot, update):
	bot.send_message(parse_mode='HTML', chat_id=update.message.chat_id, text='<b>Wassup</b>', reply_to_message_id=update.message.message_id)

def main():
	dispatcher = updater.dispatcher

	dispatcher.add_handler(CommandHandler('start', init))
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()
