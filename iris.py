# lenghts = {"specie_name": (sepal_lenght, count)}
lenghts = {}

with open('iris.csv', 'r', encoding='utf-8') as f:
    for line in f:
        if line[0].isdigit():
            cols = line.split(',')
            sepal_lenght = float(cols[0])
            specie_name = cols[4].replace('\n', '')
            if specie_name in lenghts:
                curr_sum, curr_n = lenghts[specie_name]
                curr_sum += sepal_lenght
                curr_n +=1
                lenghts[specie_name] = (curr_sum, curr_n)
            else:
                lenghts[specie_name] = (sepal_lenght, 1)
assert len(lenghts) > 0

print(lenghts)

for spec in lenghts.keys():
    sum_lenghts, num = lenghts[spec]
    avg_lenght = sum_lenghts / num
    lenghts[spec] = avg_lenght

max_len = 0
max_spec_name = ''

for spec_name, avg_len in lenghts.items():
    if avg_len > max_len:
        max_len = avg_len
        max_spec_name = spec_name

# passed = False
# assert passed

print(f'Max length species name is {max_spec_name}, avg length = {max_len}')