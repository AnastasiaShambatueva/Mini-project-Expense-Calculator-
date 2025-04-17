from tracker import *

def print_add_expense():
    '''
    Запрашивает amount - сумму нового расхода, category - категорию расхода, description - описание расхода.
    Далее выводит сообщение о добавлении нового расхода.
    '''
    # Допущенная ошибка: отсутствие указания типа данных переменной amount.
    # Из-за этого введенное число считывалось как строка и функция get_total() возвращала ошибку.  
    amount = float(input('Введите сумму нового расхода: '))
    category = input('Введите категорию, к которой относится данный расход: ')
    description = input('Введите описание расхода: ')

    add_expense(amount, category, description) # Применяем функцию для записи в список expense_traker.

    print(f"В список добавлен новый расход:\n Amount - {expense_traker[-1]['Amount']} руб.\n Category - {expense_traker[-1]['Category']}\n") # Выводим сообщение о добавление нового расхода с введенными параметрами.

def print_get_expense():
    '''Выводит список всех расходов в читаемом для пользователя виде.'''
    print('Список всех расходов: ')
    for expense in range(len(expense_traker)):
        print(f"{expense+1}. Сумма - {expense_traker[expense]['Amount']} руб. Категория - {expense_traker[expense]['Category']} ({expense_traker[expense]['Description']}).")

def print_get_total():
    '''Выводит общую сумму всех расходов.'''
    print(f"Общая сумма всех расходов равна {get_total()} руб.")

def print_get_by_category():
    '''
    Создает строку из категорий расходов.
    Запрашивает категорию, по которой необходимо отобрать расходы, из предложенного списка.
    Далее выводит список расходов по заданной категории.
    '''
    set_of_categories = set([expense['Category'] for expense in expense_traker]) # Создаем сет из категорий, которые встречаются в списке всех расходов.
    string_of_categories = '' 
    for str_category in set_of_categories:
        string_of_categories = (string_of_categories + str_category + ', ') # В цикле for перебираем категории из сета и добавляем их к строке через занятую.
    string_of_categories = string_of_categories[:-2] # Убираем два последних символа в строке категорий - лишнюю запятую и пробел.

    print(f"Имеющиеся в списке категории: {string_of_categories}")
    required_category = input('Введите нужную вам категорию: ')
    
    print('Список расходов по выбранной категории: ')
    for expense in range(len(get_by_category(required_category))):
        print(f"{expense+1}. {get_by_category(required_category)[expense]} руб.") # Выводим все расходы из списка, в которых категория соответствует введенной.

def end():
    '''Заканчивает работу калькулятора'''
    print('Спасибо, что используете "Калькулятор расходов"!')
    exit()

while True:
    
    print('Хотите воспользоваться консольным приложением "Калькулятор расходов"?')
    start = input('Введите ответ (да/нет): ')

    if start in ['Да', 'да', 'ДА']:

        print('Выберите необходимое действие:\n' \
        '1 - Добавить расход\n' \
        '2 - Вывести список всех расходов\n' \
        '3 - Вывести общую сумму расходов\n' \
        '4 - Вывести список расходов по определенной категории\n' \
        '5 - Закончить работу с калькулятором')

        num = input('Введите цифру, обозначающую нужное вам действие: ')

        name_function = {
            '1': print_add_expense,
            '2': print_get_expense,
            '3': print_get_total,
            '4': print_get_by_category, 
            '5': end
        } # Словарь с функциями и их обозначениями.

        name_function[num]() # Запуск нужной функции.
    
    else:
        print('Если понадобится помощь - обращайтесь!')
        break 
