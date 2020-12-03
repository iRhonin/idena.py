import decimal
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, NamedTuple


class Block(NamedTuple):
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

class Transaction(NamedTuple):
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

class Sync(NamedTuple):
    syncing:        bool
    currentBlock:   int
    highestBlock:   int
    wrongTime:      bool
    genesisBlock:   int

class AddressTransactions(NamedTuple):
    token:          Optional[str]
    transactions:   Optional[List[Transaction]]

class BurntCoins(NamedTuple):
    address:        str
    amount:         decimal.Decimal
    key:            str

class BaseTxArgs(NamedTuple):
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

class SendTxArgs(BaseTxArgs):
    from_:          str             = None
    to:             str             = None
    amount:         decimal.Decimal = None
    maxFee:         decimal.Decimal = None
    payload:        str             = None
    tips:           decimal.Decimal = None
    useProto:       bool            = None
    type:           TxType          = TxType.SendTx

class TxEvent(NamedTuple):
    eventName: str
    data:      List[bytes]

class TxAddr(NamedTuple):
    TxHash:     str
    Address:    str

class TxReceipt(NamedTuple):
    contractAddress: str
    success:         bool
    gasUsed:         int
    gasCost:         int
    from_:           str
    txHash:          str
    error:           str
    events:          List[TxEvent]

class FlipWords(NamedTuple):
    words:  List[int]
    used:   bool
    id:     int

class Identity(NamedTuple):
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

class State(NamedTuple):
    name:   str

class Balance(NamedTuple):
    stake:   decimal.Decimal
    balance: decimal.Decimal
    nonce:   int

class Invite(NamedTuple):
    hash:       str
    receiver:   str
    key:        str

class Epoch(NamedTuple):
    epoch:                  int
    nextValidation:         datetime
    currentPeriod:          str
    currentValidationStart: datetime

class CeremonyIntervals(NamedTuple):
    FlipLotteryDuration:  float
    ShortSessionDuration: float
    LongSessionDuration:  float

class ChangeProfile(NamedTuple):
    txHash: str
    hash:   str

FlipSubmit = ChangeProfile

class Profile(NamedTuple):
    info:       bytes
    nickname:   str

class ActivateInviteToRandomAddr(NamedTuple):
    hash:       str
    address:    str
    key:        str

class FlipHashes(NamedTuple):
    hash:      str
    ready:     bool
    extra:     bool
    available: bool

class Flip(NamedTuple):
    hex:        str
    privateHex: str

class RawFlip(NamedTuple):
    publicHex:  str
    privateHex: str

class Answer(NamedTuple):
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


