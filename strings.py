#строки

# перевернуть
test_string = 'kek cheburek'
reversed_string = test_string[::-1]
print(reversed_string)

# найти подстроку
test_string = 'fkglkl kl"da konechno shas"dfsd sdf'
idx_start = test_string.find('"', 0, len(test_string))
idx_end = test_string.find('"', idx_start + 1, len(test_string))
if (idx_start == -1) or (idx_end == -1):
    print("not found")
else:
    print(test_string[idx_start : idx_end + 1])

# удвоить число из строки
test_string = "102"
number = int(test_string)
print(number * 2)

# поменять местами числа, разделенные пробелом
test_string = "124 -56342"
idx_start = test_string.find(' ', 0, len(test_string))
print(test_string[idx_start + 1:] + ' ' + test_string[:idx_start])

# достать логин из почтового адреса
test_string = "st062780@student.spbu"
idx_start = test_string.find('@', 0, len(test_string))
print(test_string[:idx_start])

# форматирование номера телефона
test_string = "+7 (924) 334-20-12"
result = ''
for ch in test_string:
    if (ch == '(') or (ch == ')') or (ch == '-') or (ch == ' '):
        continue
    result += ch
print(result)

# проверка на палиндром
test_string = "А роза упала, на лапу - Азора"
i = 0
j = len(test_string) - 1
#result = True
#while ((i < j) and result):
#    while (not (test_string[i].isalpha())):
#        ++i
#        if (i >= j):
#            break
#    while (not (test_string[j].isalpha())):
#        --j
#        if (j <= i):
#            break
#    while ((test_string[i].isalpha()) and (test_string[j].isalpha()) and (i < j)):
#        if (test_string[i] != test_string[j]):
#            result = False
#            break
#        ++i
#        --j
alphas = ''
for ch in test_string:
    if (ch.isalpha()):
        alphas += ch
alphas = alphas.upper()
result = True
for i in range(0, int(len(alphas) / 2)):
    if (alphas[i] != alphas[len(alphas) - i - 1]):
        result = False
print(result)

# петя блин
result = ''
for i in range(1, 124):
    tmp = str(i)
    for ch in tmp:
        if (ch != '9'):
            result += ch
print(result)

# Армстронг
result = ''
for i in range(100, 1000):
    tmp = (i // 100) ** 3 + ((i // 10) % 10) ** 3 + (i % 10) ** 3
    if (i == tmp):
        result += str(i) + ' '
print(result)

# Автоморфные числа
result = ''
N = 1000
for i in range(N):
    tmp = i * i
    size = len(str(i))
    last = str(tmp)[-size:]
    if (i == int(last)):
        result += str(i) + ' '
print(result)

# Диаффант
a = 15
b = 17
c = 21
d = 185
result = ''
for x in range (14):
    for y in range (12):
        for z in range (10):
            if (a * x + b * y + c * z == d):
                result += str(x) + ' ' + str(y) + ' ' + str(z) + '\n'
print(result)
