from persistence_demo.car import Car

def load_car():
    yaml_string = "make: Tesla\nmodel: Model S\nyear: 2023"
    car = Car.from_yaml(yaml_string)
    print(f"Deserialized Car: {car.make} {car.model}, Year: {car.year}")

if __name__ == "__main__":
    load_car()
