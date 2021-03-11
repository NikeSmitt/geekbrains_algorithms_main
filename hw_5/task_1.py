"""Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для
каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import defaultdict

PERIODS = 4
companies = defaultdict(list)

company_count = int(input('Введите количество кампаний (названия уникальны) -> '))
for _ in range(company_count):
    comp_name = input('Введите название кампании -> ')
    for i in range(PERIODS):
        income = float(input(f'Введите прибыль за {i + 1} квартал -> '))
        companies[comp_name].append(income)

# прибыль для всех предприятий
all_incomes = []
for incomes in companies.values():
    all_incomes.extend(incomes)

# сумма прибылей    
incomes_sum = 0
for value in all_incomes:
    incomes_sum += value

# среднее значение прибыли
mean_income = incomes_sum / len(all_incomes)

# вывод
output = defaultdict(list)
for company, incomes in companies.items():
    if sum(incomes) / len(incomes) >= mean_income:
        output['high'].append(company)
    else:
        output['low'].append(company)

print('Компании с доходом выше или равно среднему:')
print(*output['high'], sep='\n')
print('*' * 30)
print('Компании с доходом ниже среднего:')
print(*output['low'], sep='\n')
