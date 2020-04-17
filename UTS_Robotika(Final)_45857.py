import turtle
import time
import sys

'''
Tugas UTS Instrumentasi Sistem Robotika
Mahatma Ageng Wisesa 
17/411372/TK/45857
'''
win = turtle.Screen()
win.bgcolor('#ffffff')
win.setup(620,620)

grid = 21  # grid pixels 

class wall(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')         
        self.color('#636363')           
        self.penup()                    
        self.speed(0)

class objective(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('yellow')
        self.penup()
        self.speed(0)

class robot(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('arrow')
        self.shapesize(0.4, 0.4, 0.4)
        self.color('red')
        self.setheading(270)
        #self.penup()
        self.pensize(1)
        self.speed(0)

    def go_left(self):
        if (self.heading() == 0):                           # Jika robot ngarah ke timur
            x_robot = round(robot.xcor(),0)
            y_robot = round(robot.ycor(),0)

            if (x_robot, y_robot) in finish:                # Robot jika di titik Finish
                print('FINISHED')
                stop()                                      # Break loop

            if (x_robot, y_robot+grid) not in walls:        # Jika tidak ada tembok di kiri (ada di list tembok)
                self.left(90)                               # Putar ke kiri 90 derajar
                self.forward(grid)                          # Maju sejauh satu langkah
            else:                                           # Jika ada tembok di kiri
                if(x_robot+grid, y_robot) not in walls:     # Jika tidak ada tembok di depan (tidak ada list tembok)
                    self.forward(grid)                      # Maju sejauh grid
                else:                                       # Jika ada tembok di depan
                    self.right(90)                          # Putar ke kanan 90 derajat

    def go_right(self):
        if (self.heading() == 180):                         # Jika robot ngarah ke barat
            x_robot = round(robot.xcor(),0)
            y_robot = round(robot.ycor(),0)
            
            if (x_robot, y_robot) in finish:                # Robot jika di titik Finish
                print('FINISHED')
                stop()                                      # Break loop

            if (x_robot, y_robot-grid) not in walls:
                self.left(90)                               # Putar ke kiri 90 derajar
                self.forward(grid)                          # Maju sejauh satu langkah
            else:                                           # Jika  ada tembok di kiri
                if(x_robot-grid, y_robot) not in walls:
                    self.forward(grid)
                else:
                    self.right(90)

    def go_up(self):
        if (self.heading() == 90):
            x_robot = round(robot.xcor(),0)
            y_robot = round(robot.ycor(),0)

            if (x_robot, y_robot) in finish:
                print('FINISHED')
                stop()
            
            if (x_robot-grid, y_robot) not in walls:
                self.left(90)
                self.forward(grid)
            else:
                if(x_robot, y_robot+grid) not in walls:
                    self.forward(grid)
                else:
                    self.right(90)

    def go_down(self):
        if (self.heading() == 270):
            x_robot = round(robot.xcor(),0)
            y_robot = round(robot.ycor(),0)

            if (x_robot, y_robot) in finish:
                print('FINISHED')
                stop()

            #if (not((x_robot+grid, y_robot) in walls)) and ((x_robot, y_robot-grid) not in walls):
            #    self.forward(grid)
            if (x_robot+grid, y_robot) not in walls and (x_robot, y_robot-grid) not in walls and (x_robot-grid, y_robot) not in walls and (x_robot+grid, y_robot+grid) not in walls:
                self.forward(grid) # jika tidak ada tembok di kiri, kanan, dan belakang kiri
            else:
                if (x_robot+grid, y_robot) not in walls:
                    self.left(90)
                    self.forward(grid)
                else:
                    if (x_robot, y_robot-grid) not in walls:
                        self.forward(grid)
                    else:
                        self.right(90)

# bentuk matrix

box = [
"+++++++++++++++++++++++++++++",
"+        +                  +",
"+        +                  +",
"+        +                  +",
"+++++++  +                  +",
"e     +      ++++   +++++++++",
"+     +      +              +",
"+     +      +              +",
"+     +      +              +",
"+     +      +              +",
"+     +      ++++++++++++++++",
"+     +        +   +        +",
"+     +        +   +        +",
"++++  +                     +",
"+  +  +       s             +",
"+  +  +        +   +        +",
"+  +  ++++++++++   ++++++++++",
"+  +                        +",
"+  +                        +",
"+  +  +++++++++++++++++++++++",
"+  +  +           +         +",
"+  +  +                     +",
"+  +  +                     +",
"+  +  +++++   +++++         +",
"+                 +         +",
"+                 +         +",
"+                 +         +",
"+                 +         +",
"+++++++++++++++++++++++++++++",
]

def setupWall(box):
    for y in range(len(box)):                           # ekstrak karakter baris Array 'box'
        for x in range(len(box[y])):                    # ekstrak karakter kolom Array 'box'
            char = box[y][x]                            # karakter setiap baris setiap kolom  
            x_win = -298 + (x*grid)                     # koordinat x tembok
            y_win = 298 - (y*grid)                      # koordinat y tembok
            
            if char == "+":                             # jika dalam kolom setap baris ada '+'
                wall_set.goto(x_win, y_win)             # set tembok ke koordinat sesuai baris
                wall_set.stamp()                        # stamp setiap iterasi objek wall win    
                walls.append((x_win, y_win))            # masukan koordinat ke list walls

            if char == "e":                             # jika dalam kolom setap baris ada 'e'
                objective.goto(x_win, y_win)            # set tembok ke koordinat sesuai baris
                objective.stamp()                       # stamp setiap iterasi objek exit ke win 
                finish.append((x_win, y_win))           # masukan koodinat ke list finish

            if char == "s":                             # jika terdapat karakter 's' set ke koordinat itu
                robot.goto(x_win, y_win) 

run = True

def stop():
    run = False                                         # break infinite loop jika terpenuhi
    win.exitonclick()                   
    sys.exit()                      

wall_set = wall()
robot = robot()
objective = objective()

walls = []
finish = []

setupWall(box)

while run:                                              # infinite loop sampai fungsi stop dieksekusi atau finish tercapai
    robot.go_right()
    robot.go_down()
    robot.go_left()
    robot.go_up()

    time.sleep(0.03)