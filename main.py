import random
from datetime import datetime
from enum import unique


# Task 1
def get_days_from_today(user_input):
    user_date = datetime.strptime(user_input, '%Y-%m-%d')
    current_date = datetime.now()
    delta_days = (user_date - current_date).days
    if delta_days > 0:
        print(f"{delta_days} days left")
    else:
        user_date = user_date.replace(year=user_date.year)
        delta_days = (user_date - current_date).days
        print(f"{delta_days} days left")

get_days_from_today("2023-08-21")

# Task 2

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 100 or quantity < 1 or quantity > (max - min + 1):
        return print("Write relevant numbers")
    unique_nums = random.sample(range(min, max + 1), quantity)
    return unique_nums

lottery_numbers = get_numbers_ticket(1, 100, 10)
print("Ваші лотерейні числа:", lottery_numbers)