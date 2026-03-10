n = int(input("Please, enter the number to calculate the factorial : "))

result = 1

for i in range(n, 0, -1):
    print(f"{i}*", end="")
    result = result * (i)

print()
print(result)
