class ConfigurationMomento:
    def __init__(self, height: int, width: int):
        self.height: int = height
        self.width: int = width
    
    def get_height(self) -> int:
        return self.height
    
    def get_width(self) -> int:
        return self.width
