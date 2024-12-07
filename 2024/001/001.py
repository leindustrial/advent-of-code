list_left = []
list_right = []
list_dist = []

def get_similarity_score():
    similarity_score = 0
    for num in list_left:
        count = list_right.count(num)
        similarity_score += num * count
    print (f'Similarity score: {similarity_score}')  


def get_total_distance():
    length = len(list_left)
    total_dist = 0
    for i in range(length):
        dist = list_left[i]-list_right[i]
        if dist < 0:
            dist *= -1
        list_dist.append(dist)
    # print (f'Dist list: {list_dist}')
    for num in list_dist:
        total_dist += num
    print (f'Total distance: {total_dist}')


def sort_lists():
    list_left.sort()
    list_right.sort()
    # for num in list_right:
    #     print (num)

def parse_input():
    with open('numbers.txt', 'r') as input:
        for line in input:
            num = line.split()
            list_left.append(int(num[0]))
            list_right.append(int(num[1]))
            # print (f'Left list: {list_left}')
            # print (f'Right list: {list_right}')

def main():
    # PART 1:
    parse_input()
    sort_lists()
    get_total_distance()
    # PART 2:
    get_similarity_score()

if __name__ == '__main__':
    main()