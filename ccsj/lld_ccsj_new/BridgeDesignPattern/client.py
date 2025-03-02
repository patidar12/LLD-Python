from living_thing_abstractor import (
    Dog,
    Fish,
    Tree
)

from breath_implementor import (
    LandBreathImplementor,
    WaterBreathImplementor,
    TreeBreathImplementor
)


dog = Dog(LandBreathImplementor())
dog.breath_process()

tree = Tree(TreeBreathImplementor())
tree.breath_process()