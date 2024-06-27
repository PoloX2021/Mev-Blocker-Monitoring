from blocks import Block
from bestBid import best_bid
from mevBlockerTx import get_tx
from refund import refund
import logging
logging.getLogger().setLevel(logging.ERROR)

#Prepare the data : the blocks to work on
#600 blocks ~ 180' The delay is mainly due to the inefficient querying of the files
for block_number in range(19511131, 19511164):
    try:
        file_path = f"./{block_number}.txt"
        with open(file_path, "r") as file:
            lines = file.readlines()

        blocks = []
        #for i in range(len(lines)):
        for i in range(len(lines)):
            blocks.append(Block.from_string(lines[i], i))
        print(" ")
        print(" ")
        print("###")
        print(block_number)
        print(len(blocks))
        #filters only the blocks proposed cloest to the right time
        blocks = best_bid(blocks)
        print(len(blocks))

        #The list of builders which subscribed to the MEV-Blocker
        builders = ['0x95222290DD7278Aa3Ddd389Cc1E1d165CC4BAfe5'.lower(), #beaver
                    '0x4838b106fce9647bdf1e7877bf73ce8b0bad5f97'.lower(), #titan
                    '0xdafea492d9c6733ae3d56b7ed1adb60692c98bc5'.lower(), #flashbots
                    '0xf15689636571dba322b48e9ec9ba6cfb3df818e1'.lower()  #penguin
                    ]

        #The blocks proposed by the builders
        #fill the empty blocks with the default block
        builder_blocks = {}
        for b in builders:
            if not(b in blocks.keys()):
                blocks[b] = Block(-1, b, [], 0, 0, '0x00', block_number)
            builder_blocks[b] = blocks[b]

        

        txs = get_tx(block_number)
        #txs = ['0xab6f9b2c014a993d19f11038f43329a0e5d658fffd35f179c67304460e43230c']
        
        print(' ')
        for builder in builders:
            print(f"*{builder}, {builder_blocks[builder].time}")
            print(refund(builder_blocks[builder], txs))
            print(builder_blocks[builder].hash)
    
    except Exception as e:
        print(e)

    

