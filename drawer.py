import turtle

def push_state(stack):
    def command():
        pos = turtle.position()
        heading = turtle.heading()
        stack.append((pos, heading))
    return command

def pop_state(stack):
    def command():
        pos, heading = stack.pop()
        turtle.penup()
        turtle.goto(pos)
        turtle.setheading(heading)
        turtle.pendown()
    return command

class Drawer:

    def __init__(self, draw_speed, init_angle, fwd_amt, turn_amt):
        turtle.speed(draw_speed)
        turtle.setheading(init_angle)
        self.stack = []
        self.commands = {
            'F': lambda: turtle.forward(fwd_amt),
            '+': lambda: turtle.right(turn_amt),
            '-': lambda: turtle.left(turn_amt),
            '[': push_state(self.stack),
            ']': pop_state(self.stack)
        }

    def draw(self, draw_str):
        for char in draw_str:
            if char in self.commands:
                self.commands[char]()

