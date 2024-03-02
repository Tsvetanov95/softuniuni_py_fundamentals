def my_generator():
    yield 1
    yield 2
    return 3


generator = my_generator()

print(next(generator))
print(next(generator))
try:
    print(next(generator))
except StopIteration as e:
    print("Generator :", e.value)
