import psycopg2
from faker import Faker
import random

# Параметри підключення до бази даних
conn = psycopg2.connect(
    dbname='task_management',
    user='postgres',
    password='514474',  
    host='localhost',
    port=5432
)
cursor = conn.cursor()

fake = Faker()
Faker.seed(0)

# Заповнення таблиці users
user_ids = []
for _ in range(10):
    fullname = fake.name()
    email = fake.unique.email()
    cursor.execute(
        "INSERT INTO users (fullname, email) VALUES (%s, %s) RETURNING id;",
        (fullname, email)
    )
    user_id = cursor.fetchone()[0]
    user_ids.append(user_id)

# Отримання списку статусів
cursor.execute("SELECT id FROM status;")
status_ids = [row[0] for row in cursor.fetchall()]

# Заповнення таблиці tasks
for _ in range(50):
    title = fake.sentence(nb_words=6)
    description = fake.text()
    status_id = random.choice(status_ids)
    user_id = random.choice(user_ids)
    cursor.execute(
        "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s);",
        (title, description, status_id, user_id)
    )

# Підтвердження змін та закриття з'єднання
conn.commit()
cursor.close()
conn.close()

print("Таблиці успішно заповнені випадковими даними.")
