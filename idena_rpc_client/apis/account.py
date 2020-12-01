from typing import List

from ..method import method


@method('account_list')
def get_accounts() -> List[str]: pass

@method('account_create')
def create_account(password: None) -> str: pass

@method('account_unlock')
def unlock_account(
    address:    str,
    password:   str = None,
    time:       int = None
) -> None: pass

@method('account_lock')
def lock_account(address: str) -> None: pass


