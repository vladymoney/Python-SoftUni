def squares(n):
    for i in range(1, n + 1):
        yield i * i

#test code
print(list(squares(5)))