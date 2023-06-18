import shutil

f = open("test.txt")
"""
Самый лучший способ считать файл - перебор в цикле, так как f(объект файл) - это итератор
Когда мы считываем циклом, в памяти только одна строка а не весь файл
"""
for line in f:
    line = line.rstrip()  # убираем символы переноса строки
    print(repr(line))
f.close()

"""
Запись в файл
# """
f1 = open("hello.txt", "w")
f1.write("Hello ")
f1.write("world!")
f1.write("\nSecond line\n")
lines = ['line 1', 'line 2', 'line 3']
contents = '\n'.join(lines)
f1.write(contents)
f1.close()

"""
Запись в конец файла
"""
f2 = open("hello.txt", "a")
f2.write("\nappend!")
f2.close()

"""
Контекстный менеджер
"""
print("with")
with open("test.txt") as f, open("test_copy.txt", "w") as w:
    for line in f:
        # line = line.rstrip()
        # print(line)
        w.write(line)

"""
Копирование с помощью библиотеки shutil
"""
shutil.copy("hello.txt", "2.4_files/hello2.txt")

"""
Копирование папки
"""
shutil.copytree('test', 'test/test')
