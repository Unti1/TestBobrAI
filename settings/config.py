############################################
"""Прочие необходимые библиотеки"""
import random
import configparser
import datetime
import re
from ast import literal_eval
from termcolor import colored
########################################### 

'''
Bot development
'''
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage

from aiogram import Router, types, F

from aiogram.types import Message, InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButton

from aiogram.filters import Command, StateFilter, CommandObject
from aiogram.filters.callback_data import CallbackData
from aiogram.enums import ParseMode
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile

MEDIA_FILES_ROOT = 'data/'
DEBUG = False


# from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
config = configparser.ConfigParser()
config.read(r'settings/settings.ini')  # читаем конфиг

def config_update():
    with open(r'settings/settings.ini', 'w') as f:
        config.write(f)
    config.read(r'settings/settings.ini')

import logging
logging.basicConfig(
    level=logging.INFO if DEBUG else logging.ERROR,
    filename="logs.log",
    format="%(asctime)s - %(module)s\n[%(levelname)s] %(funcName)s:\n %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
    encoding="utf-8"
)


# Кеширование [НЕИЗМЕННОЕ]
REDIS_HOST = config['redis']['host']
REDIS_PORT = config['redis']['port']
REDIS_DB = config['redis']['db']

TELEGRAM_TOKEN = config['Telegram']['token']

WEATHER_API_KEY = config['OpenWeather']['token']