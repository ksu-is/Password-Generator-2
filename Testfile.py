from tkinter import *

from tkinter import messagebox
import random



root = Tk()
root.title('Password Generator')
root.geometry('300x300')

#This gets the password length
def start_gen():
    length = pw_length.get()
    messagebox.showinfo(title='message',message='Your password length is '+length)
    return length
    generator(length)

    
#Length of password label
pw_length = Label(root, text="Enter password length").pack()
pw_length = Entry(root)
pw_length.pack()
#length od password button
Button(root, text="Submit", command=start_gen).pack()
#blank space
blank = Label(root, text="                 ")
blank.pack()
#Final Password label
final_password = Label(root, text="Your Password")
final_password.pack()
#final password output box



def generator(y):
    "Generates the password"
    x = True
    i=0
    charType = []
    password = []
    #Initialises a list to be the correct size
    for i in range(0, y):
        charType.append("a")
        password.append("a")
        
    while x == True:
        #Adds random numbers that symbolise different character types
        for i in range(0,y):
            charType[i] = random.randrange(1,5)
        for i in range(0,y):
            #Creates a random lower case character
            if charType[i] == 1:
                randomLower = random.randrange(97,124)
                password[i] = chr(randomLower)
            #Creates a random upper case character
            elif charType[i] == 2:
                randomUpper = random.randrange(65,91)
                password[i] = chr(randomUpper)
            #Creates a random number character
            elif charType[i] == 3:
                randomNum = random.randrange(48,58)
                password[i] = chr(randomNum)
            #Creates a random special character
            elif charType[i] == 4:
                randomSpecial = random.randrange(33,48)
                password[i] = chr(randomSpecial)

        (x, y) = validator(password, y)


def validator(password, y):
    "Validates the password"
    lower = 0
    upper = 0
    num = 0
    special = 0

    #Checks what type of characters exist in the password
    for i in range(0,y):
        if ord(password[i]) >= 97 and ord(password[i]) <= 122:
            lower += 1
        elif ord(password[i]) >= 65 and ord(password[i]) <= 90:
            upper += 1
        elif ord(password[i]) >= 48 and ord(password[i]) <= 57:
            num += 1
        elif ord(password[i]) >= 33 and ord(password[i]) <= 47:
            special += 1
            
    #Checks that the password contains at least one of each character type      
    if lower > 0 and upper > 0 and num > 0 and special > 0:
        print("Your password has been successfully generated and validated!")
        print("Password > " + ''.join(password))
        return (False, y)

    else:
        return (True, y)


generator_btn = Button(root, text="Generate Password", command=generator)
generator_btn.pack()










root.mainloop()



