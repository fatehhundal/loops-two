n = int(input("Enter the amount of numbers you want listed: "))

print("The numbers from {0} to {1}:".format(n, 1))

for i in range(n, 0, -1):
    print(i)