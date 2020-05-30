import pcr.common.global_state as GlobalState


async def commit_act_list_change(user: object, act_user_nickname: str):
    return GlobalState.act_append(user['nickname'], act_user_nickname), GlobalState.get_current_act_list()
