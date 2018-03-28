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


Question = input("What conversion do you want (C = In celsius, F = In Fahrenheit)? " )

if Question == "F" :
        temperature = float(input('Enter your temperature in Celsius: '))
        print(CtoF(temperature), "Fahrenheit")
elif Question == "C" :
        temperature = float(input('Enter your temperature in Fahrenheit: '))
        print(FtoC(temperature), "Celsius") 
