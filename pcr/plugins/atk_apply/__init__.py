from nonebot import on_command, CommandSession

from .commit_apply_change import commit_global_atking_state


@on_command('atk_apply', aliases=('申请出刀', '出刀申请', '出刀'))
async def atk_apply(session: CommandSession):
    # 从会话状态中（session.state）中获取申请出战的阵容，如果使用命令时未给出阵容，
    # 将会进一步追问，否则无法申请出战
    team_info = session.get('team_info', prompt='请再次确认阵容输入正确，并输入您的出刀队伍阵容（队伍各成员名称请以空格隔开）:')
    # 获取出战队伍信息是否被成功上传
    is_atk_append_success, atking_list = await commit_global_atking_state(session.event.sender, team_info)
    # 若列表被成功添加，则向用户反馈当前情况
    if is_atk_append_success:
        await session.send('出刀申请成功！\n您的出刀阵容为：\n' + str(team_info) + '\n当前攻打中人员名单为：\n' + str(list(atking_list)))
    else:
        await session.send('出刀申请失败！当前有人救树中！请稍后申请！')

# atk_apply.args_praser 将该函数声明为 atk_apply 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
# 注意：参数解析器将在 atk_apply 命令实际函数执行前执行
@atk_apply.args_parser
async def _(session: CommandSession):
    arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 若该命令是第一次执行
        if arg and team_check(arg):
            # 第一次运行时参数不为空，即正确保存参数进入state
            # 例如：申请出刀 tp弓 充电宝 狼 狗 黑骑
            session.state['team_info'] = arg
        return

    if (not arg) or (not team_check(arg)):
        # 填写的阵容名单为空（不为5个成员）
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('填写的阵容名单为空或不符合规格，请重新填写！')

        # 若当前正在询问更多信息，且新输入的信息有效，则放入会话状态
    session.state[session.current_key] = arg


def team_check(team_info: str):
    arg = team_info.split()
    return len(arg) == 5 and len((list(set(arg)))) == len(arg)
