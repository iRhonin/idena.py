.. Idena Client documentation master file, created by
   sphinx-quickstart on Wed Dec  2 12:50:15 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Idena Client
============

.. image:: https://travis-ci.com/iRhonin/idena.py.svg?branch=main
    :target: https://travis-ci.com/iRhonin/idena.py

This is Python wrapper for Idene Node.

* Highly inspired by `Web3.py <https://github.com/ethereum/web3.py>`_ and `cookiecutter-pypackage <https://github.com/briggySmalls/cookiecutter-pypackage>`_.

Installation
------------

Idena.py can be installed using ``pip`` as follows:

.. code-block:: shell

   $ pip install idena

For the development, clone the repository then:

.. code-block:: shell

   $ poetry install


Using Idena
-----------

This library depends on a connection to an Idena node and there are 2 ways to configure them. 

Calling `client.init` 
*********************

.. code-block:: python

   >>> from idena import client
   >>> client.init('http://localhost:9009/', 'api-key')


Setting environment variables
*****************************

Set `IDENA_RPC_NODE` and `IDENA_API_KEY` envars:

.. code-block:: sh

   $ export IDENA_RPC_NODE=http://localhost:9009/
   $ export IDENA_API_KEY=api-key

Getting Blockchain Info
-----------------------

.. code-block:: python
   
   >>> client.blockchain.get_last_block()
      
      Block(coinbase='0xbe854231db69ab042073b7ff8309ae3ee265a40f', 
         hash='0xa88e6ab305d7ee311ad2de35338cdbf7e664d860709e5a53f0307baeeaa6f968', 
         parentHash='0xe324a208892241e0294e5a6334965660375dda7a3ad8d8a42a5f3f2ef2857a22', 
         height=2159398, 
         timestamp=1606904853, 
         root='0xd874709bdd4c6fcd95e2e531cc07a4ce42ab23334dfd12ceb45350535b36664c', 
         identityRoot='0x9f3661f19e13d4860f2f2f1610abbbaf86abc8adf1a2781b371189e683745a97', 
         ipfsCid=None, 
         transactions=None, 
         flags=['OfflinePropose'], 
         isEmpty=False, 
         offlineAddress='0x0df427ad7e1906ab4fcc5fd31118932256f5dc7a')