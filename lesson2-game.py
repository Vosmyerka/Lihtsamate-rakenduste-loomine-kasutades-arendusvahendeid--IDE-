map1 =  [
    [12, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 24]
]
map2 = [
    [12, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 24]
]
map = map2

# 1. step
print("-------")

current_position_x = 0
current_position_y = 0

print("current_position_x = ", current_position_x)
print("current_position_y = ", current_position_y)
can_move_right = map[current_position_y][current_position_x+1] == 0
can_move_bottom = map[current_position_y+1][current_position_x] == 0

if can_move_right:
    print("Should move right")
    current_position_x = current_position_x + 1
if can_move_bottom:
    print("Should move down")
    current_position_y = current_position_y + 1

# 2. step
print("current_position_x = ", current_position_x)
print("current_position_y = ", current_position_y)
can_move_right = map[current_position_y][current_position_x+1] == 0
can_move_bottom = map[current_position_y+1][current_position_x] == 0

if can_move_right:
    print("Should move right")
    current_position_x = current_position_x + 1
if can_move_bottom:
    print("Should move down")
    current_position_y = current_position_y + 1

# 3. step
print("current_position_x = ", current_position_x)
print("current_position_y = ", current_position_y)
can_move_right = map[current_position_y][current_position_x+1] == 0
can_move_bottom = map[current_position_y+1][current_position_x] == 0

if can_move_right:
    print("Should move right")
    current_position_x = current_position_x + 1
if can_move_bottom:
    print("Should move down")
    current_position_y = current_position_y + 1

# 4. step
print("current_position_x = ", current_position_x)
print("current_position_y = ", current_position_y)
can_move_right = map[current_position_y][current_position_x+1] == 0
can_move_bottom = map[current_position_y+1][current_position_x] == 0

if can_move_right:
    print("Should move right")
    current_position_x = current_position_x + 1
if can_move_bottom:
    print("Should move down")
    current_position_y = current_position_y + 1

#5. step
print("current_position_x = ", current_position_x)
print("current_position_y = ", current_position_y)
can_move_right = map[current_position_y][current_position_x+1] == 0
can_move_bottom = map[current_position_y+1][current_position_x] == 0

if can_move_right:
    print("Should move right")
    current_position_x = current_position_x + 1
if can_move_bottom:
    print("Should move down")
    current_position_y = current_position_y + 1


if map[current_position_y][current_position_x] == 24:
    print("Finish")
    print("-------")
