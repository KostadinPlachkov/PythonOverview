from turtle import Turtle, done as turtle_done


def main():
    t = Turtle()
    t.speed("fastest")
    figures = create_figures(FIGURES_INPUT_DATA)

    for figure in figures:
        figure.draw(t)

    turtle_done()

# ========================================================

FIGURES_INPUT_DATA = [
    {"type": "square", "center_x": 0, "center_y": 0, "side": 2, "color": "black"},
    {"type": "square", "center_x": 0, "center_y": 0, "side": 100, "color": "red"},
    {"type": "square", "center_x": 0, "center_y": 0, "side": 200, "color": "blue"},
    {"type": "circle", "center_x": 0, "center_y": 0, "radius": 50, "color": "blue"},
    {"type": "rectangle", "center_x": 0, "center_y": 0, "width": 200, "height": 75, "color": "purple"},
    {"type": "pie", "center_x": 0, "center_y": 0, "radius": 100, "arg_degree": 180, "color": "green"},
    {"type": "n-sided", "center_x": 0, "center_y": 0, "radius": 60, "numb_sides": 5, "color": "red"}

]


class Figure:

    def __init__(self, center_x: int, center_y: int, color: str):
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y
        self.color = color

    def __str__(self):
        return "Figure : ({}, {})".format(self.center_x, self.center_y)

    def draw(self, turtle):
        turtle.color(self.color)

    def jump_to(self, turtle, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()


class Circle(Figure):
    steps = None

    def __init__(self, center_x: int=0, center_y: int=0, radius: int=0, color: str='black'):
        super().__init__(center_x, center_y, color)
        self.radius = radius

    def draw(self, turtle: Turtle):
        super().draw(turtle)
        self.jump_to(turtle, self.center_x, self.center_y - self.radius)
        turtle.circle(self.radius, steps=self.steps)
        self.jump_to(turtle, 0, 0)


class SquareEasy(Circle):
    def __init__(self, center_x: int=0, center_y: int=0, radius: int=0, color: str='black'):
        super().__init__(center_x, center_y, radius, color)
        self.steps = 4


class SquareEasiest(Circle):
    steps = 4


class Square(Figure):

    def __init__(self, center_x: int=0, center_y: int=0, side: int=0, color: str='black'):
        super().__init__(center_x, center_y, color)
        self.side = side

    def draw(self, turtle: Turtle):
        super().draw(turtle)
        self.jump_to(turtle,
                     self.center_x - self.side/2,
                     self.center_y - self.side/2)

        for _ in range(4):
            turtle.forward(self.side)
            turtle.left(90)

        self.jump_to(turtle, 0, 0)

class Rectangle(Figure):
    def __init__(self, center_x: int=0, center_y: int=0, width: int = 60, height: int = 20, color: str='purple'):
        super().__init__(center_x, center_y, color)
        self.width = width
        self.height = height

    def draw(self, turtle: Turtle):
        super().draw(turtle)
        self.jump_to(turtle,
                     self.center_x - self.width/2,
                     self.center_y - self.height/2)

        for _ in range(2):
            turtle.forward(self.width)
            turtle.left(90)
            turtle.forward(self.height)
            turtle.left(90)

        self.jump_to(turtle, 0, 0)

class Pie(Figure):
    def __init__(self, center_x: int=0, center_y: int=0, radius: int=30, arg_degree: int = 30, color: str='green'):
        super(Pie, self).__init__(center_x, center_y, color)
        self.radius = radius
        self.arg_degree = arg_degree

    def draw(self, turtle):
        super(Pie, self).draw(turtle)
        self.jump_to(turtle, self.center_x, self.center_y - self.radius)
        turtle.circle(self.radius, self.arg_degree)
        self.jump_to(turtle, 0, 0)

class Nsided(Figure):
    def __init__(self, center_x: int=0, center_y: int=0, radius: int=30, numb_sides: int = 30, color: str='red'):
        super().__init__(center_x, center_y, color)
        self.radius = radius
        self.num_sides = numb_sides

    def draw(self, turtle):
        super().draw(turtle)
        self.jump_to(turtle, self.center_x, self.center_y + self.radius)
        turtle.circle(self.radius, steps = self.num_sides)
        self.jump_to(turtle, 0, 0)


def create_figures(figures_input_data: list) -> list:
    """
    Return a list of Figure instances
    :param figures_list:
    :return:
    """
    result = []
    for fdata in figures_input_data:
        type = fdata['type']
        if type == 'square':
            figure = Square(
                center_x=fdata['center_x'],
                center_y=fdata['center_y'],
                side=fdata['side'],
                color=fdata['color']
            )
        elif type == 'circle':
            figure = Circle(
                center_x=fdata['center_x'],
                center_y=fdata['center_y'],
                radius=fdata['radius'],
                color=fdata['color']
            )
        elif type == "rectangle":
            figure = Rectangle(
                center_x = fdata['center_x'],
                center_y = fdata['center_y'],
                width = fdata['width'],
                height = fdata['height'],
                color = fdata['color']
            )
        elif type == "pie":
            figure = Pie(
                center_x = fdata['center_x'],
                center_y = fdata['center_y'],
                radius = fdata['radius'],
                arg_degree = fdata["arg_degree"],
                color = fdata['color']
            )
        elif type == "n-sided":
            figure = Nsided(
                center_x = fdata['center_x'],
                center_y = fdata['center_y'],
                radius = fdata['radius'],
                numb_sides = fdata["numb_sides"],
                color = fdata['color']
            )
        else:
            raise Exception("Unsupported figure type: " + type)
        result.append(figure)

    return result



if __name__ == '__main__':
    main()
