from nt_users_tool.constants import (
    NT_USER_MAX_LEN,
)


class InvalidUserNameError(Exception):
    """Raised for invalid NT user names."""

    def __init__(self, user_name) -> None:
        self.user_name = user_name
    
    def __str__(self) -> str:
        return f"{self.user_name} is not valid!"


def check_nt_user(nt_user:str) -> None:
    """Check the validity of a user name.
    
    :param user_name: user name to check
    :raises : if the given user name is invalid.
    """
    # Check that the length of the user name
    if len(nt_user) > NT_USER_MAX_LEN:
        raise IndentationError(nt_user)
