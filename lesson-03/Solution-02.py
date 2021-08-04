deposit = 2130
deposit_years = 5
annual_interest_rate = 10
year_bonus = 120

# Calculate deposit amount for 5 years
for i in range(deposit_years):
    deposit = deposit + (deposit * annual_interest_rate / 100) + year_bonus

print(deposit)