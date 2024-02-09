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
    col1 = column % 2
    col2 = int(column / 2)
    col = col1 + col2
    print(col * first)
    if col1 == 0:
        for i in range(1, row + 1):
           print((col) * second, end="")
           print(slash)
           print((col) * third, end="")
           print(backslash)
    else: 
        for i in range(1, row + 1):
           print((col-1) * second, end="")
           print(slash + 3 * space + backslash)
           print(col * third)

hexagon()