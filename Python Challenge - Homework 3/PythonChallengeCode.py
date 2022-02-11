import os
import csv

InputPath = os.path.join("Resources", "budget_data.csv")
OutputPath = os.path.join("Analysis", "budget_summary.txt")

# Open input file and read into csv reader:
with open(InputPath, "r", newline="") as ReadFile:
    DataReader = csv.reader(ReadFile, delimiter=",")
    
    # Skip header row:
    HeaderRow = next(DataReader)
    
    # Look at first row of data and initialize variables:
    FirstRow = next(DataReader)
    Month_Count = 1
    MonthlyGain_Max = 0
    MonthlyLoss_Max = 0
    MaxGainMonth = FirstRow[0]
    MaxLossMonth = FirstRow[0]
    
    Profit_FirstMonth = int(FirstRow[1])
    Profit_CurrentMonth = int(FirstRow[1])
    Profit_PriorMonth = int(FirstRow[1])
    
    NetProfit = int(FirstRow[1])

    # Loop through remaining rows and increment Month_Count and NetProfit:
    for Row in DataReader:
        Month_Count = Month_Count + 1
        Net_Profit = NetProfit + Profit_CurrentMonth
        
        # Calculate the ChangeInProfit between this month and the previous month:
        Profit_CurrentMonth = int(Row[1])
        Profit_Change = Profit_CurrentMonth - Profit_PriorMonth

        # If the ChangeInProfit is larger than MaxMonthlyGain, make it the new MaxMonthlyGain,
        # Else if the ChangeInProfit is smaller than  MaxMonthlyLoss, make it the new MaxMonthlyLoss:
        if Profit_Change > MonthlyGain_Max:
            MonthlyGain_Max = Profit_Change
            MaxGainMonth = Row[0]
        elif Profit_Change < MonthlyLoss_Max:
            MonthlyLoss_Max = Profit_Change
            MaxLossMonth = Row[0]
        PreviousMonthProfit = Profit_CurrentMonth

# Calculate the average of all changes in monthly profits using this simplification:
#   AvgChanges = ((Row2-Row1) + (Row3-Row2) + (Row4-Row3) + ... + (Row(n) - Row(n-1))) / (n-1)
#              = (Row2 - Row1 + Row3 - Row2 + Row4 - Row3 + ... + Row(n) - Row(n-1)) / (n-1)
#              = (Row2 - Row2 + Row3 - Row3 + Row4 - Row4 + ... + Row(n) - Row1) / (n-1)
#              = (Row(n) - Row1) / (n-1)
MeanMonthlyProfitChange = (Profit_CurrentMonth - Profit_FirstMonth) / (Month_Count - 1)

# Output to terminal:
print("Financial Analysis")
print("------------------")
print(f"Total Months: {Month_Count}")
print(f"Total: ${Net_Profit:,}")
print(f"Average Change: ${MeanMonthlyProfitChange:,.2f}")
print(f"Greatest Increase in Profits: {MaxGainMonth} (${MonthlyGain_Max:,})")
print(f"Greatest Decrease in Profits: {MaxLossMonth} (${MonthlyLoss_Max:,})")

# Open output file and write the results:
with open(OutputPath, "w", newline="") as WriteFile:
    print("Financial Analysis", file=WriteFile)
    print("------------------", file=WriteFile)
    print(f"Total Months: {MonthCount}", file=WriteFile)
    print(f"Total: ${NetProfit:,}",file=WriteFile)
    print(f"Average Change: ${MeanMonthlyProfitChange:,.2f}", file=WriteFile)
    print(f"Greatest Increase in Profits: {MaxGainMonth} (${MaxMonthlyGain:,})", file=WriteFile)
    print(f"Greatest Decrease in Profits: {MaxLossMonth} (${MaxMonthlyLoss:,})", file=WriteFile)