"""
    Simple expense tracker program
"""

def add_expenses(expenses, amount, category):
    expenses = []
    my_dict = {
        'amount ': amount,
        'category': category}

    expenses.append(my_dict)

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense}, Category: {expense}')