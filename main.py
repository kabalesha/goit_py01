# # This is a sample Python script.
#
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/


from datetime import datetime


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