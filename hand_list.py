# как проверить функцию на ошибки?

from main import hello_to, salary

# 1. написать программу
# 2. check directly the function
# hello_to('ali')
# salary(500,2) == 3000
# print(salary(500, 2))

# с помощью if
if salary(20, 2) != 120:
    print('failed')
if hello_to(1) == 'Hello, 1':
    print('failed')
else:
    print("ok")
