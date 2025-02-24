fahrenheit_temps = [32, 50, 77, 100, 212]

celsius_temps = [(f - 32) * 5 / 9 for f in fahrenheit_temps]

print("Temperatures in Fahrenheit:", fahrenheit_temps)
print("Equivalent Temperatures in Celsius:", celsius_temps)
