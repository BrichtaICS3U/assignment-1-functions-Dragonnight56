# Assignment 1
# ICS3U
# Jacky Liang
# March 28, 2018

def CtoF (C):
        '''Converts temperature in Celsius to Fahrenheit'''
        F = (1.8)*C+32
        return round(F)

###### uncomment this when you are ready to work on it
#def FtoC ():
#

temperature = float(input('Enter your temperature in Celsius: '))
print(CtoF(temperature), "Fahrenheit")
