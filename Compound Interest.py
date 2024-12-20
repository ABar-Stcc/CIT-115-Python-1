# This is my second assignment (Compound Interest)
# Date 10/12/2024
# Professor C is my Professor
# Anthony Barnes


#INPUT
iPV = int(input ("Enter the starting principal: "))
fRATE = float(input("Enter the annual interest rate: ")) / 100
iTIME = int(input("How many times per year is the interest compounded? "))
fOCCUR = float(input("For how many years with the account earn interest? "))


fPV = iPV *(1 + fRATE / iTIME) ** (iTIME * fOCCUR)

#Output
print(f"At the end of years you will have ${fPV:3,.2f}")
