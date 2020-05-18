import global_state as GlobalState


async def commit_global_atking_state(user: object, team_info: str):
    return GlobalState.team_info_append(user['user_id'],
                                        user['nickname'],
                                        team_info), GlobalState.get_current_atking_list()
