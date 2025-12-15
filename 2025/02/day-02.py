input_file_path = "./input.txt"
ids_ranges = []

def check_input():
    with open(input_file_path, 'r') as file:
        for ids_range in file:
            ids_ranges.extend(ids_range.split(','))
    # print(ranges)

def check_ranges_1():
    result = 0
    for ids_range in ids_ranges:
        start,end = [int(i) for i in ids_range.split('-')]
        id_numbers = [i for i in range(start, end + 1)]
        for id_number in id_numbers:
            str_number = str(id_number)
            if str_number[:len(str_number)//2] == str_number[len(str_number)//2:]:
                # print (str_number)
                result += id_number
    print (f' Result 1: {result}')

def check_ranges_2():
    result = 0
    for ids_range in ids_ranges:
        start,end = [int(i) for i in ids_range.split('-')]
        id_numbers = [i for i in range(start, end + 1)]
        for id_number in id_numbers:
            str_number = str(id_number)
            strlen = len(str_number)
            # print (str_number)
            for i in range(1, (strlen // 2) + 1):
                str_part = str_number[:i]
                # print (str_part)
                if str_part * (strlen // i) == str_number:
                    result += id_number
                    break
    print (f' Result 2: {result}')

def main():
    check_input()
    check_ranges_1()
    check_ranges_2()

if __name__ == '__main__':
    main()