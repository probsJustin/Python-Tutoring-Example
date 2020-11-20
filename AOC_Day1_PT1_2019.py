with open('AOC_Day1_PT1_2019_Puzzle_Source') as f:
    lines = f.read().splitlines()

total_fuel = 0

for x in lines:
    x = int(x)
    total_fuel = total_fuel + ((x - x % 3)/3 -2)

print(total_fuel)



test_list = list()
test_list.append(12)
test_list.append(14)
test_list.append(1969)
test_list.append(100756)

total_test_fuel = 0

for individual_line in test_list:
    total_test_fuel = total_test_fuel + ((individual_line - individual_line % 3)/3 - 2)

print(total_test_fuel)