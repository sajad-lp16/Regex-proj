import re
import os

wd = os.listdir('.')
wd.remove('data.py')
targets = [file for file in wd]
pat = r'.*\s([-\d\.]+)\skcal/mol'
data = {}
for target in targets:
    with open(target, 'r') as file:
        tmp = file.readlines()[1]

    res = re.search(pat, tmp)
    data[target] = float(res.group(1))

grouped_data = list(zip(data.values(), data.keys()))
sorted_data = sorted(grouped_data, key=lambda x: x[0])
max_data_values = sorted_data[:20]

for item in max_data_values:
    print(str(max_data_values.index(item) + 1), ' = ', item[0], '   --->   ',
          item[1])

with open('../result.log', 'w') as file:
    for item in max_data_values:
        text = str(max_data_values.index(item) + 1)+ ' = ' + str(
            item[0]) + '   --->   ' + item[1] + '\n\n'
        file.write(text)

input()
