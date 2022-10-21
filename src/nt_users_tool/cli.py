from openpyxl import Workbook, load_workbook
from sys import exit

from read_config import read_config_file, get_config
from net_commands import extract_all_nt_user_info, get_all_nt_user_string
from excel_processing import create_results_sheets, fill_all_sheets, read_nt_users
from constants import SHEET_INPUT, CONFIG_FILE_PATH

def main() -> int:
    try:
        dict_conf = read_config_file()
    except FileNotFoundError:
        print(f"Configuration file {CONFIG_FILE_PATH} cannot be found in current directory. Make sure it is present.")
    input = get_config(dict_conf)
    try:
        wb = load_workbook(input, read_only=False)
    except FileNotFoundError:
        print(f"{input} cannot be found in current directory. Make sure it is present.")
        exit()
    except PermissionError:
        print(f"{input} cannot be opened. Make sure it is not open in another program.")
        exit()
    try:
        ws = wb[SHEET_INPUT]
    except KeyError:
        print(f"Could not open the worksheet named {SHEET_INPUT}. Make sure the nt users are listed in this sheet.")
    nt_users_list = read_nt_users(ws)
    net_command_response_list = get_all_nt_user_string(nt_users_list)
    nt_user_info_list = extract_all_nt_user_info(net_command_response_list)
    create_results_sheets(wb)
    fill_all_sheets(wb,nt_user_info_list)
    wb.save(input)
    wb.close()
    return 0

if __name__ == '__main__':
    main()