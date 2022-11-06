from typing import NamedTuple
from datetime import date
from enum import Enum

from nt_users_tool.constants import (
    NT_USER_MAX_LEN,
    DAYS_EXPIRED_LIMIT,
    DAYS_EXPIRING_15_LIMIT,
    DAYS_EXPIRING_30_LIMIT,
    DAYS_EXPIRING_60_LIMIT;
)

_DATE_NOW = date.today()


class InvalidUserNameError(Exception):
    """Raised for invalid NT user names."""

    def __init__(self, user_name) -> None:
        self.user_name = user_name
    
    def __str__(self) -> str:
        return f"{self.user_name} is not valid!"


class NTUserInfo(NamedTuple):
    """Dataclass for a user of the network.

    :param NamedTuple: Full name, nt_user and expiration date (as datetime.date), fetched from net user /domain.
    """
    full_name: str
    nt_user: str
    expiration_date: date


class NTUserStatus(Enum):
    """Possible status of an NT user depending on its expiration date."""

    EXPIRED = "expired"
    EXPIRING_15_DAYS = "expiring 15 days"
    EXPIRING_30_DAYS = "expiring 30 days"
    EXPIRING_60_DAYS = "expiring 60 days"
    VALID = "valid"


def evaluate_user_status(nt_user_info: NTUserInfo) -> NTUserStatus:
    """Computes the given nt user status with regard to its expiration date.

    :param nt_user_info: The NT User that will be evaluated.
    :return: A NTUserStatus enum to give to the excel processing module.
    """
    days_to_expiration = (nt_user_info.expiration_date - _DATE_NOW).days
    if days_to_expiration <= DAYS_EXPIRED_LIMIT:
        return NTUserStatus.EXPIRED
    elif DAYS_EXPIRED_LIMIT < days_to_expiration <= DAYS_EXPIRING_15_LIMIT:
        return NTUserStatus.EXPIRING_15_DAYS
    elif DAYS_EXPIRING_15_LIMIT < days_to_expiration <= DAYS_EXPIRING_30_LIMIT:
        return NTUserStatus.EXPIRING_30_DAYS   
    elif DAYS_EXPIRING_30_LIMIT < days_to_expiration <= DAYS_EXPIRING_60_LIMIT:
        return NTUserStatus.EXPIRING_60_DAYS
    else:
        return NTUserStatus.VALID 


def check_nt_user(nt_user:str) -> None:
    """Check the validity of a user name.
    
    :param user_name: user name to check
    :raises : if the given user name is invalid.
    """
    # Check that the length of the user name
    if len(nt_user) > NT_USER_MAX_LEN:
        raise IndentationError(nt_user)
