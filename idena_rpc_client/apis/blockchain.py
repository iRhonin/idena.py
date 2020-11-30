import decimal
from typing import Optional

from .. import types
from ..method import method


@method('bcn_lastBlock')
def get_last_block() -> types.Block: pass

@method('bcn_blockAt')
def get_block_by_height(height: int) -> types.Block: pass

@method('bcn_block')
def get_block_by_hash(hash: str) -> types.Block: pass

@method('bcn_transaction')
def get_transaction(hash: str) -> types.Transaction: pass

@method('bcn_mempool')
def get_mempool() -> Optional[str]: pass

@method('bcn_syncing')
def check_sync() -> types.Sync: pass

@method('bcn_transactions')
def get_address_transactions(address: str, count: int = 5, token: str = None) -> types.AddressTransactions: pass

@method('bcn_pendingTransactions')
def get_address_pending_transactions(address: str) -> types.AddressTransactions: pass

@method('bcn_burntCoins')
def get_burnt_coins() -> Optional[types.BurntCoins]: pass

@method('bcn_sendRawTx')
def send_raw_tx(tx: str) -> str: pass

@method('bcn_getRawTx')
def get_raw_tx(
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

@method('bcn_feePerByte')
def get_fee_rate() -> decimal.Decimal: pass

@method('bcn_txReceipt')
def get_transaction_receipt(hash: str) -> Optional[types.TxReceipt]: pass


