# passwordGenerator.py


#attempt to open with flask
#from flask import Flask, render_template, request
#app = Flask(__name__)
#@app.route("Password")
#def Password():
#    return render_template("passwordgenerator.html")


#attempt to use TK

from tkinter import *
from tkinter.ttk import *
import random
#my own function to start

def start_gen():
    length=length_var.get()
    print("Your password length is"+ length)
    length_var.set("")






def main():
    print("Welcome to Password Generator \n")
    while True:
        length = eval(input("Enter how long you would like your password to be:"))
        
        if length < 8:
            print("A secure password should have a length greater than 8 please try again!")
        else:
            break
    
    generator(length)


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



#Creating GUI window
root = Tk()
var = IntVar() 
var1 = IntVar() 
root.title("Welcome to Password Generator")

#Final Password Output
password = Label(root, text="Your Password", font=("Arial", 16))
password.grid(row=7) 
entry = Entry(root) 
entry.grid(row=8) 

#start the app
start = Button(root, text="Start Application", command=main)
start.grid(row=0)

#Length label
combo_label = Label(root, text="How long would you like the password?", font=("Arial", 16))
combo_label.grid(row=1) 
#generate button
generate_button = Button(root, text="Generate Passowrd", command=generator)
#Entry
entry = Entry(root, textvariable = length_var, font=("Arial", 16))
entry.grid(row=2)
generate_button.grid(row=3)


#Creates passowrd

#if __name__=="__main__":
    #app.run(debug=True)

#Starting GUI
root.geometry("300x200")
root.mainloop() 

#Calling the app          
main()


#testing space--------------
#length = lengthvar.get()
