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

> drawArc(x, y, radius, startangle, angle, steps)  
>  _t_ ... is the Turtle Object  
>  _startangle_ ... where to start at the circle. 90 = at the top

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

> ![Example](https://github.com/SManAT/PyTurtle/blob/main/Python-Turtle/arcs.svg)

- createFilledCircle(self, x, y, color, radius, winkel=360, steps=50)

  ```python
  t.createFilledCircle(0, 0, "#aaaaaa", radius, 360)
  ```

```

```
