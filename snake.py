import turtle
import time
import random


delay = 0.1


c = input("Do you want to play(u) or watch the algorithm (a)play ? ") 


# Set up the screen
win = turtle.Screen()
win.title("SNAKE")
win.bgcolor("black")
win.setup(width=650, height=450)


box = turtle.Turtle()
box.speed(0)
box.shape("square")
box.color("red")
box.penup()
box.hideturtle()
box.goto(300, -200)
box.pendown()
box.goto(300, 200)
box.goto(-300, 200)
box.goto(-300, -200)
box.goto(300, -200)
box.penup()


win.tracer(0) 
# Turns off the screen updates


# Snake head
head = turtle.Turtle()
head.speed(0)
turtle.register_shape("sq", ((0,0), (0,20), (20,20),(20,0)))
head.shape("sq")
head.color("green")
head.penup()
head.goto(-300,-180)
head.direction = "stop"


# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("sq")
food.color("blue")
food.penup()
food.goto(0,100)
segments = []

# Functions

def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"



def go_fast():
    global delay
    delay=delay/2


def go_slow():
    global delay
    delay=delay*2


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


def foodp():
    q=True
    while q==True:
        x = 20*random.randint(-15, 14)
        y = 20*random.randint(-9, 10)
        a=0
        for m in segments:
            
            if [x,y]!=[m.xcor(),m.ycor()]:
                a+=1
        if a==len(segments):
            q=False
    food.goto(x,y)                


# Keyboard bindings
win.listen()


#user playing controls
if c=='u':
    win.onkeypress(go_up, "Up")
    win.onkeypress(go_down, "Down")
    win.onkeypress(go_left, "Left")
    win.onkeypress(go_right, "Right")


# Main game loop
while True:

    win.update()

    
    if c=='a' or c=='u':
    # Check for a collision with the border
        if head.xcor()>280 or head.xcor()<-300 or head.ycor()>200 or head.ycor()<-180:
            time.sleep(2)
            if c=='a':
                    time.sleep(20)
            head.goto(-300,-10)
            head.direction = "stop"
           # Hide the segments
            for segment in segments:
                segment.goto(15000, 15000)
            # Clear the segments list
            segments.clear()
            # Reset the delay
            delay = 0.1
        # Check for a collision with the food
        if head.distance(food) < 20:
            foodp()
            # Move the food to a random spot
            # Add a segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("sq")
            new_segment.color("green")
            new_segment.penup()
            segments.append(new_segment)
            # Shorten the delay
            if c=='u':
                delay -= 0.001
        # Move the end segments first in reverse order
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)
        # Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x,y)
        move()    
        # Check for head collision with the body segments
        for segment in segments:
            if segment.distance(head) < 0:
                time.sleep(2)
                if c=='a':
                    time.sleep(20)
                head.goto(-300,-180)
                head.direction = "stop"     
                # Hide the segments
                for segment in segments:
                    segment.goto(1000, 1000)
                # Clear the segments list
                segments.clear()
                # Reset the delay
                delay = 0.1
    if c=='a':
        win.onkeypress(go_fast, "a")
        win.onkeypress(go_slow, "s")
        if head.ycor()>200:
            go_right()
            move()
            go_down()
            move()
        if head.xcor()<-280:
            go_up()
        elif head.ycor()==-180 and head.xcor()!=280 and head.direction!='left':
            go_right()
            move()
            go_up()
            move()
        elif head.ycor()==-180:
            go_left()


    time.sleep(delay)        


win.mainloop()