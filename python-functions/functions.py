

def verify_age(age):
    if age > 17:
        print(f"{age} is old enough to buy a lottery ticket.")
        # print("How many would you like?")
    else:
        print(f"{age} is not old enough to buy a lottery ticket.")
        # print("Can I interest you in some candy?")
    print("Thank you for your patronage.")

def verify_interest(customer_interest):
    if customer_interest == True:
        print("Excellent choice, but we only have Twix.")
        print("How many would you like? ")
    else:
        print("Come back another time!")
    print("Thank you for your patronage.")

# print(customer_one_age)  # age is out of scope

customer_one_age = 23
customer_two_age = 16
customer_three_age = 17
customer_four_age = 25

customer_one_interest = True
# verify_age(customer_two_age)
# verify_interest(customer_one_interest)

# Rule for argument orders:
# 1st. params, 2nd. *args, 3rd. default parameters, **kwargs

def arg_demo(pos1, pos2, *args, **kwargs):
    print(f"Positional params: {pos1} {pos2}")
    print('*args')
    for arg in args:
        print(' ', arg)
    print('**kwargs')
    for keyword, value in kwargs.items():
        print(f' {keyword}: {value}')

# arg_demo('A', 'B', 1, 2, 3, color='purple', shape='circle')

# reduce function

from functools import reduce

new_list = [ 7, 8, 9]

def accumulator(acc, item):
    return acc + item

# print((reduce(accumulator, new_list, 0)))

# map

# filter

# zip

# lambda expression
# =================
# lambda in python are a 1 time anonymous function that you don't need more than once
# lambda param: action(param)

his_list = [ 7, 8, 9]

# print(list(map(lambda item: item*3, his_list)))

# print(reduce(lambda acc, item: acc + item, his_list))

# decorators
# ===========
# @some_function
# def regular_function():

def my_decorator(func):
    def wrap_func(param):
        print('******')
        func(param)
        print('******')
    return wrap_func

@my_decorator
def hay(name):
    print(f'hey there! {name}')

hay("Dennie")

@my_decorator
def bye():
    print("Take care")

# bye()