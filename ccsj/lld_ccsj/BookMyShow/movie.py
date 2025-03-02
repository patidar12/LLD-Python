class Movie:
    def __init__(self, mid: int, name: str, duration_in_minutes: int ):
        self.id: int = mid
        self.name: str = name
        self.duration_in_minutes: int = duration_in_minutes
