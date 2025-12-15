input_file_path = "./input.txt"
input_content = []

def check_input():
    with open(input_file_path, 'r') as file:
        for line in file:
            input_content.append(line.strip())
    # print(input_content)

def find_joltage_1():
    result = 0
    for line in input_content:
        battery1 = max(line[:-1])
        i = line.index(battery1)
        battery2 = max(line[i+1:])
        joltage = int(battery1 + battery2)
        # print (joltage)
        result += joltage
    print (f'Result1: {result}')

def find_joltage_2():
    result = 0
    for line in input_content:
        joltage = ""
        start = 0
        for j in range(12):
            # print(f'Line: {line}')
            end = len(line) - 11 + j
            search_line = line[start:end]
            # print(end)
            battery = max(search_line[:end])
            i = start + search_line.index(battery)
            joltage = joltage + battery
            start = i + 1
        # print (joltage)
        result += int(joltage)
    print (f'Result2: {result}')

def main():
    check_input()
    find_joltage_1()
    find_joltage_2()

if __name__ == '__main__':
    main()