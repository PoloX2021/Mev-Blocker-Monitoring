import json
from decodeRawTx import decode_raw_tx
from datetime import datetime

def recent_blocks(lines, block_time):
    data = {}
    for i in range(len(lines)):
        line = lines[i]
        temp = line.split("\t")
        time = datetime.strptime(temp[1], "%Y-%m-%d %H:%M:%S.%f")
        temp = json.loads(temp[6])
        block_builder = temp['ExecutionPayload']['fee_recipient']
        tx = decode_raw_tx(temp['ExecutionPayload']['transactions'][-1])
        if tx['value'] == '0x':
            pass
        elif not(block_builder in data.keys()):
            data[block_builder] = (int(tx['value'], 16), i, time)
        else:
            #if abs(time-block_time)<abs(data[block_builder][2]-block_time):
            if block_time>=time>data[block_builder][2]:
                data[block_builder] = (int(tx['value'], 16), i, time)
    return data

file_path = "./block19511131.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

data = recent_blocks(lines, datetime.strptime('2024-03-25 11:15:03.241028', "%Y-%m-%d %H:%M:%S.%f"))

for key, value in sorted(data.items(), key=lambda item: item[1][0]):
        print(f"{key}: {value}")