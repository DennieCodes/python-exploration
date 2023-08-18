from datetime import datetime

datetime(1941, 5, 24,1, 30)
str(datetime(1941, 5, 24, 1, 30))

my_birthday = datetime(1974, 8, 1, 11, 30, 30)
formatted =  my_birthday.strftime("%y-%m-%d %H:%M:%S")
# formatted = my_birthday.strftime("%A %B")

print(formatted)

# print(datetime.fromisoformat("1983-04-01 01:02:03"))

# print(datetime.now())

assert datetime(2022, 1, 1) == datetime(2022, 1, 1)
