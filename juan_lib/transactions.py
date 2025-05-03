from kafka import KafkaProducer, errors, KafkaConsumer
import json
import time
from pydantic import BaseModel

for _ in range(10):
    try:
        producer = KafkaProducer(bootstrap_servers='kafka:9092')
        consumer = KafkaConsumer(
            'transactions', bootstrap_servers='kafka:9092', value_deserializer=lambda m: json.loads(m.decode('utf-8')))
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

    def process_data(self, handler: callable) -> None:
        for consumer_record in consumer:
            transaction_data = consumer_record.value

            transaction_id = transaction_data.get('id')
            origin = transaction_data.get('origin')
            destiny = transaction_data.get('destiny')
            amount = transaction_data.get('amount')

            transaction = Transaction(
                id=transaction_id, origin=origin, destiny=destiny, amount=amount)

            handler(transaction)
