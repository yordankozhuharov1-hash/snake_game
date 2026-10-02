from turtle import Turtle


def create_snake():
    segments = [] 
    starting_position = [(0, 0), (-20, 0), (-40, 0)]
    for position in starting_position:
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        segments.append(new_segment)
    return segments


def move_snake(segments):
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

def turn_left(segments):
    if segments[0].heading() != 0:
        segments[0].setheading(180)

def turn_right(segments):
    if segments[0].heading() != 180:
        segments[0].setheading(0)

def turn_up(segments):
    if segments[0].heading() != 270:
        segments[0].setheading(90)

def turn_down(segments):
    if segments[0].heading() != 90:
        segments[0].setheading(270)

def grow_snake(segments):
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(segments[-1].position())
    segments.append(new_segment)