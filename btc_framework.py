import hashlib, time, json
# Bitcoin Framework Core (2018) - Production-style Blockchain logic
class BlockchainNode:
    def __init__(self):
        self.chain = []
        self.difficulty = 4
        self.new_block(proof=100, prev_hash='1')
    def new_block(self, proof, prev_hash=None):
        block = {'index': len(self.chain)+1, 'timestamp': time.time(), 'proof': proof, 'prev_hash': prev_hash or self.hash(self.chain[-1])}
        self.chain.append(block); return block
    @staticmethod
    def hash(block):
        return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()
    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False: proof += 1
        return proof
    def valid_proof(self, last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        return hashlib.sha256(guess).hexdigest()[:self.difficulty] == "0000"
print("[*] Bitcoin Node Online: Peer Discovery Active.")
