from application.salary import calculate_salary as calc

from application.db.people import get_employees as em

from datetime import date

if __name__ == '__main__':
    calc()
    em()
    print('Сегодня:', date.today())
