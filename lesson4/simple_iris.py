lengths = {} #{"название вида": (len_sum, count)}

with open("iris.csv", "r", encoding="utf-8") as f:
    for line in f:
        if line[0].isdigit():
            columns = line.split(",")
            sepal_length = float(columns[0])
            specie_name = columns[4]
            if specie_name in lengths:
                curr_sum, curr_n = lengths[specie_name]
                curr_sum += sepal_length
                curr_n += 1
                lengths[specie_name] = (curr_sum, curr_n)
            else:
                lengths[specie_name] = (sepal_length, 1)

# Утверждаю: файл f прочитан и закрыт, в словаре lengths
# суммы длин лепестков и количества лепестков для каждого
# вида

for spec in lengths.keys():
    sum_length, num = lengths[spec]
    average_length = sum_length / num
    lengths[spec] = average_length

# Поиск максимальной длины
max_len = 0 # Максимальная длина
max_spec_name = "" # Название вида, у которого максим. длина
for spec_name, avg_len in lengths.items():
    if avg_len > max_len:
        max_len = avg_len
        max_spec_name = spec_name

print(f"Самый длинный средний лепесток у вида {max_spec_name}")


