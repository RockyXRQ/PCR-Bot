from nonebot import on_command, CommandSession

from .commit_act_apply_change import commit_act_list_change


@on_command('act_apply', aliases=('代理', '变身', '代刀'))
async def act_apply(session: CommandSession):
    # 从会话状态中（session.state）中获取申请出战的阵容，如果使用命令时未给出阵容，
    # 将会进一步追问，否则无法申请出战
    act_name = session.get(
        'act_name', prompt='请输入所代理会员昵称（原始QQ昵称）:')
    # 取出代理否被成功上传 并 获得当前的代理列表
    isActAppend, act_list = await commit_act_list_change(
        session.event.sender, act_name)
    # 若列表被成功添加，则向用户反馈当前情况
    if isActAppend:
        await session.send('代理成功！\n您所代理的角色为：\n' + str(act_name) + '\n当前代理人员名单为：\n' + str(act_list))
    else:
        await session.send('代理申请失败！')

# act_apply.args_praser 将该函数声明为 atk_apply 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
# 注意：参数解析器将在 atk_apply 命令实际函数执行前执行
@act_apply.args_parser
async def _(session: CommandSession):
    arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 若该命令是第一次执行
        if arg:
            # 第一次运行时参数不为空，即正确保存参数进入state
            session.state['act_name'] = arg
        return

    if not arg:
        # 填写的代理昵称为空
        session.pause('填写的代理昵称为空，请重新填写！')

        # 若当前正在询问更多信息，且新输入的信息有效，则放入会话状态
    session.state[session.current_key] = arg
