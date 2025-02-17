import time
def simple_logger(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function ended")
        return result
    return wrapper

@simple_logger
def greet(name):
    print(f"Hello, {name}!")


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Function executed!")

slow_function()


def debug_info(func):
    def wrapper(*args, **kwargs):
        print(f"Function: {func.__name__}, Args: {args}, Kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Returned: {result}")
        return result
    return wrapper

@debug_info
def add(a, b):
    return a + b

print(add(5, 10))


@simple_logger
@timer
@debug_info
def test_function():
    time.sleep(1)
    print("Test function executed")

test_function()