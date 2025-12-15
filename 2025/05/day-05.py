input_file_path = "./input.txt"
input_content = []

def check_input():
    with open(input_file_path, 'r') as file:
        for line in file:
            input_content.append(line.strip())
    # print(input_content)

def part_1():
    result = 0
    ranges = []
    products = []
    is_range = True

    for item in input_content:
        if item == '':
              is_range = False
              continue
        if is_range:
             ranges.append(item.strip())
        else:
             products.append(item.strip())
    # print (ranges)
    # print (products)
    for product in products:
        for prod_range in ranges:
            start,end = [int(i) for i in prod_range.split('-')]
            
            if start <= int(product) <= end:
                result +=1
                # print (f'{product} is fresh in {prod_range}')
                break
    print (f'Result 1: {result}')

def part_2():
    result = 0
    ranges = []

    for item in input_content:
        if item != '':
              start,end = [int(i) for i in item.split('-')]
              ranges.append((start, end))
              ranges.sort()
        else:
             break
    # print (ranges)
    merged = []
    for prod_range in ranges:
        if not merged:
            merged.append(list(prod_range))
        start1, end1 = merged[-1]
        start2, end2 = prod_range
        if start2 <= end1 + 1:
            merged[-1][1] = max(end1, end2)
        else:
            merged.append(list(prod_range))
    print (merged)
    for item in merged:
        start, end = item
        diff = end - start
        if diff > 0:
             result += diff + 1
    
    # result = 0
    print (f'Result 2: {result}')

def main():
    check_input()
    part_1()
    part_2()


if __name__ == '__main__':
    main()