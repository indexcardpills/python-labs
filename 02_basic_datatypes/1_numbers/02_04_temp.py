'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''
degrees_fahrenheit = input("how many degrees fahrenheit: ")
float(degrees_fahrenheit)
degrees_celsius = (degrees_fahrenheit-32) * (5/9)
float(degrees_celsius)
print(degrees_fahrenheit + "degrees fahrenheit = " + degrees_celsius + "degrees celsius")
#why doesn't this work?
