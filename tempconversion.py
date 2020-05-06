#Author: Vishwajeet Bamane
#Last modified: 05/05/2020

def celtofeh():
	cel = float(input("Enter celcius value:\n"))
	feh = (cel*9/5) + 32
	print(feh,"°F")
	print("Thank you")
	quit()
def fehtocel():
	feh = float(input("Enter Fahrenheit value:\n"))
	cel = (feh-32)*5/9 
	print(cel,"°C")
	print("Thank you")
	quit()


print("Temperature conversion\n")

print("What you want to convert?")

print("Enter 1 for Celcius to Fahreinheit")
print("Enter 2 for Fahrenheit to Celcius")
var1 = input()
if var1 == "1":
	celtofeh()
if var1 == "2":
	fehtocel()
else:
	print("Sorry! Invalid Input.")