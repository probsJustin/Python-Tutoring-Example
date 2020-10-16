


test_param0 = "first"
test_param1 = "second"

def test_function(function_param0, function_param1):
    print("I got at pos 0 " + function_param0)
    print("I got at pos 1 " + function_param1)
    return (function_param0 + function_param1)


def function_a():
    return 1

def function_b():
    return 2

def function_add(a, b):
    return a + b

print(function_a() + function_b())

print(function_add("things ","four "))

