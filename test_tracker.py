import pytest
from tracker import *


@pytest.fixture(autouse=True)
def clear_expenses():
    '''Очищает список expense_traker перед каждым тестом для исключения влияния тестов друг на друга.'''
    yield # Выполнение теста.
    expense_traker.clear() # Очистка списка после теста.

def test_add_expense():
    '''Проверяет правильность добавления нового расхода в список expense_traker.'''
    add_expense(5000.15, 'Жилье', 'Коммунальные услуги')
    assert len(expense_traker) == 1 
    assert expense_traker[0]['Amount'] == 5000.15
    assert expense_traker[0]['Category'] == 'Жилье'
    assert expense_traker[0]['Description'] == 'Коммунальные услуги'

def test_get_expense():
    '''Проверяет правильность вывода списка всех расходов.'''
    add_expense(150.50, 'Продукты', 'Овощи и фрукты')
    add_expense(860.20, 'Кафе', 'Обед в ресторане')
    assert get_expense() == expense_traker

def test_get_total():
    '''Проверяет правильность рассчета суммы всех расходов.'''
    add_expense(1000.0, 'Здоровье', 'Поход в спортзал')
    add_expense(2380.0, 'Одежда', 'Футболка и джинсы')
    add_expense(500.0, 'Образование', 'Покупка книг')
    assert get_total() == 3880.0

def test_get_expense_without_values():
    '''Проверяет правильность рассчета суммы пустого списка расходов.'''
    assert get_total() == 0.0

def test_get_by_category():
    '''Проверяет правильность отбора расходов по определенной категории.'''
    add_expense(2000.0, 'Транспорт', 'Ремонт машины')
    add_expense(350.60, 'Продукты', 'Хлеб и выпечка')
    add_expense(1500.0, 'Подарки', 'День рождения друга')
    add_expense(200.0, 'Продукты', 'Молочные продукты')
    
    food_expenses = get_by_category('Продукты')
    transport_expenses = get_by_category('Транспорт')
    other_expenses = get_by_category('Подарки')

    assert len(food_expenses) == 2
    assert len(transport_expenses) == 1
    assert len(other_expenses) == 1
    assert transport_expenses[0] == 2000.0

