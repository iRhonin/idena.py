import decimal
from typing import List, Any

from .. import types
from ..method import method


@method('contract_getStake')
def get_stake(contract: str) -> types.Stake: pass

@method('contract_estimateDeploy')
def estimate_deploy(
    from_:      str                     = None,
    codeHash:   str                     = None,
    amount:     decimal.Decimal         = None,
    maxFee:     decimal.Decimal         = None,
    args:       List[types.DynamicArg]  = None,
) -> types.ContractTxReceipt: pass

@method('contract_estimateCall')
def estimate_call(
    from_:          str                     = None,
    contract:       str                     = None,
    method:         str                     = None,
    amount:         decimal.Decimal         = None,
    maxFee:         decimal.Decimal         = None,
    args:           List[types.DynamicArg]  = None,
    broadcastBlock: int                     = None,
) -> types.ContractTxReceipt: pass

@method('contract_estimateTerminate')
def estimate_terminate(
    from_:          str                     = None,
    contract:       str                     = None,
    maxFee:         decimal.Decimal         = None,
    args:           List[types.DynamicArg]  = None,
) -> types.ContractTxReceipt: pass

@method('contract_deploy')
def deploy_contract(
    from_:      str                     = None,
    codeHash:   str                     = None,
    amount:     decimal.Decimal         = None,
    maxFee:     decimal.Decimal         = None,
    args:       List[types.DynamicArg]  = None,
) -> str: pass

@method('contract_call')
def call_contract(
    from_:          str                     = None,
    contract:       str                     = None,
    method:         str                     = None,
    amount:         decimal.Decimal         = None,
    maxFee:         decimal.Decimal         = None,
    args:           List[types.DynamicArg]  = None,
    broadcastBlock: int                     = None,
) -> str: pass

@method('contract_terminate')
def terminate_contract(
    from_:          str                     = None,
    contract:       str                     = None,
    maxFee:         decimal.Decimal         = None,
    args:           List[types.DynamicArg]  = None,
) -> str: pass

@method('contract_readData')
def read_contract_data(
    contract:   str = None,
    key:        str = None,
    format:     str = None,
) -> Any: pass

@method('contract_readonlyCall')
def readonly_call_contract(
    contract:   str                    = None,
    method:     str                    = None,
    format:     str                    = None,
    args:       List[types.DynamicArg] = None,
) -> Any: pass

@method('contract_subscribeToEvent')
def subscribe_to_contract_event(
    contract:   str = None,
    event:      str = None,
) -> None: pass

@method('contract_unsubscribeFromEvent')
def unsubscribe_from_contract_event(
    contract:   str = None,
    event:      str = None,
) -> None: pass

@method('contract_events')
def read_events(
    contract:   str = None,
) -> None: pass


