from nonebot import on_command, CommandSession

import global_state as GlobalState


@on_command('get_list', aliases=('查看', '查看情况', '获取情况'))
async def get_list(session: CommandSession):
    await session.send('当前攻打中列表：\n' + str(GlobalState.get_current_atking_list()) +
                       '\n当前挂树列表:\n' + str(GlobalState.get_current_on_tree_list()) +
                       '\n当前救树列表：\n' + str(GlobalState.get_current_save_tree_list()))
