row = int(input("enter number of row : "))
column = int(input("enter number of column : "))
def hexagon():
    space = " "
    slash = "/"
    underscore = '___'
    backslash = "\\"
    print(space, end="")
    first = underscore + 5 * space
    second = slash + 3 * space + backslash + underscore
    third = backslash + underscore + slash + 3 * space

    print(row * first)

    for i in range(1, row + 1):
        print((row-1) * second, end="")
        print(slash + 3 * space + backslash)
        print(row * third)


hexagon()