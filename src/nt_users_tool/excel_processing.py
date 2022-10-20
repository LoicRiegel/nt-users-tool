from asyncore import read
from openpyxl import Workbook, load_workbook
from datetime import date

from constants import FAKE_NET_COMMAND, FAKE_NET_COMMAND2, FAKE_NET_COMMAND3, FAKE_NET_COMMAND4, SHEET_ALL_USERS, SHEET_EXPIRED, SHEET_EXPIRES_SOON, SHEETS_NAME_LIST, COLUMNS_LIST, MONTHS_TO_EXPIRE
from net_commands import NTUserInfo, extract_all_nt_user_info
from read_config import read_config_file, get_config


def read_nt_users(worksheet) ->list:
    """Generates a list of nt_user found in the worksheet.

    :param worksheet: The worksheet with nt_users inside.
    :return: A list of nt_user (string).
    """
    nt_user_id_list = []
    for row in worksheet.rows:
        for cell in row:
            if cell.value != None:
                nt_user_id_list.append(cell.value)
    return nt_user_id_list

def create_results_workbook(excel_desired_path: str, sheets_names_list: list):
    """Creates the output excel file according to arguments

    Args:
        excel_desired_path (str): Path where the output file should be located
        sheets_names_list (list): Names of the sheets inside the file
    """
    workbook = Workbook()
    workbook.remove(workbook.active)
    for sheet_name in sheets_names_list:
        workbook.create_sheet(sheet_name)
    workbook.save(excel_desired_path)
    workbook.close()

def fill_one_row(worksheet, row_number: int, columns: list, nt_user_info: NTUserInfo):
    """Fills row_number of columns on the given worksheet, with the info in nt_user_info.

    :param worksheet: The worksheet that needs to be changed.
    :type worksheet: an openpyxl worksheet object.
    :param row_number: the row at which the changes happen.
    :param columns: the range of columns we write on.
    :param user_info: The information that we are writing.
    """
    for i, column in enumerate(columns):
        worksheet[column + str(row_number)] = nt_user_info[i]


def fill_all_sheets(workbook: Workbook, nt_user_info_list: list):
    expired_users_sheet = workbook[SHEET_EXPIRED]
    expiring_soon_users_sheet = workbook[SHEET_EXPIRES_SOON]
    users_sheet = workbook[SHEET_ALL_USERS]

    today = date.today()
    now_month, now_year = today.month, today.year

    all_user_index = 1
    expired_index = 1
    expiring_index = 1

    for user in nt_user_info_list:
        fill_one_row(users_sheet, all_user_index, COLUMNS_LIST, user)
        all_user_index += 1

        user_day, user_month, user_year = user.expiration_date.split("/")
        user_month = int(user_month)
        user_year = int(user_year)
        if user_year < now_year:
            fill_one_row(expired_users_sheet, expired_index, COLUMNS_LIST, user)
            expired_index += 1
        elif user_year == now_year:
            if user_month == now_month:
                fill_one_row(expired_users_sheet, expired_index, COLUMNS_LIST, user)
                expired_index +=1
            elif user_month - now_month <= MONTHS_TO_EXPIRE:
                fill_one_row(expiring_soon_users_sheet, expiring_index, COLUMNS_LIST, user)
                expiring_index +=1

        elif user_year > now_year:
            if now_month > user_month:
                if (user_month - now_month)%12 <= MONTHS_TO_EXPIRE:
                    fill_one_row(expiring_soon_users_sheet, expiring_index, COLUMNS_LIST, user)
                    expiring_index +=1
