from typing import List
from Momento.configuration_momento import ConfigurationMomento

class ConfigurationCareTaker:
    def __init__(self):
        self.history: List[ConfigurationMomento] = []
    
    def add_momento(self, momento: ConfigurationMomento):
        self.history.append(momento)

    def undo(self) -> ConfigurationMomento:
        if self.history:
            return self.history.pop()
