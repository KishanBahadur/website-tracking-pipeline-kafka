import psycopg2
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import Counter

conn = psycopg2.connect(
    host="localhost", port=5433,
    database="website_tracking",
    user="postgres", password="postgres"
)

fig, axes = plt.subplots(2, 2, figsize=(14, 8))
fig.suptitle("Real-Time Website Tracking Dashboard", fontsize=16, fontweight='bold')

def update(frame):
    cursor = conn.cursor()
    for ax in axes.flat:
        ax.clear()

    # Chart 1 - Events per page
    cursor.execute("SELECT page, COUNT(*) FROM user_events GROUP BY page ORDER BY COUNT(*) DESC")
    data = cursor.fetchall()
    if data:
        pages, counts = zip(*data)
        axes[0,0].barh(pages, counts, color='steelblue')
        axes[0,0].set_title('Events per Page')
        axes[0,0].set_xlabel('Count')

    # Chart 2 - Action breakdown
    cursor.execute("SELECT action, COUNT(*) FROM user_events GROUP BY action")
    data = cursor.fetchall()
    if data:
        actions, counts = zip(*data)
        axes[0,1].pie(counts, labels=actions, autopct='%1.1f%%', startangle=90)
        axes[0,1].set_title('Action Breakdown')

    # Chart 3 - Top 10 active users
    cursor.execute("SELECT user_id, COUNT(*) FROM user_events GROUP BY user_id ORDER BY COUNT(*) DESC LIMIT 10")
    data = cursor.fetchall()
    if data:
        users, counts = zip(*data)
        axes[1,0].bar(users, counts, color='coral')
        axes[1,0].set_title('Top 10 Active Users')
        axes[1,0].tick_params(axis='x', rotation=45)

    # Chart 4 - Events over time
    cursor.execute("SELECT DATE_TRUNC('minute', event_timestamp), COUNT(*) FROM user_events GROUP BY 1 ORDER BY 1")
    data = cursor.fetchall()
    if data:
        times, counts = zip(*data)
        axes[1,1].plot(times, counts, marker='o', color='green')
        axes[1,1].set_title('Events Over Time')
        axes[1,1].tick_params(axis='x', rotation=45)

    cursor.close()
    plt.tight_layout()

ani = animation.FuncAnimation(fig, update, interval=3000)
plt.show()