import re
"""
re.math(шаблон, строка) - проверяет подходит ли строка под шаблон
re.search(шаблон, строка) - находит первую подстроку в строке, которая подходит под шаблон
re.findall(шаблон, строка) - находит все подстроки в строке, которые подходят под шаблон
re.sub(шаблон, строка) - заменит все вхождения подстрок, которы подходят под шаблон
"""


x = "hello\nworld"
print(x)

x = r"hello\nworld"  # raw - сырая строка
print(x)

# [] -- можно указать множество подходящих символов

print('-- match --')
pattern = r"a[abc]c"  # вторым символом может быть любой из перечисленных в скобках
string = "acc"
match_object = re.match(pattern, string)
print(match_object)

print("-- search --")
pattern = r"abc"
string = "babc"
match_object = re.search(pattern, string)
print(match_object)

print('-- findall --')
pattern = r"a[abc]c"  # вторым символом может быть любой из перечисленных в скобках
string = "aac, abc, acc"
match_object = re.findall(pattern, string)
print(match_object)

print("-- sub --")
fixed_typos = re.sub(pattern, "abc", string)
print(fixed_typos)
