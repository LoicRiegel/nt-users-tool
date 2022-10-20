from os import popen
from concurrent.futures import Executor, ThreadPoolExecutor

from typing import NamedTuple

from constants import LAST_RELEVANT_ELEMENT_POSITION

class NTUserInfo(NamedTuple):
    """Dataclass for a user of the bosch network

    :param NamedTuple: Full name, nt_user and expiration date (fetched from net user /domain)
    """
    full_name: str
    nt_user: str
    expiration_date: str

def get_nt_user_string(nt_user: str) -> str:
    """Executes a net command with given nt_user and returns the response as a string.

    :param nt_user: The nt_user that will be used in the net command.
    :return: The response as a string.
    """
    input = nt_user.upper()
    command = (f"net user /domain {input}")
    response = popen(command)
    string_response = response.read()
    return string_response

def get_all_nt_user_string(list_nt_user: list) -> list:
    """Performs get_nt_user_string on all elements of list_nt_user.

    :param list_nt_user: The list of nt_user.
    :return: The list of net command reponse to all elements of list_nt_user.
    """
    list_of_nt_user_string = []
    for nt_user in list_nt_user:
        list_of_nt_user_string.append(get_nt_user_string(nt_user))
    return list_of_nt_user_string

def extract_nt_user_info(nt_user_string: str) -> NTUserInfo:
    """Extracts relevant data from a string generated with a given nt_user.

    :param nt_user_string: Net command response as a string with given nt_user. 
    :return: NTUserInfo (NamedTuple) with name, nt_user and expiration date.
    """
    list_response = nt_user_string.split()
    list_of_user_info = list_response[:LAST_RELEVANT_ELEMENT_POSITION]

    nt_user = ""
    name = ""
    expiration_date = ""

    for (index,element) in enumerate(list_of_user_info):
        if element == 'name':
            nt_user = list_of_user_info[index+1]
        elif element == 'Name':
            name = (" ").join([list_of_user_info[index+2].upper(),list_of_user_info[index+3]])
        elif element == 'expires':
            expiration_date = list_of_user_info[index+1]
            break 
    return NTUserInfo(name,nt_user,expiration_date)

def extract_all_nt_user_info(list_nt_user_string: list) -> list:
    """Performs extract_nt_user_info on all elements of list_nt_user_string.

    :param list_nt_user_string: List of strings that are responses to net commands with nt_users.
    :return: A list of NTUserInfo objects, one for each nt_user in list_nt_user_string.
    """
    list_of_nt_user_info = []
    for nt_user_string in list_nt_user_string:
        list_of_nt_user_info.append(extract_nt_user_info(nt_user_string))
    return list_of_nt_user_info