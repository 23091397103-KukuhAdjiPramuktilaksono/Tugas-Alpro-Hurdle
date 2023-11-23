#Tugas Alpro Hurdle 2

def turn_right(): 
    turn_left()
    turn_left()
    turn_left()

def jalan():
    move()
    turn_left()

def lompat():
    move()
    turn_right()

def turun():
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    jalan()
    lompat()
    turun()