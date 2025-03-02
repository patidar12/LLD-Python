

from breathe_implementer import TreeBreatheImplementer, WaterBreatheImplementer, LandBreatheImplementer
from living_things import Dog, Fish, Tree

Dog(LandBreatheImplementer()).breathe_process()
Fish(WaterBreatheImplementer()).breathe_process()
Fish(TreeBreatheImplementer()).breathe_process()


'''

Defination:  Bridge pattern decouples an abstration form its implementation
so that the two can vary independently.

-----------------------------------------------------------------------------

Here we solved the issue of tightly coupled abstration and implementation.
So both can grow indipandantly. and can change the behaviour on run time.
As we did on above example for Fish.

Also both LivingThings and BreatheImplementer can grow indipendently.

'''