# Assignment 1 (The Tempverter!)
# ICS3U
# Jacky Liang
# March 28, 2018

#Coversion funcs
def CtoF (C):
        '''Converts temperature in Celsius to Fahrenheit'''
        F = (1.8)*C+32
        return round(F)

def FtoC (F):
        '''Converts temperature in Fahrenheit to Celsius'''
        C = (0.55556)*(F-32)
        return round(C)


#The Program

Run = True #Bool to run program
Another = "Y" #Bool to check if want to do another run
Counter = 0 #Check how many times program is used


#Loop to let the program run multi times
while Run == True :
        if Another == "N" : #When doesn't want do another
                print("Thanks for using this program!") #End msg
                print("You used it", Counter , "time(s)!") #tells how many times used
                Run = False # end program
        elif Another == "Y":
                if Counter == 0 : #First run msg
                        print("Welcome to the Tempverter! (Temperature Converter)")
                        print("*THIS PROGRAM IS CASE SENSITIVE*") #warning msg                       

                Question = input("What conversion do you want (C = In celsius, F = In Fahrenheit)? " ) #Ask for what conversion
                #Contiunes program depending on what was answered
                if Question == "F" :
                        temperature = float(input('Enter your temperature in Celsius: ')) #asks for number
                        if temperature >= -273.15 : #Check if input is too low
                                Counter += 1 #Counts how many times program ran
                                print(CtoF(temperature), "Fahrenheit") #If passed does the conversion
                                Another = input("Another conversion (Y = yes, N = no)? ")  #Ask for another conversion                               
                        else :
                                print("Sorry, input too low.") #Gives error msg
                elif Question == "C":
                        temperature = float(input('Enter your temperature in Fahrenheit: '))
                        if temperature >= -459.67 :
                                Counter += 1
                                print(FtoC(temperature), "Celsius")
                                Another = input("Another conversion (Y = yes, N = no)? ")
                        else :
                                print("Sorry, input too low.")
                else :
                        print("Sorry, I couldn't understand that.")
        else :
                print("Sorry, I couldn't understand that.")
                Another = input("Another conversion (Y = yes, N = no)? ")

