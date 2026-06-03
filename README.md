# PyTurtle

Some usefull stuff for Turtle Graphis

## Python-Turtle



# classes

Holds some classes 

## svg_turtle_class.py

is doing Turtle Commands, and also writes an SVG File.
Example Usage

```python
t = SVGTurtle(width=400, height=400, filename="01_square.svg", bgcolor="lightblue")
t.shape("turtle")
t.color("green")
t.speed(3)

# Quadrat zeichnen
for i in range(4):
    t.forward(100)
    t.right(90)

t.save_svg()
```

Beside all basic commands from python turtle module, there are these extensions:

> drawArc(x, y, radius, startangle, angle, steps)  
>  _t_ ... is the Turtle Object  
>  _startangle_ ... where to start at the circle. 90 = at the top  
>  _angle_ ... which angle to draw. negativ angles are drawing clockwise
>
> ```python
> params = {"title": "Pi Radial", "filename": "PiRadial.svg", "size": (500, 500)}
> t = SVG_Turtle(params)
> #1
> t.drawArc(0, 0, 100, 90, -200)
> #2
> t.drawArc(100, 100, 100, 90, 90)
> #2
> t.drawArc(-150, 00, 100, 270, 90)
> ```
>
> ![Example](https://github.com/SManAT/PyTurtle/blob/main/Python-Turtle/arcs.svg)

> createFilledCircle(self, x, y, color, radius, winkel=360, steps=50)
>
> ```python
>   t.createFilledCircle(0, 0, "#aaaaaa", radius, 360)
> ```

## Tigerjython

Is done here [https://www.tigerjython.ch](https://www.tigerjython.ch)  
Its an workaround for simplyfied working with smaller kids.

`SVG.py` is a self written library, that exports the turtle graphics to an SVG File. Still there are some missing parts. See the examples how to use it.
