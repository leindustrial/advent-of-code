input_file_path = "./input.txt"
input_content = []

def check_input():
    with open(input_file_path, 'r') as file:
        for line in file:
            input_content.append(line.strip())
    # print(input_content)

def part_1():
    result = 0
    neighbours = 0
    for y in range(len(input_content)):
        for x in range(len(input_content[0])):
            if input_content[y][x] == '@':
                if y > 0:
                    if (x - 1) >= 0:
                        if input_content[y-1][x-1] == '@': 
                            neighbours += 1
                    if input_content[y-1][x] == '@': 
                        neighbours += 1
                    if (x + 1) < len(input_content[0]):
                        if input_content[y-1][x+1] == '@': 
                            neighbours += 1
                if (y + 1) < len(input_content):
                    if (x - 1) >= 0:
                        if input_content[y+1][x-1] == '@': 
                            neighbours += 1
                    if input_content[y+1][x] == '@': 
                        neighbours += 1
                    if (x + 1) < len(input_content[0]):
                        if input_content[y+1][x+1] == '@': 
                            neighbours += 1
                if (x - 1) >= 0:
                    if input_content[y][x-1] == '@': 
                        neighbours += 1
                if (x + 1) < len(input_content[0]):
                    if input_content[y][x+1] == '@': 
                        neighbours += 1
                # print (f'Neighbours{y},{x}: {neighbours}')
                if neighbours < 4:
                    result += 1
                    # print (f'Result{y},{x}: {result}')
                neighbours = 0

    print (f'Result 1: {result}')

def part_2():
    input_content2 = [list(line) for line in input_content]
    result = 0
    neighbours = 0
    removed = 1
    while removed > 0:
        removed = 0
        for y in range(len(input_content2)):
            for x in range(len(input_content2[0])):
                if input_content2[y][x] == '@':
                    if y > 0:
                        if (x - 1) >= 0:
                            if input_content2[y-1][x-1] == '@': 
                                neighbours += 1
                        if input_content2[y-1][x] == '@': 
                            neighbours += 1
                        if (x + 1) < len(input_content2[0]):
                            if input_content2[y-1][x+1] == '@': 
                                neighbours += 1
                    if (y + 1) < len(input_content2):
                        if (x - 1) >= 0:
                            if input_content2[y+1][x-1] == '@': 
                                neighbours += 1
                        if input_content2[y+1][x] == '@': 
                            neighbours += 1
                        if (x + 1) < len(input_content2[0]):
                            if input_content2[y+1][x+1] == '@': 
                                neighbours += 1
                    if (x - 1) >= 0:
                        if input_content2[y][x-1] == '@': 
                            neighbours += 1
                    if (x + 1) < len(input_content2[0]):
                        if input_content2[y][x+1] == '@': 
                            neighbours += 1
                    # print (f'Neighbours{y},{x}: {neighbours}')
                    if neighbours < 4:
                        result += 1
                        removed += 1
                        # print (removed)
                        input_content2[y][x] = 'x'
                        # print (f'Result{y},{x}: {result}')
                    neighbours = 0
    print (f'Result 2: {result}')

def main():
    check_input()
    part_1()
    part_2()


if __name__ == '__main__':
    main()