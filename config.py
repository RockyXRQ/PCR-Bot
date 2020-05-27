from nonebot.default_config import *
import json

settings = open('Settings.json', encoding='utf-8')
settings = json.load(settings)

COMMAND_START = {'', '/', '!', '／', '！'}
HOST = settings['HOST']
PORT = settings['PORT']
