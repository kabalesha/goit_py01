import random
from datetime import datetime

# Task 1

def get_days_from_today(user_input):
    try:
        user_date = datetime.strptime(user_input, '%Y-%m-%d')
    except ValueError:
        return None
    current_date = datetime.now()
    delta_days = (user_date - current_date).days
    if delta_days == 0:
        return 0
    return delta_days
days_left = get_days_from_today("2023-08-21")

# Task 2

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 100 or quantity < 1 or quantity > (max - min + 1):
        return []
    unique_nums = random.sample(range(min, max + 1), quantity)
    return sorted(unique_nums)
lottery_numbers = get_numbers_ticket(1, 100, 10)
