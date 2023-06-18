storage = dict()


def write_in_storage(task: str, storage: dict)->None:
    key = task[0]
    values = task[2:]
    storage[key] = values


def get_answer(class1: str, class2: str,
               storage: dict, path: list) -> bool:
    if class1 in storage[class2]:
        print("Yes")
        return True
    if class1 == class2:
        print("Yes")
        return True
    if not storage[class2] and not path:
        print('No')
        return False
    for parent in storage[class2]:
        if parent not in path and parent in storage.keys():
            path.append(parent)
    if path:
        parent_class2 = path[0]
        path.remove(parent_class2)
        get_answer(class1=class1, class2=parent_class2,
                   storage=storage, path=path)


num = int(input())
for _ in range(num):
    string = input().split()
    write_in_storage(task=string, storage=storage)


num_of_requests = int(input())
for _ in range(num_of_requests):
    class1, class2 = input().split()
    get_answer(class1=class1, class2=class2,
               storage=storage, path=list())
