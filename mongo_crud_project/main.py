from pymongo import MongoClient
from pymongo.errors import PyMongoError
import sys

# Підключення до MongoDB
try:
    client = MongoClient('localhost', 27017)
    db = client['cats_db']
    collection = db['cats']
    print("Підключено до MongoDB.")
except PyMongoError as e:
    print(f"Помилка підключення до MongoDB: {e}")
    sys.exit(1)

def create_cat(name, age, features):
    """Створює новий запис про кота в колекції."""
    try:
        cat = {
            'name': name,
            'age': age,
            'features': features
        }
        result = collection.insert_one(cat)
        print(f"Кіт доданий з _id: {result.inserted_id}")
    except PyMongoError as e:
        print(f"Помилка при додаванні кота: {e}")

def read_all_cats():
    """Виводить всі записи з колекції."""
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except PyMongoError as e:
        print(f"Помилка при зчитуванні котів: {e}")

def find_cat_by_name(name):
    """Знаходить та виводить інформацію про кота за ім'ям."""
    try:
        cat = collection.find_one({'name': name})
        if cat:
            print(cat)
        else:
            print(f"Кіт з ім'ям '{name}' не знайдений.")
    except PyMongoError as e:
        print(f"Помилка при пошуку кота: {e}")

def update_cat_age(name, new_age):
    """Оновлює вік кота за ім'ям."""
    try:
        result = collection.update_one({'name': name}, {'$set': {'age': new_age}})
        if result.modified_count > 0:
            print(f"Вік кота '{name}' оновлено до {new_age}.")
        else:
            print(f"Кіт з ім'ям '{name}' не знайдений або вік вже встановлений на {new_age}.")
    except PyMongoError as e:
        print(f"Помилка при оновленні віку кота: {e}")

def add_feature_to_cat(name, feature):
    """Додає нову характеристику до списку features кота за ім'ям."""
    try:
        result = collection.update_one({'name': name}, {'$addToSet': {'features': feature}})
        if result.modified_count > 0:
            print(f"Характеристика '{feature}' додана коту '{name}'.")
        else:
            print(f"Кіт з ім'ям '{name}' не знайдений або вже має цю характеристику.")
    except PyMongoError as e:
        print(f"Помилка при додаванні характеристики коту: {e}")

def delete_cat_by_name(name):
    """Видаляє запис про кота за ім'ям."""
    try:
        result = collection.delete_one({'name': name})
        if result.deleted_count > 0:
            print(f"Кіт з ім'ям '{name}' видалений.")
        else:
            print(f"Кіт з ім'ям '{name}' не знайдений.")
    except PyMongoError as e:
        print(f"Помилка при видаленні кота: {e}")

def delete_all_cats():
    """Видаляє всі записи з колекції."""
    try:
        result = collection.delete_many({})
        print(f"Видалено {result.deleted_count} котів.")
    except PyMongoError as e:
        print(f"Помилка при видаленні всіх котів: {e}")

def main():
    """Головна функція програми."""
    while True:
        print("\nВиберіть дію:")
        print("1. Додати кота")
        print("2. Вивести всіх котів")
        print("3. Знайти кота за ім'ям")
        print("4. Оновити вік кота за ім'ям")
        print("5. Додати характеристику коту за ім'ям")
        print("6. Видалити кота за ім'ям")
        print("7. Видалити всіх котів")
        print("8. Вийти")

        choice = input("Ваш вибір: ")

        if choice == '1':
            name = input("Введіть ім'я кота: ")
            age = int(input("Введіть вік кота: "))
            features_input = input("Введіть характеристики кота (через кому): ")
            features = [feature.strip() for feature in features_input.split(',')]
            create_cat(name, age, features)
        elif choice == '2':
            read_all_cats()
        elif choice == '3':
            name = input("Введіть ім'я кота для пошуку: ")
            find_cat_by_name(name)
        elif choice == '4':
            name = input("Введіть ім'я кота: ")
            new_age = int(input("Введіть новий вік кота: "))
            update_cat_age(name, new_age)
        elif choice == '5':
            name = input("Введіть ім'я кота: ")
            feature = input("Введіть нову характеристику: ")
            add_feature_to_cat(name, feature)
        elif choice == '6':
            name = input("Введіть ім'я кота для видалення: ")
            delete_cat_by_name(name)
        elif choice == '7':
            confirm = input("Ви впевнені, що хочете видалити всіх котів? (y/n): ")
            if confirm.lower() == 'y':
                delete_all_cats()
            else:
                print("Операцію скасовано.")
        elif choice == '8':
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
