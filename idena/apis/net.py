from typing import List

from .. import types
from ..method import method


@method('net_peers')
def get_peers() -> List[types.Peer]: pass

@method('net_addPeer')
def add_peers(url) -> str: pass

@method('net_ipfsAddress')
def get_ipfs_addr() -> str: pass


