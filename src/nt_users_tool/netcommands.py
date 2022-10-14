import os

from constants import *


def obtain_info_from_user(nt_user_id: str):
    """Generates a dictionnary with relevant user_information from nt_user_id via a net user shell command.

    Args:
        string_input (str): the nt_user_id for which the command will be executed

    Returns:
        dict: The dictionnary containing relevant information about this user
    """
    input = nt_user_id.upper()
    command = 'net user /domain ' + input
    response = os.popen(command)
    string_response = response.read()
    list_response = string_response.split()
    list_of_user_info = list_response[:LAST_RELEVANT_ELEMENT_POSITION]

    dict_user_info = {USERNAME:input}
    
    print(list_of_user_info)
    for (index,element) in enumerate(list_of_user_info):
        if element == 'Name':
            dict_user_info[FULL_NAME] = BLANK.join([list_of_user_info[index+2].upper(),list_of_user_info[index+3]])
        if element == 'expires':
            dict_user_info[EXPIRATION_DATE] = list_of_user_info[index+1]
            break 
    return dict_user_info
