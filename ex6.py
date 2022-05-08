import math


def theNetwork(age, weight, height):
    h1 = (-0.46122 * age) + (0.97314 * weight) + (-0.39203 * height) + 1 * 0.80109
    act1 = 1 / (1 + math.exp(-h1))
    h2 = (0.78548 * age) + (2.10584 * weight) + (-0.57847 * height) + (1 * 0.43529)
    act2 = 1 / (1 + math.exp(-h2))
    output = (-0.81546 * act1) + (1.03775 * act2) - 1 * 0.2368
    return output


print(theNetwork(23, 75, 176))