from yaml import safe_load

from constants import CONFIG_FILE_PATH, INPUT_FILE, OUTPUT_FILE

def read_config_file() -> dict:
    """Returns a dictionnary containing all the fields inside the config file.

    :return: Dictionnary with all lines in the config file.
    """
    with open(CONFIG_FILE_PATH,'r') as config_file:
        yaml_stream_dict = safe_load(config_file)
        return yaml_stream_dict

def get_config(config_file_dict: dict) -> tuple:
    """Returns the file paths of the Excel files:\n
    -Input file\n
    -Output file

    :param config_file_dict: Dictionnary with all entries in the file.
    :return: tuple with the two excel paths.
    """
    input = config_file_dict[INPUT_FILE]
    output = config_file_dict[OUTPUT_FILE]
    return (input, output)