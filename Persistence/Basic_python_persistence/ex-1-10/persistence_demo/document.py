import json

class Document:
    def __init__(self, title, content, version="1.0"):
        self.title = title
        self.content = content
        self.version = version

    def to_json(self):
        return json.dumps(self.__dict__, indent=4)

    @classmethod
    def from_json(cls, json_string):
        data = json.loads(json_string)
        version = data.get("version", "1.0")

        if version == "1.0":
            return cls(data["title"], data["content"])
        elif version == "2.0":
            return cls(data["title"], data["content"], data["version"])
