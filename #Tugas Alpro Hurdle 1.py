#Tugas Alpro Hurdle 1 

def turn_right(): 
    turn_left()
    turn_left()
    turn_left()

def lompat():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    lompat()