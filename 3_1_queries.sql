-- a. Отримати всі завдання певного користувача (наприклад, user_id = 1)
SELECT * FROM tasks WHERE user_id = 1;

-- b. Вибрати завдання за певним статусом (наприклад, 'new')
SELECT * FROM tasks WHERE status_id = (
    SELECT id FROM status WHERE name = 'new'
);

-- c. Оновити статус конкретного завдання (наприклад, id = 5)
UPDATE tasks SET status_id = (
    SELECT id FROM status WHERE name = 'in progress'
) WHERE id = 5;

-- d. Отримати список користувачів, які не мають жодного завдання
SELECT * FROM users WHERE id NOT IN (
    SELECT DISTINCT user_id FROM tasks
);

-- e. Додати нове завдання для конкретного користувача (наприклад, user_id = 2)
INSERT INTO tasks (title, description, status_id, user_id) VALUES (
    'Нове завдання',
    'Опис нового завдання',
    (SELECT id FROM status WHERE name = 'new'),
    2
);

-- f. Отримати всі завдання, які ще не завершено
SELECT * FROM tasks WHERE status_id != (
    SELECT id FROM status WHERE name = 'completed'
);

-- g. Видалити конкретне завдання (наприклад, id = 10)
DELETE FROM tasks WHERE id = 10;

-- h. Знайти користувачів з певною електронною поштою (наприклад, що містить 'example.com')
SELECT * FROM users WHERE email LIKE '%@example.com';

-- i. Оновити ім'я користувача (наприклад, id = 3)
UPDATE users SET fullname = 'Нове Ім\'я' WHERE id = 3;

-- j. Отримати кількість завдань для кожного статусу
SELECT s.name AS status, COUNT(t.id) AS task_count
FROM status s
LEFT JOIN tasks t ON s.id = t.status_id
GROUP BY s.name;

-- k. Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти (наприклад, '@gmail.com')
SELECT t.*
FROM tasks t
JOIN users u ON t.user_id = u.id
WHERE u.email LIKE '%@gmail.com';

-- l. Отримати список завдань, що не мають опису
SELECT * FROM tasks WHERE description IS NULL OR description = '';

-- m. Вибрати користувачів та їхні завдання, які є у статусі 'in progress'
SELECT u.fullname, t.title, s.name AS status
FROM users u
INNER JOIN tasks t ON u.id = t.user_id
INNER JOIN status s ON t.status_id = s.id
WHERE s.name = 'in progress';

-- n. Отримати користувачів та кількість їхніх завдань
SELECT u.fullname, COUNT(t.id) AS task_count
FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.fullname;
