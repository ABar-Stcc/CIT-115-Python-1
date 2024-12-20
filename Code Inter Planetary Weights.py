## My first program Anthony Barnes ##
## Date 10/3/24 ##

#NAME CONSTANT
fMERCURY  = 0.38
fVENUS    = 0.91
fMOON     = 0.165
fMARS     = 0.38
fJUPITER  = 2.34
fSATURN   = 0.93
fURANUS   = 0.92
fNEPTUNE  = 1.12
fPLUTO    = 0.066
fEARTHWGT = 100
fWEIGHT   = 70.5

# Input - Name of Person
sName = input("What is your name: ")

# Input - Weight
sUserWeight = input("What is your weight: ")

#Conversion
fWEIGHT = float(sUserWeight)

fMERCURY = fWEIGHT * fMERCURY
fVENUS   = fWEIGHT * fVENUS
fMOON    = fWEIGHT * fMOON
fMARS    = fWEIGHT * fMARS
fJUPITER = fWEIGHT * fJUPITER
fSATURN  = fWEIGHT * fSATURN
fURANUS  = fWEIGHT * fURANUS
fNEPTUNE = fWEIGHT * fNEPTUNE
fPlUTO   = fWEIGHT * fPLUTO

# Output of Planet weights

print(f"Moose here are your weights on our Solar System's planets: ")
print(f"{"Weight on Mercury:":21s} {fMERCURY:10.2f}")
print(f"{"Weight on Venus:":21s} {fVENUS:10.2f}")
print(f"{"Weight on our Moon:":21s} {fMOON:10.2f}")
print(f"{"Weight on Mars:":21s} {fMARS:10.2f}")
print(f"{"Weight on Jupiter:":21s} {fJUPITER:10.2f}")
print(f"{"Weight on Saturn:":21s} {fSATURN:10.2f}")
print(f"{"Weight on Uranus:":21s} {fURANUS:10.2f}")
print(f"{"Weight on Neptune:":21s} {fNEPTUNE:10.2f}")
print(f"{"Weight on Pluto:":21s} {fPlUTO:10.2f}")
