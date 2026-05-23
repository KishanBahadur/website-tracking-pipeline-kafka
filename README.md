# 🚀 Real-Time Website Tracking Pipeline

A production-grade real-time data engineering pipeline built with Apache Kafka, Python, PostgreSQL, and Matplotlib.

## 🏗️ Architecture
Website Events → Kafka Producer → Kafka Topic → Kafka Consumer → PostgreSQL → Live Dashboard

## 📋 Prerequisites
Before running this pipeline, ensure you have the following installed on your local system:
* **Docker & Docker Compose** (To run Kafka, Zookeeper, and PostgreSQL)
* **Python 3.8+**
* Required Python libraries: `pip install kafka-python psycopg2-binary matplotlib`

## 🛠️ Tech Stack
| Tool | Purpose |
|------|---------|
| Apache Kafka | Real-time event streaming |
| Apache Zookeeper | Kafka cluster coordination |
| PostgreSQL | Event storage |
| Python | Pipeline scripting |
| Matplotlib | Live dashboard |
| Docker | Container orchestration |

## 🗄️ Database Schema
The Kafka Consumer automatically creates and populates the `website_events` table in PostgreSQL with this structure:

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| id          | SERIAL    | Primary Key |
| user_id     | VARCHAR   | Unique ID of the visitor |
| action      | VARCHAR   | User action (click, view, login, logout) |
| page        | VARCHAR   | Website page URL visited |
| timestamp   | TIMESTAMP | Exact time of the event |

## 📁 Project Structure
```text
├── producer/producer.py     # Generates & sends events to Kafka
├── consumer/consumer.py     # Reads Kafka events → saves to PostgreSQL
├── dashboard/dashboard.py   # Live auto-refreshing Matplotlib dashboard
└── docker-compose.yml       # Spins up Kafka, Zookeeper, and PostgreSQL



## ⚡ How to Run
```bash
# Start all containers (Kafka, Zookeeper, Postgres)
docker-compose up -d

# Terminal 1 - Start producer to generate live events
python producer/producer.py

# Terminal 2 - Start consumer to save events to Database
python consumer/consumer.py

# Terminal 3 - Start live dashboard
python dashboard/dashboard.py

```

## 📊 Dashboard Features

* **Events per page** (Bar chart)
* **Action breakdown** (Pie chart)
* **Top 10 active users** (Bar chart)
* **Events over time** (Line chart)
* **Auto-refreshes** every 3 seconds

## 👤 Author

**Kishan Bahadur** | Data Engineer | kishanbahadurshahi@gmail.com

```

