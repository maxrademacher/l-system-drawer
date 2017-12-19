import turtle

def push_state(stack):
    def command():
        pos = turtle.position()
        heading = turtle.heading()
        pensize = turtle.pensize()
        stack.append((pos, heading, pensize))
    return command

def pop_state(stack):
    def command():
        pos, heading, pensize = stack.pop()
        turtle.penup()
        turtle.goto(pos)
        turtle.setheading(heading)
        turtle.pensize(pensize)
        turtle.pendown()
    return command

class Drawer:

    def __init__(self, draw_speed, init_angle, init_size, fwd_amt, turn_amt, inc_amt):
        turtle.speed(draw_speed)
        turtle.setheading(init_angle)
        turtle.pensize(init_size)
        self.stack = []
        self.commands = {
            'F': lambda: turtle.forward(fwd_amt),
            '+': lambda: turtle.right(turn_amt),
            '-': lambda: turtle.left(turn_amt),
            '[': push_state(self.stack),
            ']': pop_state(self.stack),
            'p': lambda: turtle.pensize(max(1, turtle.pensize() - inc_amt)),
            'P': lambda: turtle.pensize(min(100, turtle.pensize() + inc_amt))
        }

    def draw(self, draw_str):
        for char in draw_str:
            if char in self.commands:
                self.commands[char]()

