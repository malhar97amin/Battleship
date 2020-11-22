from random import randint
import sys
print("""Hello! Welcome to the Battleship game by Malhar.
The rules are simple. Select a field size for enemy's battle field which shouldn't be less than 6x6.
You get unlimited chances to hit the ship.
Remember. Real heroes don't give up but if you wish to give up, enter 'x' in row and column.
Ahoy! You are all set to play.""")

#User gets to choose the field size
size=int(input("Enter the size of the field(just one integer):"))

if size < 6:
    print("The size of the field should atleast be 6x6, Try again!")
    sys.exit(1)
field=[]

#Creating the field as per users request
for i in range(size):
    field.append(["0"] * size)
def show_field(field):
    for row in field:
        print(" ".join(row))

#randomly creating coordinates for the ship
def create_row(field):
    return randint(0,len(field)-1)

def create_col(field):
    return randint(0,len(field)-1)

#Functions to increase the length of the ship vertically or horizontally and checking the alignment of the ship,
# If the ship does'nt fit in the matrix, the random position is generated again.
def vertical():
    if len(field) - int(row) >= 5:
        for n in range(5):
            field[row + n][col] = '0'
        test = 'true'
        return test
    else:
        test = 'false'
        return test

def horizontal():
    if len(field) - int(col) >= 5:
        for n in range(5):
            field[row][col + n] = '0'
        test1 = 'true'
        return test1
    else:
        test1 = 'false'
        return test1

def printmsg():
    if ((user_row < 0) or (user_row >= size)) or ((user_col < 0) or (user_col >= size)):
        print("Out of bounds, Mate!")

    elif field[user_row][user_col] == "X":
        print("You've already tried here!")

    else:
        print("oops! It was a miss, Try again.")
        field[user_row][user_col] = "X"

    show_field(field)
    #Printing the battle field
#creating the field
row=create_row(field)
col=create_col(field)

#Alignment of the ship
alignment=randint(0,1)

if alignment==0:
    # print('Vertical')
    # the ship is in vertical position, which is of length 5
    ver = vertical()
    while vertical() == 'false':
            row = create_row(field)
            col = create_col(field)
else:
    # print('Horizontal')
    #the ship is in horizontal position with the same size
    hor = horizontal()
    while horizontal()=='false':
            row=create_row(field)
            col=create_col(field)

show_field(field)
print("Enter the coordinates to hit the ship, The first row and column starts from zero.")

for count in range(5000):

    ##User enters coordinates to play the game
    user_row = input("Enter Row:")
    user_col = input("Enter Column:")

    # if user enters 'x' both times, the game quits
    if user_row == 'x' and user_col == 'x':
        print("Game over! You gave up too soon!")
        sys.exit(1)
    else:
        user_row=int(user_row)
        user_col=int(user_col)

    # keeping a track of how many times the user played
    print("Try " + str(count + 1) + ".")
    if alignment==0:
        if ((user_row >= row) and (user_row <= row+4)) and (user_col == col):
            print("Congratulations! It was a HIT!")
            break
        else:
            printmsg()

    else:
        if ((user_col >= col) and (user_col <= col + 4)) and (user_row == row):
            print("Congratulations! It was a HIT!")
            break
        else:
            printmsg()

#limitation of the code: The user must enter some value in the coordinates.
# there is only one ship no matter how big the field is.

