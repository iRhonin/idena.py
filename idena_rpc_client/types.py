import decimal
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Block:
    coinbase:       str
    hash:           str
    parentHash:     str
    height:         int
    timestamp:      int
    root:           str
    identityRoot:   str
    ipfsCid:        str
    transactions:   List[str]
    flags:          List[str]
    isEmpty:        bool
    offlineAddress: str

@dataclass
class Transaction:
    hash:           str
    type:           str
    from_:          str
    to:             Optional[str]
    amount:         str
    tips:           str
    maxFee:         str
    nonce:          int
    epoch:          int
    payload:        str
    blockHash:      str
    usedFee:        str
    timestamp:      int

@dataclass
class Sync:
    syncing:        bool
    currentBlock:   int
    highestBlock:   int
    wrongTime:      bool
    genesisBlock:   int

@dataclass
class AddressTransactions:
    token:          Optional[str]
    transactions:   Optional[List[Transaction]]

@dataclass
class BurntCoins:
    address:        str
    amount:         decimal.Decimal
    key:            str

@dataclass
class BaseTxArgs:
    nonce:          int             = None
    epoch:          int             = None

class TxType:
    SendTx                  = 0
    ActivationTx            = 1
    InviteTx                = 2
    KillTx                  = 3
    SubmitFlipTx            = 4
    SubmitAnswersHashTx     = 5
    SubmitShortAnswersTx    = 6
    SubmitLongAnswersTx     = 7
    EvidenceTx              = 8
    OnlineStatusTx          = 9
    KillInviteeTx           = 10
    ChangeGodAddressTx      = 11
    BurnTx                  = 12
    ChangeProfileTx         = 13

@dataclass
class SendTxArgs(BaseTxArgs):
    from_:          str             = None
    to:             str             = None
    amount:         decimal.Decimal = None
    maxFee:         decimal.Decimal = None
    payload:        str             = None
    tips:           decimal.Decimal = None
    useProto:       bool            = None
    type:           TxType          = TxType.SendTx

@dataclass
class TxEvent:
    eventName: str
    data:      List[bytes]

@dataclass
class TxReceipt:
    contractAddress: str
    success        : bool
    gasUsed        : int
    gasCost        : int
    from_          : str
    txHash         : str
    error          : str
    events         : List[TxEvent]
