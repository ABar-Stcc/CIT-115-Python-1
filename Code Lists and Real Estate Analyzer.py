# Anthony Barnes
# Lists and Real Estate Analyzer.py
# Date 12/19/2024
# Prof.C

#Input Validation

def getFloatInput(prompt):
    while True:
        try:
            Value = float(input(prompt))
            if Value <= 0:
                print("Please enter a positive, non-zero value.")
            else:
                return Value
        except ValueError:
            print("Input a number that is greater then 0.")

# Input

def getMedian(fValue: list, iNum):
    iMid = iNum // 2

    if iNum % 2 == 1:
        return fValue[iMid]
    else:
        fMed = (fValue[iMid - 1] + fValue[iMid]) / 2
        return fMed

# Calculate the For and while loop

def main():
    iSale_Value = []

    while True:
        fSale_Amt = getFloatInput("Enter property sales value: ")
        iSale_Value.append(fSale_Amt)

        while True:
            sSecond_Value = input("Enter another value Y or N: ").lower()

            if sSecond_Value == "y":
                break
            elif sSecond_Value == "n":
                break
            else:
                print("Invalid input. Please enter Y or N.")

        if sSecond_Value == 'n':
            break
# Calculate the sale of property with a range and sort

    iNum = len(iSale_Value)
    iSale_Value.sort()

    for index in range(iNum):
        sale = iSale_Value[index]
        print(f"Property {index + 1} $   {sale:10,.2f}")

# Calculate and display the minimum, maximum, total, average, and median
    min_value = min(iSale_Value)
    max_value = max(iSale_Value)
    total_value = sum(iSale_Value)
    average_value = total_value / len(iSale_Value)
    median_value = getMedian(iSale_Value, iNum)

#  Commission calculation
    commission_value = total_value * 0.03

# Output results
    print(f"Minimum:    $ {min_value:13,.2f}")
    print(f"Maximum:    $ {max_value:13,.2f}")
    print(f"Total:      $ {total_value:13,.2f}")
    print(f"Average:    $ {average_value:13,.2f}")
    print(f"Median:     $ {median_value:13,.2f}")
    print(f"Commission: $ {commission_value:12,.2f}")


main()

