#function turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#function round corner
def round_corner():
    turn_right()
    move()
    turn_right()

#function jump
def jump():
    turn_left()
    while wall_on_right():
        move()
        round_corner()
    while front_is_clear():
        move()
        turn_left()

#pengkondisian ketika belum selesai
while not at_goal():
    jump()
else:
    move()
    