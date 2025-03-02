from circle import Circle
from ractangle import Ractangle
from Exceptions.custom_exceptions import InvalidShape


class ShapeFactory:

    def getShape(self, shape_type):
        if shape_type.lower() == 'circle':
            return Circle()
        elif shape_type.lower() == 'ractangle':
            return Ractangle()
        else:
            raise InvalidShape()


#ShapeFactory().createShape("ractangle")

