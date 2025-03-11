def func2(n):
    return len(list(filter(lambda x: int(x) < 3, str(n))))


print(func2(int(input("Enter a number: "))))
