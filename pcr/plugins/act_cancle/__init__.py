from nonebot import on_command, CommandSession

from .commit_act_list_cancel import commit_act_list_cancel


@on_command('act_cancel', aliases=('取消代理', '还原', '取消代刀'))
async def act_cancel(session: CommandSession):
    isActCancel = await commit_act_list_cancel(session.event.sender)
    # 若列表被成功取消，则向用户反馈当前情况
    if isActCancel:
        await session.send('代理取消成功！')
    else:
        await session.send('代理取消失败！您不在代理名单中！')
