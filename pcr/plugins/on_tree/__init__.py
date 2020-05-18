from nonebot import on_command, CommandSession

from .commit_on_tree import commit_on_tree


@on_command('on_tree', aliases=('挂树', '已挂树', '申请挂树', '会长！我挂树了！'))
async def on_tree(session: CommandSession):
    isOnTree, on_tree_list = await commit_on_tree(session.event.sender)

    if isOnTree:
        await session.send('您已挂树，等待救树\n当前挂树名单：\n' + str(on_tree_list))
    else:
        await session.send('您未在进攻中或已经挂树，无法挂树。若未进攻请进行出刀申请 PS:使用命令【出刀】')
