from gasp import *
begin_graphics(800, 600)
finished = False

def place_player ():
    print ("Here I am!")
   
    global x, y, shape
    x, y = 400, 300
shape = circle ((x, y), 10, filled=True, color=color. RED)
place_player()



def move_player():
    print("I'm moving...")
    update_when ('key_pressed') 

place_player ()

while True:
    key = update_when ('key_pressed')
    if key == 'Escape':
        break
    elif key == 'a':
        move_direction = (-1,0)
    elif key == 'w':
        move_direction = (0,1)
    elif key == 'd':
        move_direction = (1,0)
    elif key == 's':
        move_direction = (0,-1)
    elif key == 'q':
        move_direction = (0,0)
x, y = x + 20 * move_direction[0], y +20 * move_direction[1]
   

player_x +=(640 + (20 * move_direction[0])) % 640
player_y +=(480 + (20 * move_direction[0])) % 480
move_to(player_shape, (player_x, player_y))

end_graphics ()

