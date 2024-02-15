
def total_salary(path):
    total = 0
    count = 0
    
    try:
        with open(path, 'r') as file:
            for line in file:
                name, salary_net = line.strip().split(',')
                salary = int (salary_net)
                total += salary
                count += 1
    except FileNotFoundError:
        return ('Не знайдено файл')
    except Exception as e:
        return (f"Виникла помилка: {e}")
    
    finally:
        if count == 0:
            return 0
        else:
            average = total/count
            return total, average
            
total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
        
    
