import os
from typing import Optional

from .method import method
from .types import AddressTransactions, Block, Sync, Transaction


def init(rpc_node, api_key):
    from . import method
    
    method.RPC_NODE = rpc_node
    method.API_KEY = api_key


@method('bcn_lastBlock')
def get_last_block() -> Block:
    pass

@method('bcn_blockAt')
def get_block_by_height(height: int) -> Block:
    pass

@method('bcn_block')
def get_block_by_hash(hash: str) -> Block:
    pass

@method('bcn_transaction')
def get_transaction(hash: str) -> Transaction:
    pass

@method('bcn_mempool')
def get_mempool() -> Optional[str]:
    pass

@method('bcn_syncing')
def check_sync() -> Sync:
    pass

@method('bcn_transactions')
def get_address_transactions(address: str, count: int = 5, token: str = None) -> AddressTransactions:
    pass

# TODO: this method differ from other single arg methods
# the other methods accept a single item list as para
# but this one need an object
@method('bcn_pendingTransactions')
def get_address_pending_transactions(address: str, _dummy=-1) -> AddressTransactions:
    pass

# TODO: what is resposne shape?
@method('bcn_burntCoins')
def get_burnt_coins() -> Optional[str]:
    pass


