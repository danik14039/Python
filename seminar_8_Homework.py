# Задача 38: Создать телефонный справочник возможностью добавления записей и чтения.
# Пользователь также может ввести фамилию, тогда программа должны вывести на экран все записи с этой фамилий.
# Также пользователь может добавлять новых людей в справочник в режиме экспорт.


def imp():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    tel = input('Введите номер телефона: ')
    with open('Log.txt', 'a', encoding='utf-8') as f:
        f.writelines(f'\n\n{surname}\n{name}\n{tel}')

def exp():
    surname = input('Enter surname: ')
    with open('Log.txt', 'r', encoding='utf-8') as f:
        text = f.read().splitlines()
        for i in range(len(text)):
            if text[i] == surname:
                for line in text[i:i + 3]:
                    print(line)


mode = int(input('Введите режим работы со справочником: 1 - экспорт, 2 - импорт: '))
if mode == 1:
    exp()
elif mode == 2:
    imp()
else:
    print('Выбран не корректный режим работы')

