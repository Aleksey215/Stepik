date = '2023-04-16'

# start_time = list()
# for hour in range(0, 24, 6):
#     hour = str(hour)
#     if len(hour) == 1:
#         hour = '0' + hour
#     start_time.append(f'{date} {str(hour)}:00:00')
# print(start_time)
# print()
# end_time = list()
# for hour in range(5, 24, 6):
#     hour = str(hour)
#     if len(hour) == 1:
#         hour = '0' + hour
#     end_time.append(f'{date} {str(hour)}:59:59')
# print(end_time)

for num in range(24):
    num = str(num)
    if len(num) == 1:
        num = '0' + num
    time_start = f'{num}:00:00'
    time_end = f'{num}:59:59'
    query = f"""
    select
        *
    from
        table
    where 
        `datetime` BETWEEN '{date} {time_start}' and '{date} {time_end}'
    """
    print(query)


class MyIterator:
    def __init__(self):
        self.data = [0, 1, 2, 3, 4]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        result = self.data[self.index]
        self.index += 1
        return result

for i in MyIterator():
    print(i)