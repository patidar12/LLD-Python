from shap_factory import ShapeFactory

shap_factory = ShapeFactory()
shape = shap_factory.getShape('circle')
shape.draw()


'''
FactoryPattern: Factory pattern is used when there is multiple subclasses and we wan't ot create objects of classes based on some conditions.
So insted of creating object in drive class, we can use factory class that return object of particular class based on type and then we can create the object and call the method.
So it can avoid code duplicacy, As may required to create this objects from multiple places. and if on all the places we are writing this
If conditions than it create duplicate codes. So we are providing a central place called Factory where we just provide the type and it returnes
the object, so from all the places we just need to use the ShapFactory. Here ShapeFactory is the only source of truth here.
'''