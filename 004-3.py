print("Завданя 3")
print()
razmer = 10  # int(input("Длина катета: "))
space = 0
print("*")
for i in range(1, razmer - 1):
    print("* ", end=)
    print("  " * space, end=)
    print("* ")
    space += 1
print("* " * (razmer))
print()
