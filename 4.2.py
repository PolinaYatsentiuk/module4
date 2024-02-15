def get_cats_info(path):
    cats_info = []
    
    try:
        with open(path, 'r') as file:
            for line in file:
                cat_id, cat_name, cat_age = line.strip().split(',')
                cats_info.append({"id": cat_id, "name": cat_name, "age": cat_age})
    except FileNotFoundError:
        return ("Не знайдено файл")
    except Exception as e:
        return (f"Виникла помилка: {e}")
    return cats_info

cats_info = get_cats_info("cats_file.txt")
print(cats_info)

