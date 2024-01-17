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
