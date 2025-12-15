input_file_path = "./input.txt"
lines = []

def check_input() -> None:
    with open(input_file_path, 'r') as input_file:
        for input_line in input_file:
            lines.append(input_line.strip())

def open_safe_part1() -> None:
    position = 50
    result = 0
    for line in lines:
        if line.startswith('R'):
            position = (position + int(line[1:])) % 100
        elif line.startswith('L'):
            position = (position - int(line[1:])) % 100
        if position == 0:
            result += 1
        # print (position)
    print (f'Part1: {result}')

def open_safe_part2() -> None:
    position = 50
    result = 0
    rotations = 0
    for line in lines:
        num = int(line[1:])
        for i in range(num):
            if line.startswith('R'):
                position = (position + 1) % 100
            elif line.startswith('L'):
                position = (position - 1) % 100
            if position == 0:
                rotations +=1
        result += rotations
        rotations = 0
        # print (position)
    print (f'Part2: {result}')

def main():
    check_input()
    open_safe_part1()
    open_safe_part2()



if __name__ == '__main__':
    main()