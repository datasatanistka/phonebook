
def input_name():
    return input('Введите имя: ')

def input_surname():
    return input('Введите фамилию: ')

def input_patronomic():
    return input('Введите отчество: ')

def input_phone():
    return input('Введите телефон: ')

def input_address():
    return input('Введите адрес: ')

def create_contact():
    name = input_name()
    surname = input_surname()
    patronomic = input_patronomic()
    phone = input_phone()
    address = input_address()
    return f'{name} {surname} {patronomic} {phone} {address}\n'

def add_contact():
    contact = create_contact()
    with open('phonebook.txt', 'a', encoding='UTF-8') as f_w:
        f_w.write(contact)

def print_phonebook():
    with open('phonebook.txt', 'r', encoding='UTF-8') as f_r:
        contacts_str = f_r.read()
    list_contacts = contacts_str.rstrip().split('\n')
    for i, contact in enumerate(list_contacts, 1):
        print(i, contact + '\n')

def copy_contact(line_num, source_file = 'phonebook.txt', copied_file = 'copied_file.txt'):
    with open(source_file, 'r', encoding='UTF-8') as f_r:
        lines = f_r.readlines()
        if 0 < line_num <= len(lines):
            contact_to_copy = lines[line_num - 1]
            with open(copied_file, 'a', encoding='UTF-8') as f_w:
                f_w.write(contact_to_copy)
            print('Контакт успешно скопирован.')
        else:
            print('Некорректный номер строки.')
            line_num = int(input('Введите номер строки для копирования: '))
            copy_contact(line_num)

def find_contact():
    print(
        'Возможные варианты поиска:\n'
        '1. По имени:\n'
        '2. По фамилии:\n'
        '3. По отчеству\n'
        '4. По телефону\n'
        '5. По адресу\n'
        )
    var = input('Выберите вариант поиска: ')
    while var not in ('1','2','3','4','5'):
        print('Некорректный ввод')
        var = input('Выберите вариант поиска: ')
    i_var = int(var) - 1 

    search = input('Введите данные для поиска: ')

    with open('phonebook.txt', 'r', encoding='UTF-8') as f_r:
        contacts_str = f_r.read()
    list_contacts = contacts_str.rstrip().split('\n')
    for contact in list_contacts:
        contact_list = contact.split()
        if search in contact_list[i_var]:
            print(contact)


#UI

def ui():
    with open('phonebook.txt','a'):
        pass
    print(
        'Возможные варианты действий:\n'
        '1. Добавление нового контакта:\n'
        '2. Вывод данных на экран:\n'
        '3. Поиск контакта\n'
        '4. Копирование контакта в другой файл:\n'
        '5. Выход из программы\n'
        )
    choice = input('Выберите вариант действия: ')

    while choice not in ('1','2','3','4','5'):
        print('Некорректный ввод')
        choice = input('Выберите вариант действия: ')

    if choice == '1':
        add_contact()
    elif choice == '2':
        print_phonebook()
    elif choice == '3':
        find_contact()
    elif choice == '4':
        print_phonebook()
        line_num = int(input('Введите номер строки для копирования: '))
        copy_contact(line_num)
    else:
        print('Всего доброго!')

ui()


