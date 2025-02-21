import json

class Game:
    def __init__(self, level, score):
        self.level = level
        self.score = score

    def to_json(self):
        return json.dumps(self.__dict__, indent=4)

    @classmethod
    def from_json(cls, json_string):
        return cls(**json.loads(json_string))
