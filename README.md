# PyTurtle

Some usefull stuff for Turtle Graphis

## Tigerjython

Is done here [https://www.tigerjython.ch](https://www.tigerjython.ch)  
Its an workaround for simplyfied working with smaller kids.

`SVG.py` is a self written library, that exports the turtle graphics to an SVG File. Still there are some missing parts. See the examples how to use it.

## Python-Turtle

Holds mainly a Class that is doing Turtle Commands, and also writes an SVG File.
Example Usage

```python
    params = {"title": "Pi Radial", "filename": "PiRadial.svg", "size": (500, 500)}
    t = SVG_Turtle(params)
    t.speed(8)

    t.forward(100)

    t.wait()
```

Beside all basic commands from python turtle module, there are these extensions:

- drawArc(t, x, y, radius, startangle, angle, steps)  
  t ... is the Turtle Object  
  startangle ... where to start at the circle. 90 = at the top  
  angle ... which angle to draw. negativ angles are drawing clockwise
