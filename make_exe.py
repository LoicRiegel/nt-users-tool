import os
import platform
import shutil

import PyInstaller.__main__

""" This programm generate a nt_users_tool.exe file that allows to run the nt_users_toll without running the python project
    You just need to run this file inside the folder src/nt_users_tool folder
"""


def create():
    """Simple program that greets NAME for a total of COUNT times."""

    delimiter = ";" if platform.system() == "Windows" else ":"

    PyInstaller.__main__.run(
        # commad line in a terminal
        # pyinstaller --clean --name  nt_users_tool --onefile -F --add-data "config;config" --icon config\icon.ico cli.py
        [
            "--clean",
            "--name=nt_users_tool",
            "--onefile",
            "-F",
            f"--add-data=config{delimiter}config",
            f"--icon=config{os.sep}icon.ico",
            # "--log-level=DEBUG",
            f".{os.sep}src{os.sep}nt_users_tool{os.sep}cli.py",
        ]
    )
    wash_folders_before_end()


def wash_folders_before_end() -> None:
    """This function remove all unecessary folders from the working sdirectory"""

    try:
        shutil.move(f".{os.sep}dist{os.sep}nt_users_tool.exe", f".{os.sep}nt_users_tool.exe")
    except FileNotFoundError:
        print("File not found : where is nt_users_tool.exe ?")
    # remove unecessary files
    shutil.rmtree(f".{os.sep}build")
    shutil.rmtree(f".{os.sep}dist")
    os.remove(f".{os.sep}nt_users_tool.spec")


if __name__ == "__main__":
    create()
