from .apis import blockchain


def init(rpc_node, api_key):
    from . import method

    method.RPC_NODE = rpc_node
    method.API_KEY = api_key



