storage = dict()


def write_in_storage(task: str, storage: dict)->None:
    key = task[0]
    values = task[2:]
    storage[key] = values


def get_parent(class1: str, class2: str,
               storage: dict, path: list):
    if class1 in storage[class2]:
        return True
    if class1 == class2:
        return True
    if not storage[class2] and not path:
        return False
    for parent in storage[class2]:
        if parent not in path and parent in storage.keys():
            path.append(parent)
    if path:
        parent_class2 = path[0]
        path.remove(parent_class2)
        get_parent(class1=class1, class2=parent_class2,
                   storage=storage, path=path)
    return True


num = int(input())
for _ in range(num):
    string = input().split()
    write_in_storage(task=string, storage=storage)


num_of_requests = int(input())
sequence = list()
out = list()
for _ in range(num_of_requests):
    exception = input()
    if not sequence:
        sequence.append(exception)
        out.append(exception)
        continue
    for item in sequence:
        if get_parent(class1=item, class2=exception,
                            storage=storage, path=list()):
            if exception not in out:
                out.append(exception)
                print(exception)
                break
            else:
                break
    sequence.append(exception)




# storage = dict()


# def write_in_storage(task: str, storage: dict)->None:
#     key = task[0]
#     values = task[2:]
#     storage[key] = values


# num = int(input())
# for _ in range(num):
#     string = input().split()
#     write_in_storage(task=string, storage=storage)


# num_of_requests = int(input())
# sequence = list()
# for _ in range(num_of_requests):
#     exception = input()
#     if not sequence:
#         sequence.append(exception)
#         continue
#     if not storage[exception]:
#         sequence.append(exception)
#         continue
#     for item in sequence:
#         if item in storage[exception]:
#             print(exception)
#             break
#     sequence.append(exception)

