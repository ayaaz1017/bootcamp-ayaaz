import json

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password  # Sensitive information

    def to_json(self):
        """Exclude sensitive attributes."""
        return json.dumps({k: v for k, v in self.__dict__.items() if k != "password"}, indent=4)
