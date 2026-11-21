string1 = input("Please enter a string: ")

string2 = ('')

for i in string1:
    string2 = i + string2

print("\nThe original string:", string1)
print("The reversed string:", string2)