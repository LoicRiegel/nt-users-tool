CONFIG_FILE_PATH = "./config.yaml"

INPUT_FILE = "input_file_path"

DAYS_EXPIRED_LIMIT = 15
DAYS_EXPIRING_LIMIT = 60

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

FAKE_NET_COMMAND2 = "The request will be processed at a domain controller for domain de.bosch.com\
    \n\n\n\nUser name BRI9RT Full Name EXTERNAL Brice Corentin (TnS, EB-DB/ENG3)\n\
    Comment 208489\nUser's comment 4508568\nCountry/region code (null)\nAccount active Yes\n\
    Account expires 2/1/2023 9:29:59 PM"    

FAKE_NET_COMMAND3 = "The request will be processed at a domain controller for domain de.bosch.com\
    \n\n\n\nUser name MOB2RT Full Name EXTERNAL Mombrun Anatole (TnS, EB-DB/ENG3)\n\
    Comment 208489\nUser's comment 4975140\nCountry/region code (null)\nAccount active Yes\n\
    Account expires 10/1/2023 2:00:00 AM"

FAKE_NET_COMMAND4 = "The request will be processed at a domain controller for domain de.bosch.com\
    \n\n\n\nUser name FET7RT Full Name Fesseler Timo (EB-DB/ENG3)\n\
    Comment 208489\nUser's comment 4975140\nCountry/region code (null)\nAccount active Yes\n\
    Account expires 1/1/2022"

FAKE_NET_COMMAND5 = "The request will be processed at a domain controller for domain de.bosch.com\
    \n\n\n\nUser name FET7RT Full Name John Doe (EB-DB/ENG3)\n\
    Comment 208489\nUser's comment 4975140\nCountry/region code (null)\nAccount active Yes\n\
    Account expires 1/1/2024"