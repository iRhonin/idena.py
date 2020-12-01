import decimal
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, NamedTuple


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
class TxAddr:
    TxHash:     str
    Address:    str

@dataclass
class TxReceipt:
    contractAddress: str
    success:         bool
    gasUsed:         int
    gasCost:         int
    from_:           str
    txHash:          str
    error:           str
    events:          List[TxEvent]

@dataclass
class FlipWords:
    words:  List[int]
    used:   bool
    id:     int

@dataclass
class Identity:
    address:                str
    profileHash:            str
    stake:                  decimal.Decimal
    invites:                int
    age:                    int
    state:                  str
    pubkey:                 str
    requiredFlips:          int
    availableFlips:         int
    flipKeyWordPairs:       Optional[List[FlipWords]]
    madeFlips:              int
    totalQualifiedFlips:    int
    totalShortFlipPoints:   float
    flips:                  Optional[List[str]]
    online:                 bool
    generation:             int
    code:                   bytes
    invitees:               Optional[List[TxAddr]]
    penalty:                decimal.Decimal
    lastValidationFlags:    Optional[List[str]]

@dataclass
class State:
    name:   str

@dataclass
class Balance:
    stake:   decimal.Decimal
    balance: decimal.Decimal
    nonce:   int

@dataclass
class Invite:
    hash:       str
    receiver:   str
    key:        str

@dataclass
class Epoch:
    epoch:                  int
    nextValidation:         datetime
    currentPeriod:          str
    currentValidationStart: datetime

@dataclass
class CeremonyIntervals:
    FlipLotteryDuration:  float
    ShortSessionDuration: float
    LongSessionDuration:  float

@dataclass
class ChangeProfile:
    txHash: str
    hash:   str

FlipSubmit = ChangeProfile

@dataclass
class Profile:
    info:       bytes
    nickname:   str

@dataclass
class ActivateInviteToRandomAddr:
    hash:       str
    address:    str
    key:        str

@dataclass
class FlipHashes:
    hash:      str
    ready:     bool
    extra:     bool
    available: bool

@dataclass
class Flip:
    hex:        str
    privateHex: str

@dataclass
class RawFlip:
    publicHex:  str
    privateHex: str

@dataclass
class Answer:
    none  = '0'
    left  = '1'
    right = '2'

class Grade:
    gradeNone      = '0'
    gradeReported  = '1'
    gradeD         = '2'
    gradeC         = '3'
    gradeB         = '4'
    gradeA         = '5'

class FlipAnswer(NamedTuple):
    hash:       str
    grade:      Grade
    answer:     Answer
    wrongWords: List[bool]

class FlipAnswers(NamedTuple):
    answers:  List[FlipAnswer]

class Peer(NamedTuple):
    id:     str
    addr:   str

class Stake(NamedTuple):
    Hash: str
    Stake: decimal.Decimal

class DynamicArg(NamedTuple):
    index:  int
    format: str
    value:  str

class ContractTxReceipt:
    contract:   str
    success:    bool
    gasUsed:    int
    gasCost:    decimal.Decimal
    txHash:     str
    txFee:      decimal.Decimal
    error:      str


