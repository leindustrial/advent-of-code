
input = []
with open ('input.txt') as file:
    for line in file:
        input.append(line.strip())
word = 'XMAS'
word_len = len(word)
rows = len(input)
cols = len(input[0])

def find_word(x, y):
    count = 0
    for row in range(rows):
        for col in range(cols):
            if 0 <= row + x * (word_len - 1) < rows and 0 <= col + y * (word_len - 1) < cols:
                    match = True
                    for i in range(word_len):
                        if input[row + x * i][col + y * i] != word[i]:
                            match = False
                            break
                    if match:
                        count += 1
    return (count)

def find_x():
    count = 0
    for row in range (1, rows - 1):
        for col in range(1, cols - 1):
            if input[row][col] == 'A':
                if (input[row - 1][col - 1] == 'M' and
                    input[row + 1][col + 1] == 'S' and
                    input[row + 1][col - 1] == 'S' and
                    input[row - 1][col + 1] == 'M'):
                    count += 1
                if (input[row - 1][col - 1] == 'S' and
                    input[row + 1][col + 1] == 'M' and
                    input[row + 1][col - 1] == 'M' and
                    input[row - 1][col + 1] == 'S'):
                    count += 1
                if (input[row - 1][col + 1] == 'M' and
                    input[row + 1][col - 1] == 'S' and
                    input[row - 1][col - 1] == 'S' and
                    input[row + 1][col + 1] == 'M'):
                    count += 1
                if (input[row - 1][col + 1] == 'S' and
                    input[row + 1][col - 1] == 'M' and
                    input[row - 1][col - 1] == 'M' and
                    input[row + 1][col + 1] == 'S'):
                    count += 1
    return (count)

def main():
    xmas_count = 0

    # PART 1:
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (-1, 1),
        (1, -1)
    ]
    for x, y in directions:
        xmas_count += find_word(x, y)
    print (f'Part 1: {xmas_count}')

    # PART 2:
    x_shape_count = 0
    x_shape_count = find_x()
    print (f'Part 2: {x_shape_count}')

if __name__ == '__main__':
    main()