
def parse_input():
    ordering_rules = []
    updates = []
    with open ('input.txt', 'r') as file:
        content = file.read().strip()
        part1, part2 = content.split('\n\n')

        for line in part1.splitlines():
            ordering_rules.append([int(num) for num in line.split('|')])
        
        for line in part2.splitlines():
            updates.append([int(num) for num in line.split(',')])

        return (ordering_rules, updates)

def is_valid(ordering_rules, update):
    for rule in ordering_rules:
        if rule[0] in update and rule[1] in update:
            i = update.index(rule[0])
            j = update.index(rule[1])
            if i > j:
                return False
    return True

def check(ordering_rules, updates):
    middle_num_sum = 0
    for update in updates:
        if is_valid(ordering_rules, update):
            print (update[len(update) // 2])
            middle_num_sum += update[len(update) // 2]
                
    return (middle_num_sum)

def fix(ordering_rules, updates):
    middle_num_sum_fixed = 0

    for update in updates:
        if not is_valid(ordering_rules, update):
            while not is_valid(ordering_rules, update):
                for rule in ordering_rules:
                    if rule[0] in update and rule[1] in update:
                        i = update.index(rule[0])
                        j = update.index(rule[1])
                        if i > j:
                            update.pop(i)
                            update.insert(j, rule[0])
            print (update[len(update) // 2])
            middle_num_sum_fixed += update[len(update) // 2]


    return(middle_num_sum_fixed)

def main():
    middle_num_sum = 0
    middle_num_sum_fixed = 0
    ordering_rules, updates = parse_input()

    # PART 1:
    middle_num_sum = check(ordering_rules, updates)
    print(f'Middle num sum: {middle_num_sum}')

    # PART 2:
    middle_num_sum_fixed = fix(ordering_rules, updates)
    print(f'Middle num sum (fixed updates): {middle_num_sum_fixed}')
    
if __name__ == '__main__':
    main()