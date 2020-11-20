with open('AOC_Day1_PT2_2019_Puzzle_Source') as f:
    lines = f.read().splitlines()

total_fuel = 0

def do_fuel_calc(func_input_mass):
    return ((func_input_mass - func_input_mass % 3)/3 -2)

def checkForMass_zero(func_input_mass):
    if(do_fuel_calc(func_input_mass) >= 0):
        return do_fuel_calc(func_input_mass)
    else:
        return False



total_test_fuel = 0

for x in lines:
    x = int(x)
    while(True):
        if (checkForMass_zero(x) is not False):
            x = do_fuel_calc(x)
            total_test_fuel = total_test_fuel + x
        else:
            x = x
            break

print(total_test_fuel)