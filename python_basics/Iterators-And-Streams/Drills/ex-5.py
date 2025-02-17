def multiply_by_two(iterator):
    for item in iterator:
        yield item * 2


numbers = range(1, 6)  
processed_numbers = multiply_by_two(numbers)
for num in processed_numbers:
    print(num)