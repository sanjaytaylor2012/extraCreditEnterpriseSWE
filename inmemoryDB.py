class inmemoryDB:
    def __init__(self):
        self.db = {}
        self.dbCopy = None
        self.transactionInProgress = False
    
    def begin_transaction(self):
        if self.transactionInProgress:
            raise Exception("transaction already in progress")
        self.transactionInProgress = True
        self.dbCopy = self.db.copy()

    def put(self, key, value):
        if not self.transactionInProgress:
            raise Exception("No transaction in progress")
        self.dbCopy[key] = value

    def get(self, key):
        return self.db.get(key, None)
    
    def commit(self):
        if not self.transactionInProgress:
            raise Exception("No transaction in progress")
        self.db = self.dbCopy.copy()
        self.dbCopy = None
        self.transactionInProgress = False
    
    def rollback(self):
        if not self.transactionInProgress:
            raise Exception("No transaction in progress")
        self.dbCopy = None
        self.transactionInProgress = False


