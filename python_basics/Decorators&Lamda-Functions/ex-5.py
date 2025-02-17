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