from nonebot.default_config import *
import json

setting = open('Settings.json', encoding='utf-8')
setting = json.load(setting)

COMMAND_START = {'', '/', '!', '／', '！'}
HOST = setting['HOST']
PORT = setting['PORT']
