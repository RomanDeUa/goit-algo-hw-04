def get_cats_info(path):
    cats_info = []
    try:
        with open(path, encoding='utf-8') as file:
            for line in file:
                line = line.strip()  # Видаляємо зайві пробіли та символи нового рядка
                if line:  # Перевіряємо, чи рядок не пустий
                    cat_id, name, age = line.split(',')
                    cat_info = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    cats_info.append(cat_info)
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")
    
    return cats_info

# Приклад використання функції
cats_info = get_cats_info("cats.txt")
print(cats_info)
