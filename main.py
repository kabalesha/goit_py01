from datetime import datetime

# Task 1
def get_days():
    user_input = input("Type your date (DD.MM): ")
    current_year = datetime.now().year
    user_date = datetime.strptime(user_input, '%d.%m')

    user_date = user_date.replace(year=current_year)

    if user_date < datetime.now():
        user_date = user_date.replace(year=current_year + 1)

    days_difference = (user_date - datetime.now()).days
    print(f"Days until your date: {days_difference}")


get_days()