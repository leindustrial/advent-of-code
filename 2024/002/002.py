




def main():
    safe_reports = 0
    extra_reports = 0

    with open ('numbers.txt') as input:
        for line in input:
            chars = line.split()
            nums = []
            for char in chars:
                nums.append(int(char))
            # print (nums)
            length = len(nums)
            is_increasing = True
            for i in range(length - 1):
                if nums[i] <= nums[i + 1] or (abs(nums[i] - nums[i + 1]) > 3):
                    is_increasing = False
            is_decreasing = True     
            for i in range(length - 1):
                if nums[i] >= nums[i + 1] or (abs(nums[i] - nums[i + 1]) > 3):
                    is_decreasing = False
            if is_increasing or is_decreasing:
                safe_reports += 1
            else:
                for j in range(length):
                    temp_nums = nums[:j] + nums[j+1:]
                    is_temp_increasing = True
                    for i in range(length - 2):
                        if temp_nums[i] <= temp_nums[i + 1] or (abs(temp_nums[i] - temp_nums[i + 1]) > 3):
                            is_temp_increasing = False
                    is_temp_decreasing = True
                    for i in range(length - 2):
                        if temp_nums[i] >= temp_nums[i + 1] or (abs(temp_nums[i] - temp_nums[i + 1]) > 3):
                            is_temp_decreasing = False
                    if is_temp_increasing or is_temp_decreasing:
                        extra_reports += 1
                        break

    print (f'Safe reports: {safe_reports}')
    print (f'Extra reports: {extra_reports}')
    total = safe_reports + extra_reports
    print (f'Total safe reports: {total}')

if __name__ == '__main__':
    main()