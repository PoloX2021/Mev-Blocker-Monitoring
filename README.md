# Mev-Blocker-Monitoring
This project contains a few scripts to fiilter the information on the blocks proposed by the builders

THe file main aggregates most of them. It uses these files:
 - bestBid : to find the block used in the auction. You need to specifiy an ETHERSCAN_API_KEY
 - decodeRawTX : to decode transactions, by using cast from foundry. You will need to install it and specify its address in the code
 - hash : to define the hash function of the EVM
 - MEVBlockerTx : to get all the transactions from MEVBlocker for a specific block. You wil need to add your DUNE_API_KEY to a .env file
 - refund to analyse if transactions from MEVBlocker received a refund


table_header presents the header of the file table to show the structure of the database

Finally df_experiment.py performs a few test on a db to implement to store the useful data for the monitoring.

In https://www.notion.so/cownation/MEV-Blocker-Monitoring-9426ee379caf4d50b4688b5790082a86 You will find more explanation of our The proposer builder separation is deployed and how mev blocker works.