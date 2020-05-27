import pcr.common.xls_handle as xlsHandle

import datetime
import json

settings = open('Settings.json', encoding='utf-8')
settings = json.load(settings)


class GlobalState:
    atking_list = {}  # 当前攻打中列表
    on_tree_list = []  # 当前挂树列表
    save_tree_list = []  # 当前救树列表
    current_day = 1  # 当前工会战进行天数
    current_boss = 1  # 当前被攻击Boss位序


def team_info_append(user_id: int, user_nickname: str, team_info: str):
    # 每一次收到申请都做一次时间的检查更新
    GlobalState.current_day = time_update(datetime.datetime(
        settings['START_YEAR'], settings['START_MONTH'], settings['START_DAY'], 5))

    # 如果当前无人救树
    if not GlobalState.save_tree_list:
        # 如果 用户 是第一次申请，则新建他的 sheet
        if user_nickname not in xlsHandle.xls_get_sheets():
            xlsHandle.xls_create_user(user_nickname)
            # sheet 新建 log加入
            log_append('./logs/pcr_log.txt', user_nickname, 'sheet新建')

        GlobalState.atking_list[(user_id, user_nickname)] = [
            team_info, GlobalState.current_boss]

        # 加入攻打者名单 log 加入
        log_append('./logs/pcr_log.txt', user_nickname, '加入攻打者名单')

        return True
    else:
        log_append('./logs/pcr_log.txt', user_nickname, '因有人救树申请失败')
        return False


def damage_append(user_id: int, user_nickname: str, damage: int):

    key = (user_id, user_nickname)
    isKill = False
    damage = int(damage)

    # 如果 用户 之前申请过 出刀
    if GlobalState.atking_list.get(key, -1) != -1 and \
            (not GlobalState.save_tree_list or key in GlobalState.save_tree_list):

        # 如果位于挂树列表中，则去掉其名字
        if key in GlobalState.on_tree_list:
            GlobalState.on_tree_list.remove(key)
            log_append('./logs/pcr_log.txt', user_nickname, '于挂树名单中去除')

        isKill = xlsHandle.xls_damage_append(
            user_nickname,
            GlobalState.atking_list[key][0],
            damage,
            GlobalState.current_day,
            GlobalState.atking_list[key][1]
        )

        GlobalState.current_boss += int(isKill)
        # 如果用户为 救树者
        if key in GlobalState.save_tree_list:
            # 如果救树成功，则清空全部名单
            if isKill:
                GlobalState.save_tree_list.clear()
                GlobalState.on_tree_list.clear()
                GlobalState.atking_list.clear()
            # 若救树失败，则只清空救树名单
            else:
                GlobalState.save_tree_list.clear()

        # 在攻打者名单中去除该用户
        GlobalState.atking_list.pop(key, 0)
        log_append('./logs/pcr_log.txt', user_nickname, '于攻打者名单中除名')
        return True
    else:
        log_append('./logs/pcr_log.txt', user_nickname, '因之前未申请出刀而完成失败')
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
        log_append('./logs/pcr_log.txt', user_nickname, '挂树')
        return True
    else:
        log_append('./logs/pcr_log.txt', user_nickname, '申请挂树失败')
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
        log_append('./logs/pcr_log.txt', user_nickname, '救树')
        return True
    else:
        log_append('./logs/pcr_log.txt', user_nickname, '申请救树失败')
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


def time_update(start_day):
    # 当前日期距离会站开始日期的天数为 current_day
    td = datetime.datetime.now() - start_day
    return int((td.days * 24 + td.seconds/3600 + 1) / 24) + 1


def log_append(filename: str, user_nickname: str, info: str):
    with open(filename, 'a', encoding='utf-8') as log:
        log.write(str(datetime.datetime.now()) +
                  ' [' + user_nickname + '] '+info+'\n')
