def fitness_1_1_A(out, expected):
    # print(out, expected)
    fit = 0
    if len(out) == 0:
        return -1000000.0
    elif 1 in out:
        return 0.0
    for i in range(len(expected)):
        fit += -abs(out[i] - expected[i])
    return fit


def fitness_1_1_B(out, expected):
    fit = 0
    if len(out) == 0:
        return -1000000.0
    elif 789 in out:
        return 0.0
    for i in range(len(expected)):
        fit += -abs(out[i] - expected[i])
    return fit


def fitness_1_1_C(out, expected):
    fit = 0
    if len(out) == 0:
        return -1000000.0
    elif 31415 in out:
        return 0.0
    for i in range(len(expected)):
        fit += -abs(out[i] - expected[i])
    return fit


def fitness_1_1_D(out, expected):
    fit = 0
    if len(out) == 0:
        return -1000000.0
    elif out[0] == 1:
        return 0.0
    else:
        fit += -abs(out[0] - 1)
    return fit


def fitness_1_1_E(out, expected):
    fit = 0
    if len(out) == 0:
        return -1000000.0
    elif out[0] == 789:
        return 0.0
    else:
        fit += -abs(out[0] - 789)
    return fit


def fitness_1_1_F(out, expected):
    fit = 0
    if len(out) == 0:
        return -1000000.0
    elif len(out) == 1 and out[0] == 1:
        return 0.0
    else:
        fit = -1000000.0
    return fit

fitness_functions = {
    "1_1_A": fitness_1_1_A,
    "1_1_B": fitness_1_1_B,
    "1_1_C": fitness_1_1_C,
    "1_1_D": fitness_1_1_D,
    "1_1_E": fitness_1_1_E,
    "1_1_F": fitness_1_1_F,
}

def get_fitness_function(fitness_function_name):
    return fitness_functions[fitness_function_name]
