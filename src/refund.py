from hash import keccak256
from decodeRawTx import decode_raw_tx

def refund(block, transactions):
    data = {}
    """"
    if len(block.transactions)>0:
        print(keccak256(block.transactions[0]))
        print(keccak256(block.transactions[6]))"""
    for i in range(len(block.transactions)):
        if str('0x'+keccak256(block.transactions[i]).lower()) in transactions:
            tx = decode_raw_tx(block.transactions[i+2])

            #Check if backrun is from MEVBlocker
            if tx['from'].lower() == block.builder.lower():
                data[str('0x'+keccak256(block.transactions[i]))] = int(tx['value'],16)
            else:
                data[str('0x'+keccak256(block.transactions[i]))] = 0
    return data
             