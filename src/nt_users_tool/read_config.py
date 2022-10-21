from yaml import safe_load

from nt_users_tool.constants import CONFIG_FILE_PATH, INPUT_FILE

def read_config_file() -> dict:
    """Returns a dictionnary containing all the fields inside the config file.

    :return: Dictionnary with all lines in the config file.
    """
    with open(CONFIG_FILE_PATH,'r') as config_file:
        yaml_stream_dict = safe_load(config_file)
        return yaml_stream_dict

def get_config(config_file_dict: dict) -> str:
    """Returns the file path of the Excel file:\n
    -Input file\n

    :param config_file_dict: Dictionnary with all entries in the file.
    :return: str with the  excel path.
    """
    input = config_file_dict[INPUT_FILE]
    return input