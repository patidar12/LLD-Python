from shape import Shape
from circle import Circle
from ractangle import Ractangle
from Exception.curstom_exception import InvalidShape

class ShapeFactory:
    staticmethod
    def get_shape(shape) -> Shape:
        if shape.lower() == "circle":
            return Circle()
        if shape.lower() == "ractangle":
            return Ractangle()
        raise InvalidShape()
