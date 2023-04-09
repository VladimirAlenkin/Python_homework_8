
def show_data() -> None:
    '''Выводит информацию из справочника'''
    with open('book.txt', 'r', encoding='utf-8') as f:
        print(f.read())

def add_data() -> None:
    '''Добавляет информацию в справочник'''
    fio = input('Введите ФИО: ')
    tel_number = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n{fio} | {tel_number}')
    print('Успешно!')

def find_data() -> None:
    '''Осуществляет поиск по справочнику'''
    
    data = input('Введите данные для поиска: ')
    
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    print('Результаты поиска: ')
    print(search(tel_book, data))

def search(book: str, info: str) -> str:
    '''Находит в строке записи по определенному критерию поиска'''
    book = book.split('\n')
    return'\n'.join([post for post in book if info in post])

def change_data() -> None:
    '''Вносит изменение в определенную строку справочника'''
    with open('book.txt', 'r', encoding='utf-8') as f:
        a = f.read()
    data = input('Введите данные для изменения: ')  
    b = search(a, data)
    print(b)
    
    def edited(text: str) -> str:
            fio = input('Введите новые фио (или \'enter\', если оставить прежними): ')
            num = input('Введите новый номер телефона (или \'enter\', если оставить прежним): ')
            if len(fio) == 0:
                fio = text.split(' | ')[0]
            if len(num) == 0:
                num = text.split(' | ')[1]
            return f'{fio} | {num}'
    a = a.replace(b,edited(b))
    
    with open('book.txt', 'w', encoding='utf-8') as f:
        f.write(a)
    print()
    print("Новый справочник: ", a, sep='\n')

def removal_data() -> None:
    '''Осуществляет удаление строки из справочника'''
    with open('book.txt', 'r', encoding='utf-8') as f:
        a = f.read()
    data = input('Введите данные для удаления: ')  
    b = search(a, data)
    print(b)
    temp = input('Удаляем эти данные? (y/n) ')
    if temp == 'y':
        
        a = a.replace(b,'')
        a = a.strip()
        
        
        print('Данные удалены!')
        with open('book.txt', 'w', encoding='utf-8') as f:
            f.write(a)
        print()
        print("Новый справочник: ", a, sep='\n')
    else:
        print('Как скажете)')
