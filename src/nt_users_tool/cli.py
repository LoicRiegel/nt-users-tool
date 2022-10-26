from time import perf_counter
from openpyxl import load_workbook
from sys import exit

from nt_users_tool.read_config import read_config_file, get_config
from nt_users_tool.net_commands import extract_all_nt_user_info, get_all_nt_user_string
from nt_users_tool.excel_processing import create_results_sheets, fill_all_sheets, read_nt_users
from nt_users_tool.constants import SHEET_INPUT, CONFIG_FILE_PATH

def main() -> int:
    print("Starting nt_user verification.")
    try:
        dict_conf = read_config_file()
    except FileNotFoundError:
        print(f"Configuration file {CONFIG_FILE_PATH} cannot be found in current directory. Make sure it is present.")
        exit()
    print(f"Opening {CONFIG_FILE_PATH}.")
    input = get_config(dict_conf)
    try:
        wb = load_workbook(input, read_only=False)
    except FileNotFoundError:
        print(f"{input} cannot be found in current directory. Make sure it is present.")
        exit()
    except PermissionError:
        print(f"{input} cannot be opened. Make sure it is not open in another program.")
        exit()
    print(f"Opening {input}.")
    try:
        ws = wb[SHEET_INPUT]
    except KeyError:
        print(f"Could not open the worksheet named {SHEET_INPUT} inside {input}. Make sure the nt users are listed in this sheet.")
        exit()
    print(f"Reading worksheet {SHEET_INPUT}.")
    nt_users_list = read_nt_users(ws)
    print("Gathering information from the network...")
    start = perf_counter()
    net_command_response_list = get_all_nt_user_string(nt_users_list)
    end = perf_counter()
    print(f"Information gathered in {end-start} seconds. Filtering.")
    nt_user_info_list = extract_all_nt_user_info(net_command_response_list)
    print(f"Uploading results to {input}.")
    create_results_sheets(wb)
    fill_all_sheets(wb,nt_user_info_list)
    try:
        wb.save(input)
    except PermissionError:
        print(f"Could not save {input}. Make sure it is not open in another program.")
        exit()
    wb.close()
    print(f"Done. {input} saved with changes.")
    return 0

if __name__ == '__main__':
    main()
