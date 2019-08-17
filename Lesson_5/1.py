"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""
import collections

Company = collections.namedtuple('Company',
                                 ['name', 'profit1', 'profit2', 'profit3', 'profit4'])

quarter_qty = 4

try:
    company_qty = int(input('Введите количество анализируемых компаний: '))
except ValueError:
    print('Ошибка! Необходимо ввести целое число.')
    exit(1)

companies = []
for i in range(company_qty):
    company_name = input(f'Введите имя {i + 1}й компании: ')
    try:
        qtr_profit = [int(input(f'Прибыль {company_name} за {i + 1}й квартал: ')) for i in range(quarter_qty)]
    except ValueError:
        print('Ошибка! Необходимо ввести целое число.')
        exit(1)

    companies.append(Company(company_name, qtr_profit[0], qtr_profit[1], qtr_profit[2], qtr_profit[3]))

company_profits = [sum((company.profit1, company.profit2, company.profit3, company.profit4)) for company in companies]

avg_profit = sum(company_profits) / len(companies)

print(company_profits)
print(avg_profit)

print('Компании, чья прибыль за год оказалась выше средней:')
for i, company in enumerate(companies):
    if company_profits[i] > avg_profit:
        print(company.name)

print('Компании, чья прибыль за год оказалась ниже средней:')
for i, company in enumerate(companies):
    if company_profits[i] < avg_profit:
        print(company.name)
