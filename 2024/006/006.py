class Map:
    def __init__(self, map='', rows=0, cols=0, pos=None, dir=''):
        self.map = map
        self.rows = rows
        self.cols = cols
        self.pos = pos if pos is not None else []
        self.dir = dir

    def print_info(self):
        print(f"Map:\n{self.map}\nRows: {self.rows}\nCols: {self.cols}\nPlayer pos: {self.pos}\nPlayer dir: {self.dir}")
    
    def print_map(self):
        for line in self.map:
            print(line)

DIRECTIONS = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1),
}

TURN_RIGHT = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^',
}

def parse_map(map_obj):
    with open ('input.txt', 'r') as file:
        map_obj.map = file.read().strip().splitlines()
        map_obj.rows = len(map_obj.map)
        map_obj.cols = len(map_obj.map[0])
    for x, line in enumerate(map_obj.map):
        for y, char in enumerate(line):
            if char == '^' or char == 'v' or char == '>' or char == '<':
                map_obj.pos = [x ,y]
                map_obj.dir = char

def move_guard(map_obj):
    while True:
        x, y = map_obj.pos
        dx, dy = DIRECTIONS[map_obj.dir]
        nx, ny = x + dx, y + dy
        if (nx < 0 or nx >= map_obj.rows or ny < 0 or ny >= map_obj.cols):
            break
        if map_obj.map[nx][ny] == '#':
            map_obj.dir = TURN_RIGHT[map_obj.dir]
        else:
            row = list(map_obj.map[x])
            row[y] = 'X'
            map_obj.map[x] = ''.join(row)
            x, y = nx, ny
            map_obj.pos = [x, y]
            row = list(map_obj.map[x])
            row[y] = map_obj.dir
            map_obj.map[x] = ''.join(row)
            # print (map_obj.map)


def count_moves(map_obj):
    x_count = 0
    for line in map_obj.map:
        x_count+= line.count('X')
    return (x_count)

def add_obstructions(map_obj):
    # count = 0
    print ('Obstructions added on the map 2')
    obstruction_positions = []

    for x in range(map_obj.rows):
        for y in range(map_obj.cols):
            if map_obj.map[x][y] != '.' or [x, y] == map_obj.pos:
                continue
            save_char = map_obj.map[x][y]
            row = list(map_obj.map[x])
            row[y] = 'O'
            map_obj.map[x] = ''.join(row)

            if check_loop(map_obj):
                obstruction_positions.append((x, y))
                # count += 1
            
            row[y] =save_char
            map_obj.map[x] = ''.join(row)

    return (obstruction_positions)

def check_loop(map_obj):
    visited = set()
    x, y = map_obj.pos
    dir = map_obj.dir

    while True:
        state = x, y, dir
        if state in visited:
            return True
        visited.add(state)
        dx, dy = DIRECTIONS[dir]
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >=map_obj.rows or ny < 0 or ny >= map_obj.cols:
            # print ('out of bounds')
            break
        if map_obj.map[nx][ny] =='#':
            dir = TURN_RIGHT[dir]
        elif map_obj.map[nx][ny] =='O':
            dir = TURN_RIGHT[dir]
        else:
            x, y = nx, ny

    return False

def main():
    
    map_obj1 = Map()
    map_obj2 = Map()
    parse_map(map_obj1)
    parse_map(map_obj2)
    #map_obj1.print_info()

    # PART 1:
    print ('\nPART 1')
    x_count = 0
    move_guard(map_obj1)
    x_count = count_moves(map_obj1) + 1
    #map_obj1.print_map()
    print(f'Visited positions: {x_count}')

    # PART 2:
    print ('\nPART 2')
    x2_count = 0
    positions = []
    positions = add_obstructions(map_obj2)
    x2_count = len(positions)
    print(f'Obstructions added: {x2_count}')
    #map_obj2.print_map ()
    print ('\n')

if __name__ == '__main__':
    main()