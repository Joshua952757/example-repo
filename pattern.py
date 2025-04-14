n = 5
for i in range(1, n + 1):
    if i <=n//2 + 1:
        print("* " *i)
    else:
        print("* " *(n - 1 + 1))
        
        print()
        
        n = 5

for i in range(n - 1, 0, -1):
        print("* " * i)