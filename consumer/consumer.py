import json
import psycopg2
from kafka import KafkaConsumer
from datetime import datetime

# PostgreSQL connection (Docker PostgreSQL)
conn = psycopg2.connect(
    host="localhost",
    port=5433,
    database="website_tracking",
    user="postgres",
    password="postgres"
)
cursor = conn.cursor()

# Kafka consumer
consumer = KafkaConsumer(
    'website-events',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id='website-tracking-group'
)

print("🔥 Consumer started — reading from Kafka and writing to PostgreSQL...")

for message in consumer:
    event = message.value
    try:
        cursor.execute("""
            INSERT INTO user_events 
                (user_id, page, action, duration_sec, event_timestamp)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            event['user_id'],
            event['page'],
            event['action'],
            event['duration_sec'],
            datetime.fromisoformat(event['timestamp'])
        ))
        conn.commit()
        print(f"✅ Saved: {event['user_id']} → {event['page']} ({event['action']})")
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.rollback()