def custom_logger(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{message} - {func.__name__} started")
            result = func(*args, **kwargs)
            print(f"{message} - {func.__name__} ended")
            return result
        return wrapper
    return decorator

@custom_logger("INFO")
def process_data():
    print("Processing data...")

process_data()

