import global_state as GlobalState


async def commit_save_tree(user: object, team_info: str):
    return GlobalState.save_tree_append(user['user_id'],
                                        user['nickname'],
                                        team_info), GlobalState.get_current_save_tree_list()
