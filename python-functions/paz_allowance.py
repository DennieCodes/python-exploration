'''

Young Paz gets a $30 allowance on the first day of each month. She's a fairly frugal young person, and never spends more than she has. Good for Paz!

Let's say that Paz spends $13 the first month, $22 the next month, and $33 the following month. How much money will she have on the first day of the fourth month? That's the function that you'll be writing.

3
Paz's allowance
Given a list of how much Paz spends each month, expenses, complete the function cash_on_hand that will return the amount of money she'll have the month after all of the expenses.

Constraints: 1 <= len(expenses) <= 100

Example:

Paz's expenses for five months are [10, 20, 30, 40, 45].

She starts out the first month with $30 and spends $10, leaving $20
She starts out the second month with $50 ($30 from her allowance and $20 from the previous month) and spends $20, leaving $30
She starts out the third month with $60 and spends $30, leaving $30
She starts out the fourth month with $60 and spends $40, leaving $20
She starts out the fifth month with $50 and spends $45, leaving $5
She starts out the sixth month with $35
Your function cash_on_hand would return 35 in this scenario.

input: list of expense per month
output: how much money is left after expenses
note: each month begins with $30 allowance
'''

def cash_on_hand(expenses):
    total_expenses = sum(expenses)
    total_allowance = (len(expenses) + 1) * 30

    return total_allowance - total_expenses

    # cash_on_hand = 0

    # for month in expenses:
    #     cash_on_hand += 30 - month

    # return cash_on_hand + 30

data1 = [10, 20, 30, 40, 45]
print(cash_on_hand(data1))
