from src.ProductMicroservice.app import get_app, get_db, kafka_consumer, kafka_producer
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from kafka import KafkaConsumer, KafkaProducer

def test_get_app():
    assert type(get_app()) == Flask

def test_get_db():
    assert type(get_db()) == SQLAlchemy
    
def test_kafka_consumer():
    assert type(kafka_consumer('test')) == KafkaConsumer
    
def test_kafka_producer():
    assert type(kafka_producer()) == KafkaProducer