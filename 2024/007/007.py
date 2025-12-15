from itertools import product

def parse_input():
    data = []

    with open ('input.txt', 'r') as file:
        input = file.read().strip()
        for line in input.splitlines():
            key, value = line.split(':')
            key = (int(key.strip()))
            value = list(map(int, value.strip().split()))
            data.append((key, value))
    return (data)

def evaluate_data(data):
    result = 0

    for key, value in data:
        # print(f"Evaluating {key}: {value}")
        length = len(value) - 1
        if length < 1:
            continue
        combinations = product('+*', repeat=length)

        for combination in combinations:
            if calculate(value, combination) == key:
                # print(f"Match found for key {key}: {value}, {combination}")
                result += key
                # print (result)
                break
    return (result)

def evaluate_data2(data):
    result = 0

    for key, value in data:
        # print(f"Evaluating {key}: {value}")
        length = len(value) - 1
        if length < 1:
            continue
        operators = ['+', '*', '||']
        combinations = product(operators, repeat=length)

        for combination in combinations:
            if calculate2(value, combination) == key:
                # print(f"Match found for key {key}: {value}, {combination}")
                result += key
                # print (result)
                break
    return (result)

def calculate(value, combination):
    calc = value[0]
    for i, sign in enumerate(combination):
        if sign == '+':
            calc += value[i + 1]
        elif sign == '*':
            calc *= value[i + 1]
    # print (calc)
    return (calc)

def calculate2(value, combination):
    calc = value[0]
    for i, sign in enumerate(combination):
        if sign == '+':
            calc += value[i + 1]
        elif sign == '*':
            calc *= value[i + 1]
        elif sign == '||':
            calc = int(str(calc) + str(value[i + 1]))
    # print (calc)
    return (calc)


def main():
    result = 0
    result2 = 0
    data = []
    data = parse_input()
    # print (data)
    result = evaluate_data(data)
    print (f'\nPART 1:\nTotal calibration result: {result}\n')
    result2 = evaluate_data2(data)
    print (f'\nPART 2:\nTotal calibration result: {result2}\n')

if __name__ == '__main__':
    main()
