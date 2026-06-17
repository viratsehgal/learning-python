def temperature_converter(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit 

def temperature_converter_k(celsius):
    kelvin = celsius + 273.15
    return kelvin

celsius_input = float(input("Enter the temperature in celsius: "))
fahrenheit_output = temperature_converter(celsius_input)
kelvin_output = temperature_converter_k(celsius_input)
print("The temperature in fahrenheit is :" , fahrenheit_output)
print("The temperature in kelvin is :" , kelvin_output)
