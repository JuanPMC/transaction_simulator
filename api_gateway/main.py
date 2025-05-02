from fastapi import FastAPI
from juan_lib.transactions import TransactionLog, Transaction

app = FastAPI()


@app.post("/transaction")
async def create_transaction(transaction: Transaction):
    transaction_log = TransactionLog()
    transaction_log.send_transaction_data(transaction)
    return {"status": "submitted"}
