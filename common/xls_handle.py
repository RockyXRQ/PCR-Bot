from openpyxl import load_workbook


class xlsHandle:
    wb = load_workbook(filename='影都第二次公会战数据.xlsx')


def wb_update():
    xlsHandle.wb.save('影都第二次公会战数据.xlsx')
    xlsHandle.wb = load_workbook(filename='影都第二次公会战数据.xlsx')


def xls_create_user(user_nickname: str):
    ws = xlsHandle.wb.copy_worksheet(xlsHandle.wb['Template'])
    ws.title = user_nickname
    ws['B1'] = user_nickname
    wb_update()


def xls_damage_append(user_nickname: str, team_info: str, damage: int, day: int):
    ws = xlsHandle.wb[user_nickname]
    if not ws.cell(4, 2+day):
        ws.cell(4, 2+day).value = team_info
        ws.cell(5, 2+day).value = damage
    elif not ws.cell(6, 2+day):
        ws.cell(6, 2+day).value = team_info
        ws.cell(7, 2+day).value = damage
    else:
        ws.cell(8, 2+day).value = team_info
        ws.cell(9, 2+day).value = damage
    wb_update()


def xls_on_tree(user_nickname: str):
    ws = xlsHandle.wb[user_nickname]
    ws.cell(5, 12).value += 1
    wb_update()


def xls_save_tree(user_nickname: str):
    ws = xlsHandle.wb[user_nickname]
    ws.cell(6, 12).value += 1
    wb_update()

def xls_get_sheets():
    return xlsHandle.wb.sheetnames
