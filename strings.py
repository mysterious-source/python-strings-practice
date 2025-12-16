#First version of strings practice
first_name = input("Enter your first name:")
second_name = input("Enter your middle name and nickname:")
a = second_name.strip()
b = second_name.capitalize()
c = int(len(a))
d = int(len(first_name))
g = c+d
print(c+d)
print(first_name[0])
print(second_name[0])
e = first_name[0].upper()
f = second_name[-1].lower()
print("The student ID is",e+f+str(g))

