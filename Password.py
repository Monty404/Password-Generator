#Asks for Application name
#Asks for a username
#Asks how many characters that are needed
#Display the Application in the follow: Application - Username - Password

import random
import string
from os import path

file_name = "password.txt"
special_ch = ['!','$','%','&','(',')']#special character list
app= str(input("The name of the application is: "))#waits for string input
User = str(input("Your username is: "))#waits for string input
maxCH = int(input("This is how many charcters I need: "))#waits for int input
passw = []#empty list, stores the password data temp

if path.exists(file_name) != True:#check to see if the file exist
    f_pass = open(file=file_name,mode="w+")
    f_pass.close()

def pass_create():#creates password
    for i in range(maxCH):#checks for the max char needed
        NumChk = random.randint(0,2)#1/3 chances for types of chars to be used
        if NumChk == 0:
            letter = random.choice(string.ascii_letters)#52 letters includes upper case
            passw.append(letter)#adds to the password
        elif NumChk == 1:
            num = str(random.randint(0,9))#9 numbers
            passw.append(num)#adds to the password
        else:
            spec_ch = random.choice(special_ch)#common special characters from the list
            passw.append(spec_ch)#adds to the password
    pass_file()

def pass_file():#files/adds the password into a text based doc
    f_pass = open(file=file_name,mode="a")
    passwto = ''.join(passw)
    f_pass.write(f"Appliction: {app}\nUsername: {User}\nPassword: {passwto}\n\n")
    f_pass.close()

pass_create()