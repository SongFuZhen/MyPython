import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

# ax^2 + bx + c = 0 的解


def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
    x2 = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)
    return (x1, x2)


# 位置参数
def power(x):
    return x * x

# x 位置参数  n 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# name 位置参数  age 位置参数  kw关键字参数
def person(name, age, **kw):
    print('name:', name, 'age', age, 'other', kw)

#print(person('Bob', 35, city = 'Beijing'))
#print(person('Adam', 45, gender='M', job='Engineer'))

# 命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)

# print(person('jack',24,city='Beijing', job='Engineer'))

#递归函数
def fact(x):
    if x == 1:
        return 1
    return x * fact(x - 1)


# 使用尾递归方式
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

# print(fact(1000))

# 汉诺塔移动
def move(n, a, b, c):
    if n == 1:
        print('move', a, '--->', b)
    else:
        move(n-1,a,c,b)
        move(1, a, b, c)
        move(n-1, b, a, c)

# print(move(4, 'A', 'B', 'C'))








