from idena_rpc_client import client, method


def test_init():
    rpc_node = 'http://localhost:9009/'
    api_key = 1

    client.init(rpc_node, api_key)
    assert method.API_KEY == api_key
    assert method.RPC_NODE == rpc_node
