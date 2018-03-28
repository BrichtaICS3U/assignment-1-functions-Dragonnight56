# Assignment 1
# ICS3U
# Jacky Liang
# March 28, 2018

def CtoF (C):
        '''Converts temperature in Celsius to Fahrenheit'''
        F = (1.8)*C+32
        return round(F)

def FtoC (F):
        '''Converts temperature in Fahrenheit to Celsius'''
        C = (0.55556)*(F-32)
        return round(C)


#Ask for what conversion
Question = input("What conversion do you want (C = In celsius, F = In Fahrenheit)? " )

#Contiunes program depending on what was answered
if Question == "F" :
        temperature = float(input('Enter your temperature in Celsius: ')) #asks for number
        if temperature >= -273.15 : #check if input is too low
                print(CtoF(temperature), "Fahrenheit") #if passed does the conversion
        else :
                print("invalid input") #gives msg
                
elif Question == "C" :
        temperature = float(input('Enter your temperature in Fahrenheit: '))
        if temperature >= -459.67 :
                print(FtoC(temperature), "Celsius")
        else :
                print("invalid input")

