from idena_rpc_client import client


client.init('http://51.178.166.157:9009/', '1')
# r = client.get_last_block()
#r = client.get_block_by_height(2129472)
#r = client.get_block_by_hash('0xc32fc04e04b7d1d86116f4f586d2c68bdd00f71203789a810eebb45fa5abf253')
#r = client.get_transaction('0xe587a3cda712ae8cd8c1e318cd40acfe07f9d1827675af498166363f4348d91c')
#r = client.get_mempool()
#r = client.check_sync()
#r = client.get_address_transactions('0xa5ba57a22eff691d32f7cca57b13e785463af3e5')
#r = client.get_address_pending_transactions('0xa5ba57a22eff691d32f7cca57b13e785463af3e5')
r = client.get_burnt_coins()
print(r)