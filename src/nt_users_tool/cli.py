from sys import exit
from time import perf_counter

from openpyxl import load_workbook

from nt_users_tool.nt_user_check import check_nt_user
from nt_users_tool.read_config import read_config_file, get_input_file
from nt_users_tool.net_commands import extract_all_nt_user_info, get_all_nt_user_string
from nt_users_tool.excel_processing import create_results_sheets, fill_all_sheets, read_nt_users
from nt_users_tool.constants import SHEET_INPUT, CONFIG_FILE_PATH


def main() -> int:
    """The main functions takes an excel file with a list of nt_users as input.
    It runs the net command /domain for each nt_user and generates multiple sheets to portray the current state of each user.
    It also creates a table on the last sheet to easily sort through.
    Everything is saved on the same input document.

    :return: 1 if the script executed successfully, 1 if an error was raised.
    """
    print("Starting nt_user verification.")

    # Read configuration file
    try:
        dict_conf = read_config_file()
    except FileNotFoundError:
        print(f"Configuration file {CONFIG_FILE_PATH} cannot be found in current directory. Make sure it is present.")
        return 1

    # Parse configuration and open Excel workbook
    print(f"Opening {CONFIG_FILE_PATH}.")
    input = get_input_file(dict_conf)
    try:
        wb = load_workbook(input, read_only=False)
    except FileNotFoundError:
        print(f"{input} cannot be found in current directory. Make sure it is present.")
        return 1
    except PermissionError:
        print(f"{input} cannot be opened. Make sure it is not open in another program.")
        return 1
    print(f"Opening {input}.")

    # Try to read the list of NT users in the input sheet
    try:
        ws = wb[SHEET_INPUT]
    except KeyError:
        print(f"Could not open the worksheet named {SHEET_INPUT} inside {input}. Make sure the nt users are listed in this sheet.")
        return 1

    print(f"Reading worksheet {SHEET_INPUT}.")
    nt_users = read_nt_users(ws)
    for nt_user in nt_users:
        check_nt_user(nt_user)  # Security check

    print("Gathering information from the network...")
    start = perf_counter()
    net_command_responses = get_all_nt_user_string(nt_users)
    end = perf_counter()
    print(f"Information gathered in {end-start:.2f} seconds.")

    print("Filtering.")
    nt_user_info_list = extract_all_nt_user_info(net_command_responses)

    print(f"Write results to {input}.")
    create_results_sheets(wb)
    fill_all_sheets(wb, nt_user_info_list)

    # Save updated Excel workbook
    try:
        wb.save(input)
    except PermissionError:
        print(f"Could not save {input}. Make sure it is not open in another program.")
        return 1

    wb.close()
    print(f"Done. {input} saved with changes.")
    return 0


if __name__ == '__main__':
    exit(main())
