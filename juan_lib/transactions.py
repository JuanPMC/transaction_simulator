from kafka import KafkaProducer, errors
import json
import time
from pydantic import BaseModel

for _ in range(10):
    try:
        producer = KafkaProducer(bootstrap_servers='kafka:9092')
        break
    except errors.NoBrokersAvailable:
        print("Kafka not ready, retrying...")
        time.sleep(5)


class Transaction(BaseModel):
    id: int
    origin: str
    destiny: str
    amount: str


class TransactionLog():

    TOPIC = "transactions"

    def send_transaction_data(self, transaction: Transaction) -> None:
        producer.send(self.TOPIC, transaction.model_dump_json().encode())
