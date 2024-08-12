# Boolean - 3 состояния

b = bool

t = True
f = False
n = None

# if/elif/else

if True:
     print("я выполняюсь")

if False:
    print('я никогда не выолнюс ')

code = 200

if 200 <= code < 400:
    print('првоекра пройдена')
elif 400 <= code < 600:
    print('плохой код ответа')
else:
    print('странный код')

# Пустые объекты - False

user_list = []
if user_list == []:
    pass
# или проще так
if user_list:
    pass


items_count = 1
if items_count == 1:
    pass
# или проще так
if items_count:
    pass

if 'abc' == '':
    pass
# или проще так
if 'abc':
    pass

print('____')
print(bool(100))
print(bool(-100))
print(bool(0))
print('____')

print(bool('abc'))
print(bool(''))
print('____')


print(bool([1, 2, 3]))
print(bool([]))
print(bool([False]))
print('____')




