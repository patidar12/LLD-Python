from abc import ABC, abstractmethod

class BreatheImplementer(ABC):
    @abstractmethod
    def breathe(self):
        pass


class LandBreatheImplementer(BreatheImplementer):
    def breathe(self):
        print(
            "Breathe form nose \
            Inhale Oxygone form Air \
            Exahale Carbon dioxide..."
        )

class WaterBreatheImplementer(BreatheImplementer):
    def breathe(self):
        print(
            "Breathe form GILLS \
            Inhale Oxygone form Water \
            Exahale Carbon dioxide..."
        )

class TreeBreatheImplementer(BreatheImplementer):
    def breathe(self):
        print(
            "Breathe form LEAVES \
            Inhale Carbon dioxide \
            Exahale Oxygone through Photosynthesis..."
        )
