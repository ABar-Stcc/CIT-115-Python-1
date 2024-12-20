# Anthony Barnes 3rd assignment
# OCT-21-2024
# Code Temperture Converter

sName1 = "Prof C's"
fFahrenheit = 212
fCelsius = 100
fTemperature = float
sTemp = str

print(f"{sName1} Temp Converter:")

fTemperature = float(input("Enter a temperature: "))
sTemp = input("Is the temp F for Fahrenheit or C for Celsius? ").lower()

if sTemp != "f" and sTemp != "c":
    print("You must enter a F or C")

if sTemp == "f":
    if fTemperature > 212:
        print("Temp can not be > 212")

    else:
        fCelsius = (5.0 / 9) * (fTemperature - 32)
        print(f"The Celsius equivalent is: {fCelsius:.1f}")

elif sTemp == 'c':
    if fTemperature > 100:
        print("Temp can not be > 100")
    else:
        fFahrenheit = ((9.0 / 5.0) * fTemperature) + 32
        print(f"The Fahrenheit equivalent is: {fFahrenheit:.1f}")

