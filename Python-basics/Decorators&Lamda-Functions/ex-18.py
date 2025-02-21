data = ["hello", "world", 1, 2, 3]
transformed = [x.upper() if isinstance(x, str) else x**2 for x in data]
print(transformed)
