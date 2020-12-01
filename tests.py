from idena_rpc_client import client


client.init('http://51.178.166.157:9009/', '1')
#r = client.blockchain.get_last_block()
#r = client.blockchain.get_block_by_height(2129472)
#r = client.blockchain.get_block_by_hash('0xc32fc04e04b7d1d86116f4f586d2c68bdd00f71203789a810eebb45fa5abf253')
#r = client.blockchain.get_transaction('0xe587a3cda712ae8cd8c1e318cd40acfe07f9d1827675af498166363f4348d91c')
#r = client.blockchain.get_mempool()
#r = client.blockchain.check_sync()
#r = client.blockchain.get_address_transactions('0xa5ba57a22eff691d32f7cca57b13e785463af3e5')
#r = client.blockchain.get_address_pending_transactions('0xa5ba57a22eff691d32f7cca57b13e785463af3e5')
#r = client.blockchain.get_burnt_coins()
#r = client.blockchain.get_raw_tx(
#    from_='0xa5ba57a22eff691d32f7cca57b13e785463af3e5',
#    maxFee=1,
#)
#r = client.dna.get_identity('0xAB6E36f38E0bDAC88e53640c1313C1944A644fcC')
#r = client.dna.get_identities()
#r = client.dna.get_current_process()
#r = client.dna.get_coinbase_address()
#r = client.dna.get_balance('0xAB6E36f38E0bDAC88e53640c1313C1944A644fcC')
#r = client.dna.send_dna(
#    from_='0xa5ba57a22eff691d32f7cca57b13e785463af3e5',
#    to='0xa5ba57a22eff691d32f7cca57b13e785463af3e5',
#    maxFee=1,
#)
#r = client.dna.send_invite(
#    to='0xa5ba57a22eff691d32f7cca57b13e785463af3e5',
#)
#r = client.dna.kill_identity()
#r = client.dna.get_epoch()
#r = client.dna.get_ceremony_intervals()
#r = client.dna.export_key('asdas')
#r = client.dna.change_profile(nickname='rhonin')
#r = client.dna.get_profile('0xa5ba57a22eff691d32f7cca57b13e785463af3e5')
#r= client.dna.activate_invite_to_random_address()
#r = client.dna.isValidationReady()
#r = client.flip.get_raw_flip('123')
#r = client.flip.submit_short_answers(types.FlipAnswers(
#    answers=[
#        types.FlipAnswer('1','2','3',[False]),
#    ],
#))
r = client.net.get_peers()
from pudb import set_trace; set_trace()
#r = client.net.get_ipfs_addr()
print(r)
