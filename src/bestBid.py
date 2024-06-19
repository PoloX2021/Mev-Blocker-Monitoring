import os
from dotenv import load_dotenv
from requests import get
load_dotenv()

def best_bid(blocks):
    api_key=os.getenv("ETHERSCAN_API_KEY")
    hex_block_number = hex(blocks[0].block_number)
    url = f"https://api.etherscan.io/api?module=proxy&action=eth_getBlockByNumber&tag={hex_block_number}&boolean=true&apikey={api_key}"
    hash = get(url).json()['result']['hash']
    time = 0
    for block in blocks:
        if block.hash == hash:
            time = block.time
            break
        
    if time == 0:
        print("Not Agnostic Relay")
        return {}

    data = {}
    for block in blocks:
        if not(block.builder in data.keys()):
            data[block.builder] = block
        else:
            if abs(block.time-time)<abs(data[block.builder].time-time):
                #maybe filter with blocks that are came before the solution settled (maybe a bit fairer for the builder)
                data[block.builder] = block
    return data