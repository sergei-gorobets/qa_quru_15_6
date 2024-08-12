# объявляем функуцию

def my_func():
    print("вызвал функцию!")

my_func()
my_func()
my_func()


print('---')
# функция с позиционым аргументом

def sum_numders(a: int, b: int):
    print(a + b)

sum_numders(10, 20)
sum_numders(20, 30)
sum_numders(19, 61)
sum_numders('при', 'вет')

print('---')
# Возвращаемые значения

def sum(a: int, b: int):
    return a + b

n = sum(10,25)
print(n)

print('---')
# Функции с именновынными аргументами

sum_numders(a=10, b=15)
sum_numders(b=15, a=10)

print('---')
# функции с аргументами по умолчанию

def multiply(n, mult=2):
    print(n * mult)

multiply(10)
multiply(10, mult=5)


# Возвращение нескольких значение

def retur_tuple():
    return 1, 2, 3

t = retur_tuple()
print(t)

t1, t2, t3 = retur_tuple()
print(t1, t2, t3)

t1, *t2, = retur_tuple()
print(t1, t2,)

t1, t2, *t3= retur_tuple()
print(t1, t2, t3)

t1, *_,= retur_tuple()
print(t1)

print('___')

# Переменное количество аргументов на примере print

def custom_print(*args):
    for arg in args:
        print(arg)


custom_print(1, 2, 3, 4, 5)

print('___')

# Переменное количество именованных аргументов

def custom_named_print(*args, **kwargs):
   print(args, kwargs)
   print(*args, **kwargs)

custom_named_print(1,2,3,4,5, end='!\n', sep=' | ')

print('___')

# Области видимости переменных

v = 123

def my_awesome_func():
    v = 456
    print(v)

print(v)
my_awesome_func()
print(v)

