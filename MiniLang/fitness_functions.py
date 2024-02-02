def fitness_1_1_A(out, expected, inputs):
    # print(out, expected)
    fit = 0
    if len(out) == 0:
        return -1000000.0
    elif 1 in out:
        return 0.0
    for i in range(len(expected)):
        fit += -abs(out[i] - expected[i])
    return fit


def fitness_1_1_B(out, expected, inputs):
    if len(out) == 0:
        return -1000000.0
    elif 789 in out:
        return 0.0
    # fit = 0
    # for i in range(len(expected)):
    #     fit += -abs(out[i] - expected[i])
    # return fit
    return -min([abs(x - 789) for x in out])


def fitness_1_1_C(out, expected, inputs):
    fit = 0
    if len(out) == 0:
        return -1000000.0
    elif 31415 in out:
        return 0.0
    for i in range(len(expected)):
        fit += -abs(out[i] - expected[i])
    return fit


def fitness_1_1_D(out, expected, inputs):
    fit = 0
    if len(out) == 0:
        return -1000000.0
    elif out[0] == 1:
        return 0.0
    else:
        fit += -abs(out[0] - 1)
    return fit


def fitness_1_1_E(out, expected, inputs):
    fit = 0
    if len(out) == 0:
        return -1000000.0
    elif out[0] == 789:
        return 0.0
    else:
        fit += -abs(out[0] - 789)
    return fit


def fitness_1_1_F(out, expected, inputs):
    fit = 0
    if len(out) == 0:
        return -1000000.0
    elif len(out) == 1 and out[0] == 1:
        return 0.0
    else:
        fit = -len(out) * 10
    return fit

def fitness_1_2_A(out, expected, inputs):
    if len(out) == 1 and out[0] == expected[0]:
        return 0.0
    elif len(out) == 1:
        if out[0] in inputs:
            return -10.0
        else:
            return -1000.0
    elif len(out) > 1 and expected[0] in out:
        return len(out) * -20
    else:
        return len(out) * -100 if len(out) > 1 else -100000
    
    
def fitness_pass_2_inputs(out, expected, inputs):
    if len(out) == 0:
        return -1000000.0
    if len(out) == 2:
        if (out[0] == expected[0] and out[1] == expected[1]) or (out[0] == expected[1] and out[1] == expected[0]):
            return 0.0
        elif (out[0] == expected[0] and out[1] != expected[1]) or (out[0] != expected[0] and out[1] == expected[1]):
            return -10.0
        elif out[0] != expected[0] and out[1] != expected[1]:
            return -1000.0
    elif len(out) == 1:
        if out[0] == expected[0] or out[0] == expected[1]:
            return -100.0
        else:
            return -1010.0
    else:
        return abs(len(out) - len(expected)) * -10000 
        

def fitness_4_6_3(out, expected, inputs):
    if len(out) == len(expected) and all([x in expected for x in out]):
        return 0.0
    elif len(out) == len(expected) and not all([x in expected for x in out]):
        return -10.0
    elif len(out) != len(expected) and all([x in expected for x in out]):
        return -100.0
    else:
        return -1000.0

def fitness_1_3_B(out, expected, inputs):
    if len(out) == 0:
        return -50.0
    elif len(out) == 1 and out[0] == expected[0]:
        return 0.0
    elif len(out) == 1 and out[0] != expected[0]:
        if out[0] in inputs:
            return -20.0
        else:
            return -1000.0
    elif len(out) == 2 and out[0] in inputs and out[1] in inputs:
        if out[0] != out[1]:
            return -10.0
        return -15.0
    elif len(out) >=0 and any([x in inputs for x in out]):
        return len(out) * -100
    else:
        return len(out) * -1000 if len(out) > 1 else -100000
    
def fitness_int_float_sum(out, expected, inputs):
    if len(out) == 0:
        return -1000000.0
    elif len(out) == 2 and out[0] == expected[0] and out[1] == expected[1]:
        return 0.0
    elif len(out) == 2 and out[0] == expected[0] and out[1] != expected[1]:
        return -10.0
    elif len(out) == 2 and out[0] != expected[0] and out[1] == expected[1]:
        return -15.0
    elif len(out) == 2 and out[0] in expected and out[1] in expected and out[0] != out[1]:
        return -5.0
    elif len(out) == 2 and out[0] != expected[0] and out[1] != expected[1] and any([o in inputs for o in out]):
        return (out[0] in inputs) * -10 + (out[1] in inputs) * -10
    elif len(out) == 2:
        return -100.0
    elif len(out) == 1 and (out[0] == expected[0] or out[0] == expected[1]):
        return -100.0
    elif len(out) == 1 and out[0] not in expected and out[0] in inputs:
        return -1000.0
    elif len(out) == 1 and out[0] not in expected and out[0] not in inputs:
        return -10000.0
    else:
        return -100000.0
    
def fitness_9_6_8(out, expected, inputs):
    if len(out) == 0:
        return -100000000.0
    expected_len = len(expected)
    fit = 0
    for o_idx, o in enumerate(out):
        if o_idx >= expected_len:
            o_idx = o_idx % expected_len
        if o != expected[o_idx]:
            fit += -100
    return fit
        
def fitness_pass_inputs(out, expected, inputs):
    if len(out) == 0:
        return -1000000.0
    return sum([i not in out for i in inputs]) * -100 + sum([o not in inputs for o in out]) * -1000
    
def fitness_print_n_times(out, expected, inputs):
    if len(out) == 0:
        return -100000000.0
    return abs(len(out) - inputs[0]) * -1000

def fitness_boolean(out, expected, inputs):
    if len(out) == 0:
        return -1000000.0
    if len(out) == 1 and out[0] == expected[0]:
        return 0.0
    elif len(out) == 1 and out[0] != expected[0]:
        return abs(out[0] - expected[0]) * -100
    else:
        return len(out) * -1000
        

fitness_functions = {
    "1_1_A": fitness_1_1_A,
    "1_1_B": fitness_1_1_B,
    "1_1_C": fitness_1_1_C,
    "1_1_D": fitness_1_1_D,
    "1_1_E": fitness_1_1_E,
    "1_1_F": fitness_1_1_F,
    "1_2_A": fitness_1_2_A,
    "1_2_B": fitness_1_2_A,
    "1_2_C": fitness_1_2_A,
    "1_2_D": fitness_1_2_A,
    "1_2_E": fitness_1_2_A,
    "1_3_A": fitness_1_3_B,
    "1_3_B": fitness_1_3_B,
    "pass_2_inputs": fitness_pass_2_inputs,
    "4_6_3": fitness_4_6_3,
    "3_5_1": fitness_int_float_sum,
    "9_6_8": fitness_9_6_8,
    "pass_inputs": fitness_pass_inputs,
    "print_n_times": fitness_print_n_times,
    "1_1": fitness_boolean,
    "1_2": fitness_boolean,
    "2_1": fitness_boolean,
    "2_2": fitness_boolean,
    "2_3": fitness_boolean,
    "2_4": fitness_boolean,
}

def get_fitness_function(fitness_function_name):
    return fitness_functions[fitness_function_name]
