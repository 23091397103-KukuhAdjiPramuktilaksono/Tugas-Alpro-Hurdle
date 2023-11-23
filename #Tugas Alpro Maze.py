#function turn right
def turn_right():
     turn_left()
     turn_left()
     turn_left()

#pengkondisian ketika belum selesai finish
while not at_goal():
    if wall_on_right():
        if front_is_clear():
            move()
        elif wall_in_front():
            turn_left()
    elif right_is_clear():
        turn_right()
        move()