#Anthony Barnes
# Compound Interest with Loops
# Date 11/23/2024
# Prof.C

# Input for the Deposit,Rate,Months and Goal which has to have a positive amount.


fDeposit = 0
while fDeposit <= 0:
    try:
        fDeposit = int(input(f"What is the Original Deposit (positive value): "))
    except ValueError:
        print("Input must a positive numeric value")

iPer_Rate = 0
while iPer_Rate <= 0:
    try:
        iPer_Rate = float(input(f"What is the Interest Rate (positive value): ")) / 100 / 12
    except ValueError:
        print("Input must a positive numeric value")
iMonths = 0
while iMonths <= 0:
    try:
        iMonths = int(input(f"What is the number of Months (positive value): "))
    except ValueError:
        print("Input must a positive numeric value")
fGoal = -1
while fGoal < 0:
    try:
        fGoal = float(input("What is the Goal Amount (can enter 0 but not negative): "))
        if fGoal < 0:
           print("Input must 0 or greater")
    except ValueError:
        print("Input must a positive numeric value")

# Calculation for 12 month of interest


for month in range(1, iMonths + 1):
    fInt_Amt = fDeposit * iPer_Rate
    fDeposit += fInt_Amt

# Output Balance

    print(f"Month: {month} Account balance is: ${fDeposit:,.2f}")

if fGoal == 0:
    iMonths = 0

# Calculation beyond months of interest

while fDeposit < fGoal:
    fInt_Amt = fDeposit * iPer_Rate
    fDeposit += fInt_Amt
    iMonths += 1

# Output Balance

print(f"It will take: {iMonths} to reach the goal of ${fGoal:,.2f}")
