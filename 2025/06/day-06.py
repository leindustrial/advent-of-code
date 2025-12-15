input_file_path = "./input.txt"
input_content = []

def check_input():
    with open(input_file_path, 'r') as file:
        for line in file:
            input_content.append(line.split())
    # print(input_content)

def part_1():
    result = 0
    # problems = []
    # print(input_content[0])
    # length = len(input_content[0])
    # print (length)

    for x in range(len(input_content[0])):
        op = input_content[-1][x]

        total = int(input_content[0][x])
        # print (f'First num: {total}')

        for y in range(1, len(input_content) - 1):
            if op == '+':
                total += int(input_content[y][x])
                # print (f'Next num: {op} {input_content[y][x]}')
            if op == '*':
                total *= int(input_content[y][x])
                # print (f'Next num: {op} {input_content[y][x]}')
            # print (total)
        result += total
    # for item in input_content:

    print (f'Result 1: {result}')

def part_2():
    result = 0
    print (f'Result 2: {result}')

def main():
    check_input()
    part_1()
    part_2()


if __name__ == '__main__':
    main()