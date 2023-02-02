from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from subprocess import PIPE, Popen
from typing import List

from progress.bar import Bar

from nt_users_tool.constants import LAST_RELEVANT_ELEMENT_POSITION
from nt_users_tool.nt_user_info import NTUserInfo


def get_nt_user_command_response(nt_user: str) -> str:
    """Returns the result of executing the net user command with a given nt user.

    :param nt_user: The nt_user that will be used in the net command.
    :return: The net user command entire response as a string.
    """
    # For security reasons, make sure that the input is only one word
    nt_user = nt_user.split(" ")[0].upper()
    command = f"net user /domain {nt_user}"
    command_response, err = Popen(command, stdout=PIPE, errors="ignore").communicate()
    # if the user does not exist, we change the command response to display the user name
    if len(command_response) < 100:
        command_response = f"User name       {nt_user}"
    return command_response


def get_all_nt_user_string(list_nt_user: List[str]) -> List[str]:
    """Returns the results of executing the net user command with a given list of nt users.

    :param list_nt_user: The list of nt_user.
    :return: The list of net command reponses.
    """
    command_respones = []
    with Bar("Processing", max=len(list_nt_user)) as bar:
        with ThreadPoolExecutor() as executor:
            future_to_net_response = {
                executor.submit(get_nt_user_command_response, nt_user): nt_user for nt_user in list_nt_user
            }
            for future in as_completed(future_to_net_response):
                command_respones.append(future.result())
                bar.next()  # update the progress bar
    return command_respones


def extract_nt_user_info(net_command_response: str) -> NTUserInfo:
    """Extract relevant data from the nt user command response.

    :param net_command_response: Net command response.
    :return: the extracted nt user information.
    """
    list_response = net_command_response.split()
    list_of_user_info = list_response[:LAST_RELEVANT_ELEMENT_POSITION]

    nt_user = ""
    name = ""
    expiration_date = ""
    for index, element in enumerate(list_of_user_info):
        if element == "name" or element == "Benutzername":
            nt_user = list_of_user_info[index + 1]
        elif element == "Name":
            name = (" ").join([list_of_user_info[index + 2].upper(), list_of_user_info[index + 3]])
        elif element == "expires":
            expiration_date = list_of_user_info[index + 1]
            user_month, user_day, user_year = expiration_date.split("/")
            break
        elif element == "abgelaufen":
            expiration_date = list_of_user_info[index + 1]
            user_day, user_month, user_year = expiration_date.split(".")
            break
    # if the user does not have an expiration date, the user name is ivalid and we return an adapted NTUserInfo
    if expiration_date == "":
        return NTUserInfo(name, nt_user, None)
    else:
        return NTUserInfo(name, nt_user, date(int(user_year), int(user_month), int(user_day)))


def extract_all_nt_user_info(net_command_responses: List[str]) -> List[NTUserInfo]:
    """Extract and returns the nt user information from a list of net command responses.

    :param net_command_responses: responses to different 'net user' commands.
    :return: a list of NTUserInfo containing the nt user info extracted from the different command respones.
    """
    nt_user_infos = []
    for net_command_response in net_command_responses:
        nt_user_infos.append(extract_nt_user_info(net_command_response))
    return nt_user_infos
