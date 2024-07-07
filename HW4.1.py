def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        total = 0
        count = 0
        
        for line in lines:
            name, salary = line.strip().split(',')
            total += int(salary)
            count += 1
            
        if count == 0:
            average = 0
        else:
            average = total / count
        
        return total, average
    
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return None, None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None, None

# Приклад використання функції
total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
