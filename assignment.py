number = int(input("What number do you want powered? "))
index = int(input("How many times should it be powered? "))

fin_num = number
print(f"{number} to the power of {index} is", end=" ")

for i in range(index-1):
    fin_num = fin_num * number

print(fin_num)