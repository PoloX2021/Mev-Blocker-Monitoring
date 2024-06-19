import json
from decodeRawTx import decode_raw_tx
from datetime import datetime
file_path = "./block19511131.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

d = {}
block_time = datetime.strptime('2024-03-25 11:15:03.241028', "%Y-%m-%d %H:%M:%S.%f")
#for line in lines:
for i in range(len(lines)):
    line = lines[i]
    tem = line.split("\t")
    temp = json.loads(tem[6])
    tx = decode_raw_tx(temp['ExecutionPayload']['transactions'][-1])
    if not(temp['ExecutionPayload']['fee_recipient'] in d.keys()):
        d[temp['ExecutionPayload']['fee_recipient']] = {}

    time = datetime.strptime(tem[1], "%Y-%m-%d %H:%M:%S.%f")
    #time = datetime.timestamp(time)
    if tx['value'] == '0x':
        pass
    else:
        d[temp['ExecutionPayload']['fee_recipient']][time]=(int(tx['value'], 16), i)
    if tem[4] == '0x1bb6ca71aa0157b6a3850b3f9c7584c324ddad60bd77dadbce75c1c41e0f784a':
        print(tx)
        print(temp['ExecutionPayload']['transactions'][-1])
    

    

# Sort the dictionary by value and print
for k in d.keys():
    print(f"### {k}:")
    for key, value in sorted(d[k].items(), key=lambda item: item[1]):
        print(f"        {key}: {value}")
