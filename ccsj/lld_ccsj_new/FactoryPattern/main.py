from shape_factory import ShapeFactory
class ShapeManager:
    def create_shape(self, shape):
        shape_obj = ShapeFactory.get_shape(shape)
        shape_obj.draw()

shape = input("Provide shape that needs to create: ")
ShapeManager().create_shape(shape)