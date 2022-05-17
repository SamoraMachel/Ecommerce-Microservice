from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from kafka import KafkaConsumer, KafkaProducer
import json
import os

# setup the flask application 
def get_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABSE_URL")
    return app

# setup the database
def get_db()-> SQLAlchemy:
    db = SQLAlchemy(get_app())
    return db

# setup kafka consumer 
def kafka_consumer(topic: str) -> KafkaConsumer:
    consumer = KafkaConsumer(
        topic,
        value_deserializer=lambda x : json.loads(x),
        auto_offset_reset='latest',
    )
    return consumer

# setup the kafka producer
def kafka_producer() -> KafkaProducer:
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        compression_type='gzip'
    )
    return producer
    