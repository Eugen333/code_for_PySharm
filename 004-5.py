print("Завданя 5")
print()
storona1=int(input("введіть ширину прямокутника: "))
storona2=int(input("введіть висоту прямокутника: "))
print("* " * storona1)
for i in range(1, storona2 - 1):
    print("* " + "  " * (storona1 - 2) + "*")
print("* " * storona1)
print()
