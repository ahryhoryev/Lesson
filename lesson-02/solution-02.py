deposit = 2130
percents = 10
dep_years = 5
bonus = 120

for year in range(dep_years):
    deposit = deposit + (deposit / percents) + bonus
print(f'На счету через 5 лет {deposit}')
