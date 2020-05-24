import pcr.common.global_state as GlobalState


async def commit_atk_damage(user: object, damage: int):
    return GlobalState.damage_append(user['user_id'], user['nickname'], damage)
