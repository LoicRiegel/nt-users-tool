from typing import List
from openpyxl import Workbook

from nt_users_tool.constants import COLUMN_WIDTH, FIRST_COLUMN, NUMBER_OF_COLUMNS, SHEET_ALL_USERS, SHEET_EXPIRED, SHEET_EXPIRES_15, SHEET_EXPIRES_30, SHEET_EXPIRES_60, SHEETS_NAME_LIST, COLUMNS_LIST, NAME_COLUMN, EXPIRATION_DATE_COLUMN
from nt_users_tool.nt_user_info import NTUserInfo, NTUserStatus, evaluate_user_status

def read_nt_users(worksheet) -> List[str]:
    """Generates a list of nt_user found in the worksheet.

    :param worksheet: The worksheet with nt_users inside.
    :return: A list of nt_user (string).
    """
    nt_user_id_list = []
    for row in worksheet.rows:
        for cell in row:
            if cell.value:
                nt_user_id_list.append(cell.value)
    return nt_user_id_list

def create_results_sheets(workbook: Workbook):
    """Creates the sheets inside the given workbook according to parameter.
    If they are already present, does nothing.

    :param workbook: The workbook in which to add the sheets.
    """
    for sheet_name in SHEETS_NAME_LIST:
        if sheet_name in workbook.sheetnames:
            old_ws = workbook[sheet_name]
            old_ws.delete_cols(FIRST_COLUMN, NUMBER_OF_COLUMNS)  
        if sheet_name not in workbook.sheetnames:
            workbook.create_sheet(sheet_name)
            workbook[sheet_name].column_dimensions[NAME_COLUMN].width = COLUMN_WIDTH 
            workbook[sheet_name].column_dimensions[EXPIRATION_DATE_COLUMN].width = COLUMN_WIDTH


def fill_one_row(worksheet, row_number: int, columns: List[str], nt_user_info: NTUserInfo):
    """Fills row_number of columns on the given worksheet, with the info in nt_user_info.

    :param worksheet: The worksheet that needs to be changed.
    :type worksheet: an openpyxl worksheet object.
    :param row_number: the row at which the changes happen.
    :param columns: the range of columns we write on.
    :param user_info: The information that we are writing.
    """
    for i, column in enumerate(columns):
        worksheet[column + str(row_number)] = nt_user_info[i]


def fill_all_sheets(workbook: Workbook, nt_user_info_list: List[NTUserInfo]):
    """Fills all sheets for the given workbook and nt_user info list (via fill_one_row).

    :param workbook: The workbook which has all sheets to be modified.
    :param nt_user_info_list: The list of NTUserInfo objects containing information.
    """
    expired_users_sheet = workbook[SHEET_EXPIRED]
    expiring_15_users_sheet = workbook[SHEET_EXPIRES_15]
    expiring_30_users_sheet = workbook[SHEET_EXPIRES_30]
    expiring_60_users_sheet = workbook[SHEET_EXPIRES_60]
    users_sheet = workbook[SHEET_ALL_USERS]

    all_user_index = 1
    expired_index = 1
    expiring_15_index = 1
    expiring_30_index = 1
    expiring_60_index = 1

    for user in nt_user_info_list:
        fill_one_row(users_sheet, all_user_index, COLUMNS_LIST, user)
        all_user_index += 1
        user_status = evaluate_user_status(user)
        if user_status == NTUserStatus.EXPIRED:
            fill_one_row(expired_users_sheet, expired_index, COLUMNS_LIST, user)
            expired_index += 1
        elif user_status == NTUserStatus.EXPIRING_15_DAYS:
            fill_one_row(expiring_15_users_sheet, expiring_15_index, COLUMNS_LIST, user)
            expiring_15_index +=1
        elif user_status == NTUserStatus.EXPIRING_30_DAYS:
            fill_one_row(expiring_30_users_sheet, expiring_30_index, COLUMNS_LIST, user)
            expiring_30_index += 1
        elif user_status == NTUserStatus.EXPIRING_60_DAYS:
            fill_one_row(expiring_60_users_sheet, expiring_60_index, COLUMNS_LIST, user)
            expiring_60_index += 1
