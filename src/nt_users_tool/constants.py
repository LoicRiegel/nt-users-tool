from lib2to3.pgen2.token import NAME


BLANK = " "
SLASH = "/"

USERNAME = "user_name"
FULL_NAME = "full_name"
EXPIRATION_DATE = "expiration_date"
DICT_INFO_LIST = [USERNAME, FULL_NAME, EXPIRATION_DATE]

SHEET_EXPIRED = "expired_users"
SHEET_EXPIRES_SOON = "expiring_soon_users"
SHEET_ALL_USERS = "all_users"
SHEETS_NAME_LIST = [SHEET_EXPIRED, SHEET_EXPIRES_SOON, SHEET_ALL_USERS]

LAST_RELEVANT_ELEMENT_POSITION = 40

NT_USER_COLUMN = "D"
NAME_COLUMN = "E"
EXPIRATION_DATE_COLUMN = "F"

COLUMNS_LIST = [NT_USER_COLUMN, NAME_COLUMN, EXPIRATION_DATE_COLUMN]

FAKE_NET_COMMAND = "The request will be processed at a domain controller for domain de.bosch.com\
    \n\n\n\nUser name RIL1RT Full Name EXTERNAL Riegel Loic (Technology Strategy, EB-DB/ENG3)\n\
    Comment 208489\nUser's comment 4508629\nCountry/region code (null)\nAccount active Yes\n\
    Account expires 8/1/2023 8:29:59 PM"

FAKE_USER_INFO_LIST = [
    {"user_name": "RIL1RT", "full_name": "RIEGEL LOIC", "expiration_date": "8/1/2023"},
    {
        "user_name": "MOB2RT",
        "full_name": "MOMBRUN ANATOLE",
        "expiration_date": "1/10/2023",
    },
    {
        "user_name": "ADV8RT",
        "full_name": "ADVENTURE TIME",
        "expiration_date": "8/1/2022",
    },
    {
        "user_name": "HAB7RT",
        "full_name": "JOHN DOE",
        "expiration_date": "8/1/2020",
    },
]
