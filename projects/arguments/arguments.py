
def positional_parameter_add(a, b):
    return a+b

def many_positional_parameters_add(*args):
    output = 0
    for i in args:
        output += i
    return output

def positional_mix_add(a, b, *args):
    output = a + b
    for i in args:
        output += i
    return output

def keyword_parameter_add(a=0, b=0):
    return a + b

def many_keyword_parameters_add(**kwargs):
    output = 0
    for i in kwargs.values():
        output += i
    return output

