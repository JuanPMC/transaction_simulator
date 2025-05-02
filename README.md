# Transaction processing application
# Introduction
This is a project used for testing different aplications of technology in fintech applications.
## Architecture of repo
This architecture will change from day to day. Might not be fully up to date.
```
project_root/
├── docker-compose.yml
├── .env
├── kafka_commons/                   # Shared Kafka lib (from your zip)
│   └── ...
├── api_gateway/                     # FastAPI app
│   ├── app/
│   │   ├── main.py                  # FastAPI entrypoint
│   │   └── producer.py              # Publishes to Kafka using kafka_commons
│   ├── Dockerfile
│   └── requirements.txt
├── transaction_worker/             # Kafka consumer + Celery worker
│   ├── consumer/
│   │   └── main.py                  # Kafka consumer calls Celery tasks
│   ├── tasks/
│   │   ├── process_transaction.py   # DB insert logic
│   │   └── send_email.py           # Email logic
│   ├── celery_app.py                # Celery config
│   ├── Dockerfile
│   └── requirements.txt
├── ml_ingestor/                     # Second consumer (ML-focused)
│   ├── consumer/
│   │   └── main.py                  # Kafka consumer to ML DB
│   ├── db/
│   │   └── insert.py                # Writes to ML training DB
│   ├── Dockerfile
│   └── requirements.txt
└── common_db/                       # DB init scripts, migrations, etc.
    └── schema.sql
```
```
         [Client/API Request]
                 |
                 v
          [FastAPI Gateway]
                 |
                 v
       [Kafka Topic: transactions]
                 |
         ┌───────┴────────┐
         v                v
[Kafka Consumer]     [Kafka Consumer]
     |                    |
     v                    v
[Celery Task: validate]   [Audit Logger]
     |
     v
[Database Write + Email Notification]
```