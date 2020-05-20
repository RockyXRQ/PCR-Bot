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

# Todo: 加入help指令
# Todo: 下树提醒
# Todo: 补时刀boss血量计算问题 √
# Todo: 由分数记录改为伤害记录 √