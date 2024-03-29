# Sophia Avielle D. Gregoro
# 223019
# October 10, 2022
# I have not discussed the Python language code in my program 
# with anyone other than my instructor or the teaching assistants 
# assigned to this course.
# I have not used Python language code obtained from another student, 
# or any other unauthorized source, either modified or unmodified.
# If any Python language code or documentation used in my program 
# was obtained from another source, such as a textbook or website, 
# that has been clearly noted with a proper citation in the comments 
# of my program.

#citations:
#Waleed Lugod - helped in logic by telling me to look at the maze as an empty maze instead of stressing about the walls
#Vaughn Alvarez - Moral support and made me ask the question, "how do I represent the maze?"
#https://www.delftstack.com/howto/python/python-not-in-list/#:~:text=list%20in%20Python.-,
#Use%20not%20in%20to%20Check%20if%20an%20Element,in%20a%20List%20in%20Python&text=If%20we%20need%20to%20check,
#list%2C%20it%20will%20return%20True%20. - for helping in the implementation of Add On 2

print("Welcome to the maze!")
level = int(input("select a level: 1, 2, or 3: "))
start = int(input("Starting location: "))
end = int(input("Ending location: "))

loc = start
exitspace = end

if level == 1:
    n = 0-3
    s = 0+3
    print("*************")
    print("* 0 * 1   2 *")
    print("*   *    ****")
    print("* 3   4   5 *")
    print("*        ****")
    print("* 6 * 7   8 *")
    print("*   *       *")
    print("*************")
elif level == 2:
    n = 0-4
    s = 0+4
    print("******************")
    print("* O   1   2   3  *")
    print("*   **********   *")
    print("* 4   5   6  *7  *")
    print("*   *****    *****")
    print("* 8 * 9 * 10  11 *")
    print("*   *   *        *")
    print("* 12  13* 14 *15 *")
    print("*       *    *   *")
    print("******************")
    
elif level == 3:
    n = 0-5
    s = 0+5
    print("***********************")
    print("* O   1    2   3  * 4 *")
    print("*   *****         *   *")
    print("* 5   6 *  7 * 8    9 *")
    print("*****   *    *    *****")
    print("* 10  11  12 * 13  14 *")
    print("*        *********    *")
    print("*    *      *    *    *")
    print("* 15 *16  17* 18 * 19 *")
    print("*    ****   *         *")
    print("* 20  21* 22* 23   24 *")
    print("*       *   *         *")
    print("***********************")
e = 0+1
w = 0-1

easymaze = [
    0, 1, 2,
    3, 4, 5,
    6, 7, 8,
]

directionmoveseasy = [
    ['south', 'quit'], ['south', 'east', 'quit'], ['west', 'quit'],
    ['north', 'south', 'east', 'quit'], ['north', 'south', 'east', 'west', 'quit'], ['west', 'quit'],
    ['north', 'quit'], ['north', 'east', 'quit'], ['west', 'quit']
]

normalmaze = [
    0, 1, 2, 3,
    4, 5, 6, 7,
    8, 9, 10, 11,
    12, 13, 14, 15
]

directionmovesnormal = [
    ['south', 'east', 'quit'], ['west', 'east', 'quit'], ['west', 'east', 'quit'], ['west', 'south', 'quit'],
    ['north', 'south', 'east', 'quit'], ['west', 'east', 'quit'], ['south', 'west', 'east', 'quit'], ['north', 'quit'],
    ['north', 'south', 'quit'], ['south', 'quit'], ['north', 'south', 'east', 'quit'], ['west', 'south', 'quit'],
    ['north', 'east', 'quit'], ['north', 'west', 'quit'], ['north', 'quit'], ['north', 'quit']
]

hardmaze = [
    0, 1, 2, 3, 4,
    5, 6, 7, 8, 9,
    10, 11, 12, 13,
    14, 15, 16, 17,
]

directionmoveshard = [
    ['south', 'east', 'quit'], ['west', 'east', 'quit'], ['south', 'west', 'east', 'quit'], ['west', 'south', 'quit'], ['south', 'quit'],
    ['north', 'east', 'quit'], ['west', 'south', 'quit'], ['north', 'south', 'quit'], ['north', 'south', 'east', 'quit'], ['west', 'south', 'quit'],
    ['south', 'east', 'quit'], ['north', 'south', 'east', 'west', 'quit'], ['north', 'west', 'quit'], ['north', 'east', 'quit'], ['west', 'south', 'quit'],
    ['north', 'south', 'quit'], ['north', 'east', 'quit'], ['west', 'south', 'quit'], ['south', 'quit'], ['north', 'south', 'quit'],
    ['south', 'east', 'quit'], ['west', 'quit'], ['north', 'quit'], ['north', 'east', 'quit'], ['north', 'south', 'west', 'quit'],
]

while loc != end:
    print("Available directions: ", end='')
    if level == 1:
        print(*directionmoveseasy[loc])
        direction = input("Which direction will you take?: ")
        x = direction.lower() in directionmoveseasy[loc]
    elif level == 2:
        easymaze = normalmaze
        print(*directionmovesnormal[loc])
        direction = input("Which direction will you take?: ")
        x = direction.lower() in directionmovesnormal[loc]
    elif level == 3:
        easymaze = hardmaze
        print(*directionmoveshard[loc])
        direction = input("Which direction will you take?: ")
        x = direction.lower() in directionmoveshard[loc]
    
    if x == False:
        print("Please choose an available direction")
        continue
    
    if direction.lower() == "north":
        loc = easymaze[n+loc]
    elif direction.lower() == "south":
        loc = easymaze[s+loc]
    elif direction.lower() == "east":
        loc = easymaze[e+loc]
    elif direction.lower() == "west":
        loc = easymaze[w+loc]
    elif direction.lower() == "quit":
        print("Try again next time")
        print("Goodbye!")
        exit()
    else:
        print("please choose an available direction")
    
print("found the exit!")
print("Goodbye!")
