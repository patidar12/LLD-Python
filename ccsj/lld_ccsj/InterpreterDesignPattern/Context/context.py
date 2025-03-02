from typing import Dict

class Context:
    def __init__(self):
        self.context_map: Dict[str, int] = {}
    
    def put(self, string_value: str, number: int):
        self.context_map[string_value] = number
    

    def get(self, string_value: str) -> int:
        return self.context_map.get(string_value)
