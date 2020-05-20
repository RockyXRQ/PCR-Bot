from os import path

import nonebot

import config

if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'pcr', 'plugins'),
        'pcr.plugins'
    )
    nonebot.run()

# Todo: 加入天数增加机制 √
# Todo: 完善boss击杀判定 √
# Todo: 完善damage_append()函数 √
# Todo: 加入Log系统
# Todo: 加入help指令