import global_state as GlobalState


async def commit_on_tree(user: object):
    return GlobalState.on_tree_append(user['user_id'], user['nickname']), GlobalState.get_current_on_tree_list()
