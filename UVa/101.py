n = int(input())
block_world = {i:[i] for i in range(n)}
pos = {i: i for i in range(n)}


def return_pile(i):
    while True:
        if block_world[pos[i]][-1] != i:
            j = block_world[pos[i]].pop()
            block_world[j].append(j)
            pos[j] = j
        else:
            break

def move_onto(a,b):
    return_pile(b)
    move_over(a, b)

def move_over(a, b):    
    return_pile(a)
    block_world[pos[a]].pop()
    block_world[pos[b]].append(a)
    pos[a] = pos[b]

def pile_onto(a, b):
    return_pile(b)
    pile_over(a, b)

def pile_over(a, b):
    pos_a_in_list = block_world[pos[a]].index(a)
    block_world[pos[b]] += block_world[pos[a]][pos_a_in_list:]
    pos_a = pos[a]
    for i in block_world[pos_a][pos_a_in_list:]:
        pos[i] = pos[b]
    block_world[pos_a] = block_world[pos_a][:pos_a_in_list]

def parse_cmd(cmd):
    act1 = cmd[0]
    act2 = cmd[2]
    a = int(cmd[1])
    b = int(cmd[3])
    if pos[a] == pos[b]:
        return
    if (act1 == 'move') and (act2 == 'onto'):
        move_onto(a, b)
    elif (act1 == 'move') and (act2 == 'over'):
        move_over(a, b)
    elif (act1 == 'pile') and (act2 == 'onto'):
        pile_onto(a, b)
    else:
        pile_over(a, b)

def print_block_world():
    for k, v in block_world.items():
        if not v:
            print('{}:'.format(k))
        else:
            print('{}: {}'.format(k, str(v)[1:-1].replace(',', '')))

while True:
    cmd = input()
    if cmd == 'quit':
        break
    else:
        parse_cmd(cmd.split())

print_block_world()
