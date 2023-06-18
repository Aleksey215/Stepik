# Словарь для хранения, записи и чтения наших данных
db = dict()
db.update({'global': []})

def add(namespace:str, var:str):
    """
    Функция добавления переменной в пространство имен
    аргументы:
        namespace - название пространства имен
        var - имя переменной
    """
    if namespace not in db.keys():
        db.update({namespace: []})
        db[namespace].append(var)
    else:
        db[namespace].append(var)

def create(namespace:str, parent:str):
    """
    Функция создания пространства имен
    аргументы: 
        namespace - название пространства имен
        parent - пространство имен в котором создается новое
    """
    db[parent].append(namespace)
    db.update({namespace: []})

def get(namespace:str, var:str):
    """
    Функция чтения пространства имен по переменной
    аргументы:
        namespace - название пространства имен
        var - имя переменной
    """
    if namespace is None:
        return None
    parent_namespace = None
    for key, values in db.items():
        if namespace in values:
            parent_namespace = key
    if var in db[namespace]:
        return namespace
    else:
        return get(namespace=parent_namespace, var=var)

num = int(input())
for _ in range(1, num+1):
    cmd, namesp, arg = input().split()
    if cmd == 'add':
        add(namespace=namesp, var=arg)
    elif cmd == 'create':
        create(namespace=namesp, parent=arg)
    elif cmd == 'get':
        print(get(namespace=namesp, var=arg))