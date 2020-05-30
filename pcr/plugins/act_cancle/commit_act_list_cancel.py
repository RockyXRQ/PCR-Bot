import pcr.common.global_state as GlobalState


async def commit_act_list_cancel(user: object):
    return GlobalState.act_cancel(user['nickname'])
