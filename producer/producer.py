import json
import time
import random
from datetime import datetime
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

PAGES = ['/', '/home', '/products', '/about', '/contact', '/checkout', '/blog']
ACTIONS = ['page_view', 'click', 'scroll', 'add_to_cart', 'purchase']
USERS = [f'user_{i}' for i in range(1, 21)]

print("🚀 Producer started — sending events to Kafka...")

while True:
    event = {
        'user_id': random.choice(USERS),
        'page': random.choice(PAGES),
        'action': random.choice(ACTIONS),
        'duration_sec': random.randint(5, 300),
        'timestamp': datetime.now().isoformat()
    }
    producer.send('website-events', value=event)
    print(f"Sent: {event}")
    time.sleep(1)