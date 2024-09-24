import psycopg2

# Параметри підключення до бази даних
conn = psycopg2.connect(
    dbname='task_management',
    user='postgres',
    password='514474',  
    host='localhost',
    port=5432
)
cursor = conn.cursor()

# Створення таблиці users
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100),
    email VARCHAR(100) UNIQUE
);
""")

# Створення таблиці status
cursor.execute("""
CREATE TABLE IF NOT EXISTS status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE
);
""")

# Вставка початкових статусів
cursor.execute("""
INSERT INTO status (name) VALUES
('new'),
('in progress'),
('completed')
ON CONFLICT (name) DO NOTHING;
""")

# Створення таблиці tasks
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    description TEXT,
    status_id INTEGER REFERENCES status(id),
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);
""")

# Підтвердження змін та закриття з'єднання
conn.commit()
cursor.close()
conn.close()

print("Таблиці успішно створені та ініціалізовані.")
