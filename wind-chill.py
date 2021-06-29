# function calculates wind chill using user-inputted Celsius
def windChillCelsius():
    T = float(input("Enter temperature in Celsius "))
    V = float(input("Enter the wind speed in km/h "))
    windChill = 13.12 + 0.61215 * T - 11.37 * V**0.16 + 0.3965 * T * V**0.16
    windChillFahrenheit = (windChill * 9/5) + 32
    print("Wind chill is", windChill, "Celsius")
    print("Wind chill is", windChillFahrenheit, "Fahrenheit")

# function calculates wind chill using user-inputted Fahrenheit
# converts F to C for given equation then back to F for printed results
def windChillFahrenheit():
    f = float(input("Enter temperature in Fahrenheit "))
    V = float(input("Enter the wind speed in km/h "))
    T = (f-32)*5/9
    windChill = 13.12 + 0.61215 * T - 11.37 * V**0.16 + 0.3965 * T * V**0.16
    windChillFahrenheit = (windChill * 9/5) + 32
    print("Wind chill is", windChill, "Celsius")
    print("Wind chill is", windChillFahrenheit, "Fahrenheit")

print("This is a calculator for wind chill")

# calls above functions according to user entering temp in F or C
tempType = input("Do you want to enter in Fahrenheit or Celsius? Enter F or C ")
if tempType == "C" or tempType == "c":
    windChillCelsius()
elif tempType == "F" or tempType == "f":
    windChillFahrenheit()
else:
    print("Sorry, try again.")
