from .apis import \
    account, \
    blockchain, \
    contract, \
    dna, \
    flip, \
    net


def init(rpc_node: str, api_key: str) -> None:
    """Initialization

    Args:
        rpc_node (str): URL of rpc node
        api_key (str): API-Key
    """
    from . import method

    method.RPC_NODE = rpc_node
    method.API_KEY = api_key



