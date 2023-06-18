# 1. Функция сохранения данных в файл:
def save_data(data, filename):
    with open(filename, 'w') as f:
        for item in data:
            f.write(','.join(item) + '\n')

# 2. Функция загрузки данных из файла:
def load_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            item = line.strip().split(',')
            data.append(item)
    return data

# 3. Функция поиска записей по заданному критерию:
def search_data(data, key, value):
    results = []
    for item in data:
        if value.lower() in item[key].lower():
            results.append(item)
    return results

# 4. Функция вывода данных на экран:
def print_data(data):
    for item in data:
        print('{} {} {}: {}'.format(item[0], item[1], item[2], item[3]))

# 5. Функция изменения данных:
def edit_data(data, key, value, new_value):
    for item in data:
        if value.lower() in item[key].lower():
            item[key] = new_value

# 6. Функция удаления данных:
def delete_data(data, key, value):
    data[:] = [item for item in data if value.lower() not in item[key].lower()]


filename = 'phonebook.txt'
data = []

while True:
    print('1. Вывести данные')
    print('2. Добавить запись')
    print('3. Сохранить данные')
    print('4. Загрузить данные')
    print('5. Поиск по имени')
    print('6. Поиск по фамилии')
    print('7. Изменить данные')
    print('8. Удалить данные')
    print('9. Экспорт в файл')
    print('10. Импорт из файла')
    print('11. Выход')

    choice = input('Введите номер действия: ')

    if choice == '1':
        print_data(data)
    elif choice == '2':
        surname = input('Введите фамилию: ')
        name = input('Введите имя: ')
        patronymic = input('Введите отчество: ')
        phone = input('Введите номер телефона: ')
        data.append([surname, name, patronymic, phone])
    elif choice == '3':
        save_data(data, filename)
        print('Данные сохранены в файл')
    elif choice == '4':
        data = load_data(filename)
        print('Данные загружены из файла')
    elif choice == '5':
        name = input('Введите имя для поиска: ')
        results = search_data(data, 1, name)
        print_data(results)
    elif choice == '6':
        surname = input('Введите фамилию для поиска: ')
        results = search_data(data, 0, surname)
        print_data(results)
    elif choice == '7':
        surname = input('Введите фамилию для изменения: ')
        name = input('Введите имя для изменения: ')
        key = input('Введите ключ для изменения (0 - фамилия, 1 - имя, 2 - отчество, 3 - телефон): ')
        new_value = input('Введите новое значение: ')
        edit_data(data, key, surname, new_value)
        edit_data(data, key, name, new_value)
        print('Данные изменены')
    elif choice == '8':
        surname = input('Введите фамилию для удаления: ')
        name = input('Введите имя для удаления: ')
        delete_data(data, 0, surname)
        delete_data(data, 1, name)
        print('Данные удалены')
    elif choice == '9':
        export_filename = input('Введите имя файла для экспорта: ')
        save_data(data, export_filename)
        print('Данные экспортированы в файл')
    elif choice == '10':
        import_filename = input('Введите имя файла для импорта: ')
        data += load_data(import_filename)
        print('Данные импортированы из файла')
    elif choice == '11':
        break
    else:
        print('Неверный выбор')
