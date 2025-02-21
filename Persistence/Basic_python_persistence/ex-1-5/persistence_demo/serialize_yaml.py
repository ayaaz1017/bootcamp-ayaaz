from persistence_demo.car import Car

def save_car():
    car = Car("Toyota", "Corolla", 2022)
    yaml_string = car.to_yaml()
    print("Serialized YAML:\n", yaml_string)

if __name__ == "__main__":
    save_car()
