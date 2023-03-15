from PythonCharm.Python.oop_shapes.ShapeParent import ShapeParent
from PythonCharm.Python.oop_shapes.squareChild import squareChild


class MainShape () :

    shape1 = ShapeParent("Shape White")
    shape2 = ShapeParent("Shape Blue")

    square = squareChild()
    shape1.perimeter(2,3)
    shape2.perimeter(4,5)
    square.area(3,4)



