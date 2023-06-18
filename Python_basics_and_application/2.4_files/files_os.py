import os
import os.path

print()
print(os.getcwd())
print(os.listdir('2.4_files'))
print(os.path.exists('2.4_files/files.py'))
print(os.path.exists('tests'))
# получение абсолютного пути
print(os.path.abspath('file'))

os.chdir('1.6_classes')
print(os.listdir())

os.chdir('..')
print(os.listdir())

print()
for current_dir, dirs, files in os.walk('.'):
    print(current_dir, dirs, files)
    