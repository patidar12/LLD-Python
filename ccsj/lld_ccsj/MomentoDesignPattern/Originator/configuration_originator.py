from Momento.configuration_momento import ConfigurationMomento

class ConfigurationOriginator:
    def __init__(self, height: int, width: int):
        self.height: int = height
        self.width: int = width

    def set_height(self, height: int):
        self.height = height

    def set_width(self, width: int):
        self.width = width
    
    def create_momento(self):
        return ConfigurationMomento(self.height, self.width)

    def restore_momento(self, momento: ConfigurationMomento):
        self.height = momento.height
        self.width = momento.width
