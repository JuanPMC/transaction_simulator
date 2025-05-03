from juan_lib.transactions import Transaction, TransactionLog
import logging

logger = logging.Logger('data_estracter')


def log_data(transaction: Transaction):
    print(f'Data stored: {transaction.model_dump_json()}')


transaction_log = TransactionLog()
transaction_log.process_data(log_data)
