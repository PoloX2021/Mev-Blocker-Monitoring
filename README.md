# Mev-Blocker-Monitoring
This project contains a few scripts to fiilter the information on the blocks proposed by the builders

THe file main aggregates most of them. It uses these files:
 - bestBid : to find the block used in the auction. You need to specifiy an ETHERSCAN_API_KEY
 - decodeRawTX : to decode transactions, by using cast from foundry. **You will need to install it and specify its address in the code**
 - hash : to define the hash function of the EVM
 - MEVBlockerTx : to get all the transactions from MEVBlocker for a specific block. You wil need to add your DUNE_API_KEY to a .env file
 - refund to analyse if transactions from MEVBlocker received a refund

table_header presents the header of the file table to show the structure of the database

Finally df_experiment.py performs a few test on a db to implement to store the useful data for the monitoring.

Packages needed :
 - dune-client 1.7.3
 - pycryptodome 3.20.0
 - web3 6.16.0

 - requests 2.31.0
 - pandas 2.2.1
 - python-dotenv 1.0.1
 - requests 2.31.0

In https://www.notion.so/cownation/MEV-Blocker-Monitoring-9426ee379caf4d50b4688b5790082a86 You will find more explanation of our The proposer builder separation is deployed and how mev blocker works.

At https://drive.google.com/drive/folders/15zqZwGi_zEQarMQPdczK4pQ9nz8mHbvH?usp=sharing there is an example of the sets of blocks received by Agnostic Relay from block 19511131 to 195111163. This data gives an example of how the blocks are filtered. However, the sample is not very relvant for rebates.