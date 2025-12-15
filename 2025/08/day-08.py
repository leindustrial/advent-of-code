input_file_path = "./input.txt"
input_content = []

def check_input():
    with open(input_file_path, 'r') as file:
        for line in file:
            input_content.append(line.strip())
    print(input_content)

def part_1():
    
    result = 0
    print (f'Result 1: {result}')

def part_2():
    input_content2 = [list(line) for line in input_content]

    result = 0
    print (f'Result 2: {result}')

def main():
    check_input()
    part_1()
    part_2()


if __name__ == '__main__':
    main()