num = int(input("Enter the number: "))

space = (num * 2) - 2
star = 1

# Upper Half
for row in range(1, num + 1):

    # Left Stars
    for col2 in range(1, star + 1):
        print("*", end=" ")

    # Space
    for col1 in range(1, space + 1):
        print(" ", end=" ")

    # Right Stars
    for col3 in range(1, star + 1):
        print("*", end=" ")

    print()
    if row< (num*2)//2 +2:

        star = star + 1
        space = space - 2
    else:
        star = star - 1
        space = space + 2

# Lower Half
'''space = 2
star = num - 1

for row in range(1, num):

    # Left Stars
    for col2 in range(1, star + 1):
        print("*", end=" ")

    # Space
    for col1 in range(1, space + 1):
        print(" ", end=" ")

    # Right Stars
    for col3 in range(1, star + 1):
        print("*", end=" ")

    print()

    star = star - 1
    space = space + 2'''
