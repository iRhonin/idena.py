import decimal
from functools import partial
from typing import List

from .. import types
from ..method import method


@method('dna_identity')
def get_identity(address: str) -> types.Identity: pass

@method('dna_identities')
def get_identities() -> List[types.Identity]: pass

@method('dna_state')
def get_current_process() -> types.State: pass

@method('dna_getCoinbaseAddr')
def get_coinbase_address() -> str: pass

@method('dna_getBalance')
def get_balance(address: str) -> types.Balance: pass

@method('dna_sendTransaction')
def send_tx(
    nonce:          int             = None,
    epoch:          int             = None,
    from_:          str             = None,
    to:             str             = None,
    amount:         decimal.Decimal = None,
    maxFee:         decimal.Decimal = None,
    payload:        str             = None,
    tips:           decimal.Decimal = None,
    useProto:       bool            = None,
    type:           types.TxType   = types.TxType.SendTx,
) -> str: pass


@method('dna_sendInvite')
def send_invite(
    nonce:          int             = None,
    epoch:          int             = None,
    to:             str             = None,
    amount:         decimal.Decimal = None,
) -> types.Invite: pass

@method('dna_activateInvite')
def activate_invite(
    nonce:          int             = None,
    epoch:          int             = None,
    key:            str             = None,
) -> types.Invite: pass

kill_identity = partial(send_tx, type=types.TxType.KillTx)

kill_invitee = partial(send_tx, type=types.TxType.KillInviteeTx)

send_dna = partial(send_tx, type=types.TxType.SendTx)

change_god_address = partial(send_tx, type=types.TxType.ChangeGodAddressTx)

@method('dna_becomeOnline')
def become_online(
    nonce:          int             = None,
    epoch:          int             = None,
) -> str: pass

@method('dna_becomeOffline')
def become_offline(
    nonce:          int             = None,
    epoch:          int             = None,
) -> str: pass

@method('dna_epoch')
def get_epoch() -> types.Epoch: pass

@method('dna_ceremonyIntervals')
def get_ceremony_intervals() -> types.CeremonyIntervals: pass

@method('dna_exportKey')
def export_key(password: str) -> str: pass

@method('dna_burn')
def burn(
    nonce:          int             = None,
    epoch:          int             = None,
    from_:          str             = None,
    amount:         decimal.Decimal = None,
    maxFee:         decimal.Decimal = None,
    key:            str             = None,
) -> str: pass

@method('dna_changeProfile')
def change_profile(
    info:           str             = None,
    nickname:       str             = None,
    maxFee:         decimal.Decimal = None,
) -> types.ChangeProfile: pass

@method('dna_profile')
def get_profile(
    address:        str             = None,
) -> types.Profile: pass

@method('dna_activateInviteToRandAddr')
def activate_invite_to_random_address(
    nonce:          int             = None,
    epoch:          int             = None,
    key:            str             = None,
) -> types.ActivateInviteToRandomAddr: pass

@method('dna_isValidationReady')
def isValidationReady() -> bool: pass


