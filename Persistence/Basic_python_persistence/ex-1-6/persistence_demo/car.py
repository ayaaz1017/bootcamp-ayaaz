import yaml

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @classmethod
    def from_yaml(cls, yaml_string):
        """Convert YAML string to Car object."""
        data = yaml.safe_load(yaml_string)
        return cls(**data)
