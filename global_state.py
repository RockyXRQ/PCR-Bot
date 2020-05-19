import common.xls_handle as xlsHandle


class GlobalState:
    atking_list = {}
    on_tree_list = []
    save_tree_list = []
    current_boss = 0
    boss_list = [['飞龙', 6000000], ['狂暴格里芬', 8000000], [
        '兽人酋长', 10000000], ['圣灵角鹿', 12000000], ['牛头怪', 20000000]]
    current_day = 1


def team_info_append(user_id: int, user_nickname: str, team_info: str):
    # 如果当前无人救树
    if not GlobalState.save_tree_list:
        # 如果 用户 是第一次申请，则新建他的 sheet
        if user_nickname not in xlsHandle.xls_get_sheets():
            xlsHandle.xls_create_user(user_nickname)

        GlobalState.atking_list[(user_id, user_nickname)] = [
            team_info, GlobalState.current_boss]
        return True
    else:
        return False


def damage_append(user_id: int, user_nickname: str, damage: int):
    key = (user_id, user_nickname)

    # 如果 用户 之前申请过 出刀
    if GlobalState.atking_list.get(key, -1) != -1:

        # 如果用户为 救树者
        if key in GlobalState.save_tree_list:
            # 如果救树成功，则清空全部名单
            if damage > GlobalState.boss_list[GlobalState.atking_list[key][1]][1]:
                GlobalState.save_tree_list.clear()
                GlobalState.on_tree_list.clear()
                GlobalState.atking_list.clear()
            # 若救树失败，则只清空救树名单
            else:
                GlobalState.save_tree_list.clear()

        # 加入伤害记录函数
        xlsHandle.xls_damage_append(
            user_nickname, GlobalState.atking_list[key][0], damage, GlobalState.current_day)

        # 在攻打者名单中去除该用户
        GlobalState.atking_list.pop(key, 0)

        if key in GlobalState.on_tree_list:
            GlobalState.on_tree_list.remove(key)
        return True
    else:
        return False


def on_tree_append(user_id: int, user_nickname: str):
    key = (user_id, user_nickname)

    # 如果用户位于攻打者名单中 且 没有挂树
    if GlobalState.atking_list.get(key, -1) != -1 \
            and key not in GlobalState.on_tree_list:
        # 在救树名单中加入用户
        GlobalState.on_tree_list.append(key)
        # 该用户 救树次数 加1
        xlsHandle.xls_on_tree(key[1])
        return True
    else:
        return False


def save_tree_append(user_id: int, user_nickname: str, team_info: str):
    key = (user_id, user_nickname)

    # 如果挂树名单不为空 且 用户不在挂树名单中 且 用户不在救树名单中
    if GlobalState.on_tree_list \
            and key not in GlobalState.on_tree_list \
            and key not in GlobalState.save_tree_list:

        # 在攻打者名单 和 救树名单中加入用户
        GlobalState.atking_list[key] = [team_info, GlobalState.current_boss]
        GlobalState.save_tree_list.append(key)
        # 该用户 救树次数 加1
        xlsHandle.xls_save_tree(key[1])
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
    # 用来获取只含有名字的列表
    temp_pns = []
    for p in ps:
        temp_pns.append(p[1])
    return temp_pns
