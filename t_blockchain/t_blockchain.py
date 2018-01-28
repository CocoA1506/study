class Blockchain(object):
  def __init__(self):
    self.chain = []
    self.current_transactions = []

    # Create the genesis block
    self.new_block(previous_hash=1, proof=100)

  def new_block(self):
    # Creates a new Block and adds it to the chain
    """
    Create a new Block in the Blockchain

    :param proof: <int> The proof given by the Proof of Work algorithm
    :param previous.hash: (Optional) <str> Hash of previous Block
    :return: <dict> New Block
    """"

    block = {
        'index': len(self.chain) + 1,
        'timestamp': time(),
        'transactions': self.current_transactions,
        'proof': proof,
        'previous_hash': previous_hash or self.hash(self.chain[-1]),
    }

    # Reset the current list of current_transactions
    self.current_transactions()

    self.chain.append(block)
    return block

  def new_transaction(self, sender, recipient, amount):
    # Adds a new transaction to list of current_transactions
    """
    Creates a new transaction to go into the next mined Block

    :param sender: <str> Address of the sender
    :param recipient: <str> Address of the recipient
    :param amount: <int> amount
    :return: <int> The index of the Block that will hold this new_transaction
    """

    self.current_transactions.append({
      'sender': sender,
      'recipent': recipient,
      'amount': amount,
    })

    return self.last_block['index'] + 1

  @staticmethod
  def hash(block):
    # Hashes a Block
    pass

  @property
  def last_block(self):
    # Returns the last Block in the chain
    pass
