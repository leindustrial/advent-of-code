import re

def main():
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    # input_string = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    with open ('input.txt', 'r') as file:
        input_string = file.read()
        numbers = re.findall(pattern, input_string)
        result = 0
        for match in numbers:
            num1, num2 = match
            result += int(num1) * int(num2)
            
        print (f'Result: {result}')

        # PART2:
        pattern2 = r'(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\))'
        on = True
        result2 = 0
        numbers2 = re.findall(pattern2, input_string)
        for match2 in numbers2:
            string, num1, num2 = match2
            if string == 'do()':
                on = True
            elif string == "don't()":
                on = False
            elif string.startswith('mul') and on:
                result2 += int(num1) * int(num2)
        
        print (f'Precise result: {result2}')

if __name__ == '__main__':
    main()