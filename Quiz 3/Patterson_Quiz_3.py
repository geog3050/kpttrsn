#Takes in the type of climate the user measured data from
climate = input("What Climate was the data measured in (Tropical, Continental, Other)?")

#checks the type of climate entered and sets the Temperature Threshold as appropriate. Checks for TypeError from user input
try:
if climate == "Tropical" or climate == "tropical":
	Tthreshold = 30
elif climate == "Continental" or climate == "continental":
	Tthreshold = 25
else:
	Tthreshold = 18
except TypeError:
	print("Climate type must be entered as a string.")


#inputs the user's temperature data
temps = eval(input("Enter the temperatures recorded in celsius, separated by commas"))

#checks if each individual temperature is under or over the threshold to determine folding. Checks for TypeError from user input
try:
for i in range (0, len(temps)-1):
	if temps[i] > Tthreshold:
		print("U")
	else:
		print("F")
except TypeError:
	print("Temperatures must be entered as integer or float values, separated by commas."))