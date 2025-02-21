def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error: {e}, Retrying...")
            print("Max retries reached")
        return wrapper
    return decorator

@retry(3)
def error_prone():
    raise ValueError("Oops!")

error_prone()