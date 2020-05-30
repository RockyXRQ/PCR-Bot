import pcr.common.global_state as GlobalState


async def commit_atk_damage(user: object, damage: int):
    if int(damage) >= 0:
        return GlobalState.damage_append(user['user_id'], user['nickname'], damage)
    else:
        return False
