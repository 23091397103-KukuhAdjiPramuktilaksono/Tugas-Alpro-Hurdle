def turn_right():
    turn_left()
    turn_left()
    turn_left()

def loncat():
    trun_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    move()

while not at_goal():
    if wall_in_front():
        loncat()
    else:
        move()            