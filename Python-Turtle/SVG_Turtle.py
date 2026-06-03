"""
Eine Klasse, die sowohl die Turtle als auch die SVG Ausgabe macht.
"""

from turtle import Screen, Turtle
import math

from svg_turtle import SvgTurtle


class SVG_Turtle(Turtle):
    svg: SvgTurtle

    def __init__(self, params, *args, **kwargs):
        super().__init__(*args, **kwargs)

        title = params.get("title", "Python Turtle")
        self.filename = params.get("filename", "output.svg")
        self.size = params.get("size", (500, 500))
        width, height = self.size

        self.screen = Screen()
        self.screen.title(title)
        self.svg = SvgTurtle(width, height)

    def __del__(self) -> None:
        print("Writing SVG File ....")
        self.svg.save_as(self.filename)

    def wait(self):
        """keep the screen open"""
        self.screen.mainloop()

    def speed(self, speed=None):
        if speed is not None:
            super().speed(speed)

    def penup(self):
        super().penup()
        self.svg.penup()

    def pendown(self):
        super().pendown()
        self.svg.pendown()

    def forward(self, distance):
        super().forward(distance)
        self.svg.forward(distance)

    def backward(self, distance):
        super().backward(distance)
        self.svg.backward(distance)

    def right(self, angle):
        super().right(angle)
        self.svg.right(angle)

    def left(self, angle):
        super().left(angle)
        self.svg.left(angle)

    def goto(self, x, y=None):
        super().goto(x, y)
        self.svg.goto(x, y)

    def setheading(self, to_angle):
        super().setheading(to_angle)
        self.svg.setheading(to_angle)

    def home(self):
        super().home()
        self.svg.home()

    def circle(self, radius, angle=None, steps=None):
        super().circle(radius, angle, steps)
        self.svg.circle(radius, angle, steps)

    def dot(self, size=None, *color):
        super().dot(size, *color)
        self.svg.dot(size, *color)

    def stamp(self):
        super().stamp()
        self.svg.stamp()

    def clear(self):
        super().clear()

    def reset(self):
        super().reset()

    def undo(self):
        super().undo()

    def fillcolor(self, *args):
        super().fillcolor(*args)
        self.svg.fillcolor(*args)

    def pencolor(self, *args):
        super().pencolor(*args)
        self.svg.pencolor(*args)

    def begin_fill(self):
        super().begin_fill()
        self.svg.begin_fill()

    def end_fill(self):
        super().end_fill()
        self.svg.end_fill()

    def hideturtle(self):
        super().hideturtle()

    def showturtle(self):
        super().showturtle()

    def isvisible(self):
        return super().isvisible()

    def write(self, arg, move=False, align="left", font=("Arial", 8, "normal")):
        super().write(arg, move, align, font)
        self.svg.write(arg, move, align, font)

    # Extended Stuff ---------------------------------------

    def toRad(self, w):
        return w * math.pi / 180

    def toGrad(self, w):
        return w * 180 / math.pi

    def createFilledCircle(self, x, y, color, radius, winkel=360, steps=50):
        """M = Centered"""
        self.penup()
        self.goto(x, y - radius)
        self.pendown()

        self.fillcolor(color)
        self.begin_fill()
        self.circle(radius, winkel, steps)
        self.end_fill()

    def getPosviaAngle(self, radius, angle):
        x = radius * math.cos(self.toRad(angle))
        y = radius * math.sin(self.toRad(angle))
        return x, y

    def outsideHeading(self, x, y):
        """
        Calculate the angle from the origin to point (x, y)
        Returns angle in degrees, measured counterclockwise from positive x-axis
        """
        return self.toGrad(math.atan2(y, x))

    import math

    def drawArc(self, mx, my, radius, startangle, angle, steps=None):
        """
        Draw an arc centered at (mx, my)

        Args:
            mx, my: Center coordinates of the arc
            radius: Radius of the arc
            startangle: Starting angle in degrees (0° = positive x-axis)
            angle: Arc angle in degrees (positive = counterclockwise, negative = clockwise)
            steps: Number of line segments (if None, auto-calculate based on angle)
        """
        if steps is None:
            # Auto-calculate steps based on angle size (more steps for larger angles)
            steps = max(5, int(abs(angle) / 5))

        # Ensure we have at least 2 points for an arc
        steps = max(2, steps)

        # Calculate step size
        step_angle = angle / (steps - 1)

        # Move to starting position
        start_x = mx + radius * math.cos(math.radians(startangle))
        start_y = my + radius * math.sin(math.radians(startangle))

        self.penup()
        self.goto(start_x, start_y)
        self.pendown()

        # Draw the arc
        for i in range(steps):
            current_angle = startangle + (step_angle * i)
            x = mx + radius * math.cos(math.radians(current_angle))
            y = my + radius * math.sin(math.radians(current_angle))
            self.goto(x, y)

        # Set turtle heading to be tangent to the arc at the end point
        end_angle = startangle + angle
        # Tangent is perpendicular to radius, so add 90 degrees
        tangent_angle = end_angle + 90
        self.setheading(tangent_angle)
