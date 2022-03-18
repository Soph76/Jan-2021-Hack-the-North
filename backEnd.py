from random import randint
class Person:
    def __init__(self, username, password, name, school, faculty, program, year, canHelpCourses):
        self.username = username
        self.password = password
        self.name = name
        self.school = school
        self.faculty = faculty
        self.program = program
        self.year = year
        self.canHelpCourses = canHelpCourses
        self.credits=10

class Tile (Person):
    def __init__(self, person, needHelpCourse, helpDescription):
        self.person = person
        self.needHelpCourse = needHelpCourse
        self.helpDescription = helpDescription
        self.person.credits-=1
    # to print out a tile
    def printTile(self):
        print("----------------------------------")  
        print("Name: " + self.person.name)
        print("School: " + self.person.school) 
        print("Program: " + self.person.program + ", year " + str(self.person.year))
        print("Needs help with " + self.needHelpCourse)   
        print("Description: " + self.helpDescription) 
        print("Chat now")  
        print("----------------------------------")  
    
# making new person for a new profile
def signUp ():
    name = input("What is your name? ")
    school = input("What school do you go to? ")
    faculty = input("What faculty are you in? ")
    program = input("What program are you in? ")
    year = int(input("What year are you in? "))
    done = False  
    canHelpCourses = []
    while done == False:
        n = input("What is a course you can help with? ")
        canHelpCourses.append(n)
        answer = input("Anything else? (y/n): ")
        if answer == "n":
            done = True
        while answer!="y" and answer!="n":
            answer = input("Please use 'y' or 'n': ")
            if answer == "n":
                done = True
    done = False
    while done == False:
        unique = True
        username = input("Make a username: ")
        for person in listOfPeople:
            if username == person.username:
                print("I'm sorry, that username has already been taken.")
                unique = False
                break
        if unique == True:
            done = True
    password = input("Make a password: ")
    return Person(name, username, password, school, faculty, program, year, canHelpCourses)

# get help function
def getHelp(person):
    if person.credits <= 0:
        print("You have no credits left. Help others to earn credits!")
        return
    
    needHelpCourse = input("What course do you need help with? ")
    helpDescription = input("Please provide a brief description of what you need help with: ")
    answer = input("Would you like to post this to Tutor Tinder? (y/n): ")
    if answer == "n":
        return
    elif answer == "y":
        print("You now have " + str(person.credits-1) + " credits!")
        return Tile(person, needHelpCourse, helpDescription)
    while answer!="y" and answer!="n":
        answer = input("Please use 'y' or 'n': ")
        if answer == "n":
            return
        elif answer == "y":
            print("You now have " + str(person.credits-1) + " credits!")
            return Tile(person, needHelpCourse, helpDescription)

#Log in function
def logIn():
    checkU = False
    checkP = False
    check = False
    while check == False:
        checkUsername = input("Username: ")
        checkPassword = input("Password: ")
        for person in listOfPeople:
            if person.username == checkUsername:
                checkU = True
                pperson = person
        if checkU == True:
            if pperson.password == checkPassword:
                checkP = True
                check = True
        if checkU!=True or checkP != True:
            print("I'm sorry, that username or pasword is incorrect. Please try again\n")
    return pperson

# method that gets called when someone clicks on Chat Now to help someone
def helpSomeone(helper, tile):
    print("Thank you for choosing to help " + tile.person.name + ".\nThey will have the option of giving you one, two or three credits at the end! \n\nConnecting you to chat with this student ...")
    points = randint(1,3)
    print(tile.person.name + " has sent you " + str(points) + " credits!")
    helper.credits += points
    print("You now have " + str(helper.credits) + " credits!")
    return tile

#Fake person data base
hattie = Person("coburh1", "password", "Hattie", "McMaster", "Engineering", "Mechatronics", 2, ["MUSIC 1A04", "ECON 1B03"])
sophie = Person("bierers", "password", "Sophie", "McMaster", "Engineering", "Engineering Physics", 2, ["FRENCH 1A06"])
ashleigh = Person("warrea2", "password", "Ashleigh", "McMaster", "Engineering", "Chemical", 2, ["ECON 1B03"])
emily = Person("browe21","password","Emily", "McMaster", "Science", "Computer Science", 2, ["MUSIC 1A04", "ART 1D03"])
listOfPeople = [hattie, sophie, ashleigh, emily]

#fake Tile database
hattieTile = Tile(hattie, "ENGPHYS 2E04", "Using Maple")
sophieTile = Tile(sophie, "ENGPHYS 3D03", "What is a nuclear reaction")
ashleighTile = Tile(ashleigh, "MATH 2ZZ3", "Fourier series")
emilyTile = Tile(emily, "MATH 2R03", "Vector Spaces")
listOfTile = [hattieTile, sophieTile, ashleighTile,  emilyTile]

# "main" technically starts here

#Login and sign up pages
print("----------------------------------")  
answer = input("Welcome to Tutor Tinder! \n Login (l) \n Sign up (s)\n")
while answer !="l" and answer !="s":
    answer = input("Please use 'l' to login or 's' to sign up\n")
print("\n----------------------------------")  
if answer == "l":
    user = logIn()
elif answer == "s":
    user = signUp()
    listOfPeople.append(user)

cont = True
while (cont == True):
    #Get help or Give help pages
    print("----------------------------------")  
    answer = input("What would you like to do? \n Get help now (g) \n Help someone else, earn credits (h)\n")
    while answer !="g" and answer !="h":
        answer = input("Please use 'g' to get help or 'h' to help someone else")
    print("\n----------------------------------")  
    
    if answer == "g":
        userTile = getHelp(user)
        if userTile != None:
            listOfTile.append(userTile)
        response = input("Do you want to continue? (y/n): ")
        if (response == "n"):
            cont = False

    elif answer == "h":
        someoneElse = False
        for tile in listOfTile:
            if tile.person != user:
                someoneElse = True

        if someoneElse == False:
            print("There are no people to help right now, check back later!") 
        else:
            for tile in listOfTile:
                if(tile.person!=user):
                    tile.printTile()
            check = False
            while check == False:
                help = input("Who would you like to help?\n")
                for tile in listOfTile:
                    if tile.person.name == help:
                        tileToDelete = helpSomeone(user, tile)
                        listOfTile.remove(tileToDelete)
                        check = True
                if check == False:
                    print("Make sure to write their name correctly!")

        response = input("Do you want to continue? (y/n): ")
        if (response == "n"):
            cont = False