class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius  

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if not (-273.15 <= value <= 5000):
            raise ValueError("Temperature out of range")
        self._celsius = value

# Create an instance
temp = Temperature(25)
print(f"Temperature: {temp.celsius}°C")

# Attempt to set an invalid temperature
try:
    temp.celsius = -300
except ValueError as e:
    print(e)