
class GlobalState:
    atking_list = {}
    on_tree_list = []
    save_tree_list = []
    team_info_list = []
    current_boss = 0
    boss_list = [['飞龙', 6000000], ['狂暴格里芬', 8000000], [
        '兽人酋长', 10000000], ['圣灵角鹿', 12000000], ['牛头怪', 20000000]]


def team_info_append(user_id: int, user_nickname: str, team_info: str):
    GlobalState.atking_list[(user_id, user_nickname)] = [
        team_info, 0, GlobalState.current_boss]
    return True


def damage_append(user_id: int, user_nickname: str, damage: int):
    if GlobalState.atking_list.get((user_id, user_nickname), -1) != -1:
        GlobalState.atking_list[(
            user_id, user_nickname)][1] = damage
        if (user_id, user_nickname) in GlobalState.save_tree_list:
            GlobalState.save_tree_list.clear()
            GlobalState.on_tree_list.clear()
            GlobalState.atking_list.clear()
        # todo: 等待加入伤害记录函数
        GlobalState.atking_list.pop((user_id, user_nickname), 0)
        if (user_id, user_nickname) in GlobalState.on_tree_list:
            GlobalState.on_tree_list.remove((user_id, user_nickname))
        return True
    else:
        return False


def on_tree_append(user_id: int, user_nickname: str):
    if GlobalState.atking_list.get((user_id, user_nickname), -1) != -1 \
            and GlobalState.atking_list[(user_id, user_nickname)][1] != -2:
        GlobalState.on_tree_list.append((user_id, user_nickname))
        GlobalState.atking_list[(user_id, user_nickname)][1] = -2
        return True
    else:
        return False


def save_tree_append(user_id: int, user_nickname: str, team_info: str):
    if GlobalState.on_tree_list \
            and (user_id, user_nickname) not in GlobalState.on_tree_list \
            and (user_id, user_nickname) not in GlobalState.save_tree_list:
        GlobalState.atking_list[(user_id, user_nickname)] = [
            team_info, 0, GlobalState.current_boss]

        GlobalState.save_tree_list.append((user_id, user_nickname))
        return True
    else:
        return False


def get_current_atking_list():
    return get_names_list(GlobalState.atking_list.keys())


def get_current_on_tree_list():
    return get_names_list(GlobalState.on_tree_list)


def get_current_save_tree_list():
    return get_names_list(GlobalState.save_tree_list)


def get_names_list(ps: list):
    temp_pns = []
    for p in ps:
        temp_pns.append(p[1])
    return temp_pns
