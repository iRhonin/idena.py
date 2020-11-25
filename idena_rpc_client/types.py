from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Block:
    coinbase: str
    hash: str
    parentHash: str
    height: int
    timestamp: int
    root: str
    identityRoot: str
    ipfsCid: str
    transactions: List[str]
    flags: List[str]
    isEmpty: bool
    offlineAddress: str

@dataclass
class Transaction:
    hash: str
    type: str
    from_: str
    to: Optional[str]
    amount: str
    tips: str
    maxFee: str
    nonce: int
    epoch: int
    payload: str
    blockHash: str
    usedFee: str
    timestamp: int

@dataclass
class Sync:
    syncing: bool
    currentBlock: int
    highestBlock: int
    wrongTime: bool
    genesisBlock: int

@dataclass
class AddressTransactions:
    token: Optional[str]
    transactions: Optional[List[Transaction]]
