# Mini-project-Expense-Calculator-
Консольное приложение для учета личных расходов.

🚀 ИСПОЛЬЗОВАНИЕ
Для использования калькулятора необходимо скачать файлы tracker.py, где хранится основная логика программы, и main.py, где хранится пользовательский интерфейс. Запуск приложения осуществляется через main.py 

Доступные команды:
1 - Добавить расход
2 - Вывести список всех расходов
3 - Вывести общую сумму расходов
4 - Вывести расходы по категории
5 - Выход

🛠 ФУНКЦИОНАЛ. ОСНОВНЫЕ ВОЗМОЖНОСТИ.
1) Добавление расходов с указанием:
Суммы расхода (рубли)
Категории расхода (произвольная строка)
Описания расхода (произвольная строка)

3) Просмотр статистики:
Полный список расходов (история операций)
Суммарные траты
Фильтрация по категориям

4) Данные хранятся в памяти (сбрасываются после закрытия)

🐛 ПРОБЛЕМЫ
В текущей версии исправлена ошибка:
Было (вызывало ошибку при расчете суммы): amount = input('Введите сумму нового расхода: ')  # получали строку
Стало: amount = float(input('Введите сумму: '))  # корректное число

