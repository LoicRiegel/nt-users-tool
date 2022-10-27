from typing import List
from openpyxl import Workbook, worksheet
from openpyxl.worksheet.table import Table, TableStyleInfo

from nt_users_tool.constants import COLUMN_WIDTH, TABLE_EXPIRATION_DATE_COLUMN, TABLE_NAME, TABLE_NAME_COLUMN
from nt_users_tool.constants import NUMBER_OF_COLUMNS, SHEET_ALL_USERS, SHEET_EXPIRED, SHEET_EXPIRES_15, TABLE_STYLE
from nt_users_tool.constants import SHEET_EXPIRES_30, SHEET_EXPIRES_60, SHEETS_NAME_LIST, COLUMNS_LIST
from nt_users_tool.constants import NAME_COLUMN, EXPIRATION_DATE_COLUMN, FIRST_COLUMN, NT_USER_COLUMN, TABLE_NT_USER_COLUMN
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
    If they are already present, removes the content of relevant columns to update information.

    :param workbook: The workbook in which to add the sheets.
    """
    for sheet_name in SHEETS_NAME_LIST:
        if sheet_name in workbook.sheetnames:
            old_ws = workbook[sheet_name]
            old_ws.delete_cols(FIRST_COLUMN, NUMBER_OF_COLUMNS)  
        elif sheet_name not in workbook.sheetnames:
            workbook.create_sheet(sheet_name)
            workbook[sheet_name].column_dimensions[NAME_COLUMN].width = COLUMN_WIDTH
            workbook[sheet_name].column_dimensions[NT_USER_COLUMN].width = COLUMN_WIDTH/2 
            workbook[sheet_name].column_dimensions[EXPIRATION_DATE_COLUMN].width = COLUMN_WIDTH


def fill_one_row(worksheet: worksheet, row_number: int, columns: List[str], nt_user_info: NTUserInfo):
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

    all_users_index = 2
    expired_index = 2
    expiring_15_index = 2
    expiring_30_index = 2
    expiring_60_index = 2

    for user in nt_user_info_list:
        fill_one_row(users_sheet, all_users_index, COLUMNS_LIST, user)
        all_users_index += 1
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
    table_range = f"{NAME_COLUMN}1:{EXPIRATION_DATE_COLUMN}{all_users_index-1}"
    create_table_results(users_sheet,table_range)
    

def create_table_results(ws: worksheet, tablerange: str):
    """Creates the table of results inside given worksheet for given tablerange.

    :param ws: The worksheet you want to create the table in.
    :param tablerange: The range of cells that will be in this table.
    """
    ws[f"{NAME_COLUMN}1"] = TABLE_NAME_COLUMN
    ws[f"{NT_USER_COLUMN}1"] = TABLE_NT_USER_COLUMN
    ws[f"{EXPIRATION_DATE_COLUMN}1"] = TABLE_EXPIRATION_DATE_COLUMN
    light_style = TableStyleInfo(name = TABLE_STYLE, showRowStripes= True, showColumnStripes= True)
    if ws.tables:
        del ws.tables[TABLE_NAME]
    table = Table(displayName = TABLE_NAME, ref = tablerange)
    table.tableStyleInfo = light_style
    ws.add_table(table)
