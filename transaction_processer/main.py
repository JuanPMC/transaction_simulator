from juan_lib.transactions import Transaction, TransactionLog
import logging


def log_data(transaction: Transaction):
    print(f'Transaction processed: {transaction.model_dump_json()}')


transaction_log = TransactionLog()
transaction_log.process_data(log_data)
