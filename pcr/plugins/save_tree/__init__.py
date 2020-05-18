from nonebot import on_command, CommandSession

from .commit_save_tree import commit_save_tree


@on_command('save_tree', aliases=('救树', '申请救树', '别慌！我来也！'))
async def save_tree(session: CommandSession):
    team_info = session.get(
        'team_info', prompt='请再次确认阵容输入正确，并输入您的救树队伍阵容（队伍各成员名称请以空格隔开）:')

    isSaveCan, save_tree_list = await commit_save_tree(session.event.sender, team_info)

    if isSaveCan:
        await session.send('救树申请成功！您的出刀阵容为：\n' + str(team_info) +
                           '\n当前救树中人员名单为：\n' + str(list(save_tree_list)))
    else:
        await session.send('救树申请失败！当前无人挂树 或 您正在挂树 或 您已在救树中')


@save_tree.args_parser
async def _(session: CommandSession):
    arg = session.current_arg_text.strip()

    if session.is_first_run:
        if arg and team_check(arg):
            session.state['team_info'] = arg
        return

    if (not arg) or (not team_check(arg)):
        session.pause('填写的阵容名单为空或不符合规格，请重新填写！')
    session.state[session.current_key] = arg


def team_check(team_info: str):
    arg = team_info.split()
    return len(arg) == 5 and len((list(set(arg)))) == len(arg)
