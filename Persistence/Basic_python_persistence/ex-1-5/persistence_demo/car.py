import yaml

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def to_yaml(self):
        """Convert Car object to YAML string."""
        return yaml.dump(self.__dict__, default_flow_style=False)
