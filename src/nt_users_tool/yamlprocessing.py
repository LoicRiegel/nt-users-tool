import yaml


def output_file_path(config_file_name: str):
    """Returns the filepath of the excel file that will be generated

    Args:
        config_file_name (str): Name of the YAML configuration file

    Returns:
        str: Filepath of the output excel file
    """
    with open(config_file_name, "r") as config_file:
        yaml_stream = yaml.safe_load(config_file)
        file_path = yaml_stream["file_output_path"]
        return file_path


def input_file_path(config_file_name: str):
    """Returns the filepath of the excel file that is used

    Args:
        config_file_name (str): Name of the YAML configuration file

    Returns:
        str: Filepath of the input excel file
    """
    with open(config_file_name, "r") as config_file:
        yaml_stream = yaml.safe_load(config_file)
        file_path = yaml_stream["file_input_path"]
        return file_path