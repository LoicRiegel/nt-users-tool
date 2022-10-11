from enum import Enum, IntEnum

DEFAULT_INPUT_FILE = "./nt_users_name.xlsx"


class DaysExpiring(IntEnum):
    DAYS_EXPIRED_LIMIT = 0
    DAYS_EXPIRING_15_LIMIT = 15
    DAYS_EXPIRING_30_LIMIT = 30
    DAYS_EXPIRING_60_LIMIT = 60


SHEET_INPUT = "nt_users"


class Sheets(str, Enum):
    SHEET_EXPIRED = "expired_users"
    SHEET_EXPIRES_15 = "expiring_15_users"
    SHEET_EXPIRES_30 = "expiring_30_users"
    SHEET_EXPIRES_60 = "expiring_60_users"
    SHEET_ERROR_NAME_USER = "error_name_user"
    SHEET_ALL_USERS = "all_users"


SHEETS_NAME_LIST = [
    Sheets.SHEET_EXPIRED.value,
    Sheets.SHEET_EXPIRES_15.value,
    Sheets.SHEET_EXPIRES_30.value,
    Sheets.SHEET_EXPIRES_60.value,
    Sheets.SHEET_ERROR_NAME_USER.value,
    Sheets.SHEET_ALL_USERS.value,
]

# print(SHEETS_NAME_LIST)

LAST_RELEVANT_ELEMENT_POSITION = 40


# TO DO : 3.11 use ReprEnum
class SheetSettingsInt(IntEnum):
    FIRST_COLUMN = 4
    NUMBER_OF_COLUMNS = 3
    COLUMN_WIDTH = 30


class SheetSettingsStr(str, Enum):
    NAME_COLUMN = "D"
    NT_USER_COLUMN = "E"
    EXPIRATION_DATE_COLUMN = "F"


COLUMNS_LIST = [
    SheetSettingsStr.NAME_COLUMN.value,
    SheetSettingsStr.NT_USER_COLUMN.value,
    SheetSettingsStr.EXPIRATION_DATE_COLUMN.value,
]


class Tables(str, Enum):
    TABLE_STYLE = "TableStyleLight13"
    TABLE_NAME = "nt_users_table"
    TABLE_NAME_COLUMN = "Name"
    TABLE_NT_USER_COLUMN = "NT_User"
    TABLE_EXPIRATION_DATE_COLUMN = "Expiration Date"
