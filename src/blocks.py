import json
from decodeRawTx import decode_raw_tx
from datetime import datetime

class Block:
    def __init__(self, _number, _builder, _transactions, _bid, _time, _hash, _block_number):
        self.number = _number
        self.builder = _builder
        self.transactions = _transactions
        self.bid = _bid
        self.time = _time
        self.hash = _hash
        self.block_number = int(_block_number)
    
    @classmethod
    def from_string(cls, block_string, _number):
        temp = block_string.split('\t')
        _hash = temp[4]
        _time = datetime.strptime(temp[1], "%Y-%m-%d %H:%M:%S.%f")
        temp = json.loads(temp[6])
        _builder = temp['ExecutionPayload']['fee_recipient'].lower()
        _transactions = temp['ExecutionPayload']['transactions']
        _block_number = temp['ExecutionPayload']['block_number']
        """for i in range(len(_transactions)):
            _transactions[i] = decode_raw_tx(_transactions[i])"""
        _bid = decode_raw_tx(_transactions[-1])['value']

        return cls(_number, _builder, _transactions, _bid, _time, _hash, _block_number)