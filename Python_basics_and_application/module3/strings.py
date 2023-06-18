# методы строк
print("abs" in "abcba")  # проверка вхождения
print("abacaba".find("aba"))  # индекс первого вхождения или -1
print("abacaba".rfind("aba"))  # то-же самое но с права на лево

print("cabcd".index("abc"))  # индекс первого вхождения подстроки или ошибка  substring not found
print("jwh erf kuhwe ruifhr uwei".startswith("jwhry"))  # проверят начинается ли строка с указанной подстроки
                                                        # можно использовать кортеж в качестве префикса
print("frghkjfgh.png".endswith('.png1'))  # проверяет не заканчивается ли строка на указанную подстроку
print('abacaba'.count("aba"))  # кол-во вхождений одной строки в другую

s1 = "1,2,3,4"
print(s1)
print(s1.replace(",", ", "))  # можно передать число замен -> print(s1.replace(",", ", ", 2))

s2 = '1 2 3 4'
print(s2.split())  # разбивает строку по указанному символу на элементы списка
                   # по умолчанию разделяет по пробелу а пустые строки удаляет

s3 = "   1, 2, 3, 4   "
print(s3.rstrip())  # удаляет указанные строчные симвалы справа
print(s3.lstrip())  # удаляет указанные строчные симвалы слева
print(s3.strip())  # удаляет указанные строчные симвалы справа и слева

s4 = "__1, 2, 3, 4__*"
print(s4.rstrip('_*'))  # удаляет указанные строчные симвалы справа
print(s4.lstrip('_*'))  # удаляет указанные строчные симвалы слева
print(s4.strip('_*'))  # удаляет указанные строчные симвалы справа и слева

numbers = map(str, [1, 2, 3, 4, 5])
print(repr(" ".join(numbers)))  # вставляет указанную строку между всеми элементами

s = 'ababac'
a = 'c'
b = 'c'

answer = None
count = 0
while a in s:
    s = s.replace(a, b)
    count += 1
    if count >= 1000:
        answer = "Impossible"
        print(answer)
        break
if not answer:
    answer = count
    print(answer)

print("abacaba".find("aba"))  # индекс первого вхождения или -1
print('-------------------')
s = "abababa"
t = "abc"

ans = 0
index = 0
while True:
    if t in s[index:]:
        if s[index:].find(t) == 0:
            ans += 1
        index += 1
    else:
        print(ans)
        break