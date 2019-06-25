import hashlib as hasher
import datetime as date


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index).encode('utf-8') + str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') + str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()


def create_genesis_block():
    # Manually construct a block with index zero and arbitrary previous hash
    return Block(0, date.datetime.now(), "Genesis Block", "0")


def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)


def add_blocks(blockchain, num_of_blocks_to_add):
    previous_block = blockchain[-1]
    for i in range(num_of_blocks_to_add):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add


def peek_blockchain(blockchain):
    for block in blockchain:
        print(block.data)
        print(block.hash)


if __name__ == '__main__':
    my_blockchain = [create_genesis_block()]
    num_of_blocks_to_add = 20
    add_blocks(my_blockchain, num_of_blocks_to_add)
    peek_blockchain(my_blockchain)
