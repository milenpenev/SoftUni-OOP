class Hero:
    def __init__(self, username: str, level: int):
        self.level = level
        self.username = username

    def __str__(self):
        return f"{self.username} of type Hero has level {self.level}"