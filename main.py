import json
import time
from hashlib import sha256


class PyBlock:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash

    def compute_hash(self):

        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()


class PyBlockchain:

    def __init__(self):
        self.chain = []
        self.create_start_block()

    def create_start_block(self):

        start_block = PyBlock(0, [], time.time(), "0")
        start_block.hash = start_block.compute_hash()
        self.chain.append(start_block)

    @property
    def last_block(self):

        return self.chain[-1]


myblockchain = PyBlockchain()

print(PyBlockchain.last_block)
