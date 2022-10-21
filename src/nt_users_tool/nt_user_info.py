from typing import NamedTuple
from datetime import date
from enum import Enum

from nt_users_tool.constants import DAYS_EXPIRED_LIMIT, DAYS_EXPIRING_LIMIT

class NTUserInfo(NamedTuple):
    """Dataclass for a user of the bosch network.

    :param NamedTuple: Full name, nt_user and expiration date (as datetime.date), fetched from net user /domain.
    """
    full_name: str
    nt_user: str
    expiration_date: date

class NTUserStatus(Enum):
    """Enum for describing possible status of a nt user with regard to its expiration date.

    :param Enum: 3 possibles status : Expired, expiring soon, or valid.
    """
    EXPIRED = "expired"
    EXPIRING_SOON = "expiring_soon"
    VALID = "valid"

DATE_NOW = date.today()

def evaluate_user_status(nt_user_info: NTUserInfo) -> NTUserStatus:
    """Computes the given nt user status with regard to its expiration date.

    :param nt_user_info: The NT User that will be evaluated.
    :return: A NTUserStatus enum to give to the excel processing module.
    """
    days_to_expiration = (nt_user_info.expiration_date - DATE_NOW).days
    print(days_to_expiration)
    if days_to_expiration < DAYS_EXPIRED_LIMIT:
        return NTUserStatus.EXPIRED
    elif DAYS_EXPIRED_LIMIT < days_to_expiration < DAYS_EXPIRING_LIMIT:
        return NTUserStatus.EXPIRING_SOON
    else:
        return NTUserStatus.VALID 
