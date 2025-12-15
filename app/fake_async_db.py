
class FakeAsyncDBSession:
    def __init__(self):
        self.data = []
        self.in_transaction = False

    async def begin(self):
        self.in_transaction = True

    async def insert(self, item):
        if not self.in_transaction:
            raise RuntimeError("No active transaction")
        self.data.append(item)

    async def rollback(self):
        self.data.clear()
        self.in_transaction = False
