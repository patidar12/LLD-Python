from abc import ABC, abstractmethod

class LivingThings(ABC):
    @abstractmethod
    def breathe_process(self):
        pass




class Dog(LivingThings):
    def breathe_process(self):
        print(
            "Breathe form nose \
            Inhale Oxygone form Air \
            Exahale Carbon dioxide..."
        )


class Fish(LivingThings):
    def breathe_process(self):
        print(
            "Breathe form GILLS \
            Inhale Oxygone form Water \
            Exahale Carbon dioxide..."
        )

class Tree(LivingThings):
    def breathe_process(self):
        print(
            "Breathe form LEAVES \
            Inhale Carbon dioxide \
            Exahale Oxygone through Photosynthesis..."
        )


#Tree().breathe_process()
Fish().breathe_process()



'''

Defination:  Bridge pattern decouples an abstration form its implementation
so that the two can vary independently.

-----------------------------------------------------------------------------
Because of real classes or breathe process is tightly couples with
abstract class.
if i wan't to add new breathe process then i have to create new class of LivingThings.
Like if i wan't to add breathe process for Bird, then i have to class new Bird class.
Then that will implement the Livingthings class. And because of LivingThings can have other
things also, so for only BrithProcess implementing LivingClass is irivallent.
Also Because of breathe process is tightly coupled with LivingThings
We can not change or grow both classes sepratly.

To sole this bridge pattern comes into pitcure. Here we will sperate LivingThings
and BrithProcess so both can grow speratly.

'''