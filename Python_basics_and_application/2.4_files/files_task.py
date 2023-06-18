with open('dataset_24465_4.txt', 'r') as f, open('answer.txt', 'w') as ans:
    l = list()
    for line in f:
        line = line.rstrip()
        l.append(line)
    l.reverse()
    contents = '\n'.join(l)
    ans.write(contents)
