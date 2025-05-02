from fastapi import FastAPI, HTTPException
from kafka import KafkaProducer
import json

app = FastAPI()
producer = KafkaProducer(bootstrap_servers='kafka:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))


@app.post("/transaction")
async def create_transaction(transaction: dict):
    producer.send("transactions", transaction)
    return {"status": "submitted"}
