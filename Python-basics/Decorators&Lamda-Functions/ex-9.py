def validate_args(func):
    def wrapper(self, *args, **kwargs):
        if any(arg is None for arg in args):
            raise ValueError("Arguments cannot be None")
        return func(self, *args, **kwargs)
    return wrapper

class Calculator:
    @validate_args
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(10, 20))