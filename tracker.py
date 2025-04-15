expense_traker = []

def add_expense(amount: float, category: str, description: str):
    '''
    Добавляет новый расход в список.

    Ключевые аргументы:
    amont -- сумма расхода (число с плавающей точкой)
    category -- категория расхода (строка)
    description -- описание расходв (строка)
    '''
    expense = {
        'Amount': amount,
        'Category': category,
        'Description': description
    }
    expense_traker.append(expense)

def get_expense():
    '''Возвращает список расходов.'''
    return expense_traker
    
def get_total():
    '''Возвращает сумму всех расходов.'''
    return sum([expense['Amount'] for expense in expense_traker])

def get_by_category(category: str):
    '''
    Возвращает список расходов по определенной категории.

    Ключевые аргументы:
    category -- категория, по которой отбираются расходы (строка)
    '''
    return [expense['Amount'] for expense in expense_traker if expense['Category'] == category]
