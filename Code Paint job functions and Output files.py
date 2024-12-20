# Anthony Barnes
# Code Paint job functions and Output files
# Date 12/06/2024
# Prof.C

# Input Validation
import math

def getFloatInput(prompt):
    while True:
        try:
            Paint_job = float(input(prompt))
            if Paint_job <= 0:
                print("Please enter a positive numeric number.")
            else:
                return Paint_job
        except ValueError:
            print("Input must be a positive numeric value.")

# Calculating Gallons of Paint Hours,Cost,Labor

def getGallonsOfPaint(fSqfeet_Wall, fFtper_gal):
    return  math.ceil(fSqfeet_Wall / fFtper_gal)

def getLaborHours(fLbr_hrs_per_1gal, iHowmuch_Paint):
    return (fLbr_hrs_per_1gal * iHowmuch_Paint)

def getLaborCost(fPersonHrs, fChghr):
    return (fPersonHrs * fChghr)

def getPaintCost(iHowmuch_Paint, fPaint_Price):
    return (iHowmuch_Paint * fPaint_Price)


# Calculating the Sales Tax for each specified State

def getSalesTax(sState, getPaintCost, getLaborCost):
    fTax_rate = 0.0

    if sState == "CT":
        fTax_rate = .06
    elif sState == "MA":
        fTax_rate = .0625
    elif sState == "ME":
        fTax_rate = .085
    elif sState == "NH":
        fTax_rate = .0
    elif sState == "RI":
        fTax_rate = .07
    elif sState == "VT":
        fTax_rate = .06

    fTotalcost_est = getPaintCost + getLaborCost
    return fTotalcost_est * fTax_rate

# Output from Calculating how much is needed

def showCostEstimate(fSqfeet_Wall, fPaint_Price, fFtper_gal, fLbr_hrs_per_1gal, fChghr, sState, sName):

    iHowmuch_Paint = getGallonsOfPaint(fSqfeet_Wall, fFtper_gal)
    fPersonHrs = getLaborHours(fLbr_hrs_per_1gal, iHowmuch_Paint)
    fTotal_Amt = getLaborCost(fPersonHrs, fChghr)
    fPriceCost = getPaintCost(iHowmuch_Paint, fPaint_Price)
    fTax_rate = getSalesTax(sState, fPriceCost, fTotal_Amt)


    print(f"Gallons of Paint Needed: {iHowmuch_Paint}")
    print(f"Hours of labor: {fPersonHrs}")
    print(f"Paint Charges: ${fPriceCost:,.2f}")
    print(f"Labor Charges: ${fTotal_Amt:,.2f}")
    print(f"Tax: ${fTax_rate:,.2f}")
    print(f"Total Cost Estimate: ${fTotal_Amt + fPriceCost + fTax_rate:,.2f}")

    # Output to a file

    with open('{sName}_PaintJob.output.txt', 'w') as outfile:
        outfile.write(f"Gallons of Paint Needed: {iHowmuch_Paint}\n")
        outfile.write(f"Hours of labor: {fPersonHrs}\n")
        outfile.write(f"Paint Charges: ${fPriceCost:.2f}\n")
        outfile.write(f"Labor Charges: ${fTotal_Amt:.2f}\n")
        outfile.write(f"Tax: ${fTax_rate:.2f}\n")
        outfile.write(f"Total Cost Estimate: ${fTotal_Amt + fPriceCost + fTax_rate:.2f}\n")

    print(f"File: {sName}_PaintJob.output.txt was created.")

def main():
    fSqfeet_Wall = getFloatInput(f"Enter wall space in square feet: ")
    fPaint_Price = getFloatInput(f"Enter paint price per gallon: ")
    fFtper_gal = getFloatInput(f"Enter feet per gallon: ")
    fLbr_hrs_per_1gal = getFloatInput(f"How many labor hours per gallon: ")
    fChghr = getFloatInput(f"Labor charge per hour: ")
    sState = input(f"State job is in: ")
    sName = input(f"Customer Last Name: ")

    showCostEstimate(fSqfeet_Wall, fPaint_Price, fFtper_gal, fLbr_hrs_per_1gal, fChghr, sState, sName )

main()

