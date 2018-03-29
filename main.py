# Assignment 1
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

Run = True #Bool to check if want to continue running program

#Ask for what conversion
Question = input("What conversion do you want (C = In celsius, F = In Fahrenheit)? " )

#Loop to let the program run multi times
while Run == True :
        #Contiunes program depending on what was answered
        if Question == "F" and Run == True :
                temperature = float(input('Enter your temperature in Celsius: ')) #asks for number
                if temperature >= -273.15 : #Check if input is too low
                        print(CtoF(temperature), "Fahrenheit") #If passed does the conversion
                        Run = False #Ends the run
                else :
                        print("invalid input") #Gives msg
        elif Question == "C" :
                temperature = float(input('Enter your temperature in Fahrenheit: '))
                if temperature >= -459.67 :
                        print(FtoC(temperature), "Celsius")
                        Run = False #Ends the run
                else :
                        print("invalid input")

