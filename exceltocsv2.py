import openpyxl
import csv
import pandas as pd

# 1. Open the workbook using openpyxl instead of xlrd
wb = openpyxl.load_workbook("Test.xlsx", data_only=True)
sheet = wb.active # Gets the first sheet

# 2. Open the CSV file for writing
with open("T.csv", "w", newline="") as f:
    writer = csv.writer(f)

    # Iterate through the rows in the sheet
    for row in sheet.iter_rows(values_only=True):
        writer.writerow(row)

# 3. Read the CSV into Pandas (OUTSIDE the loop)
# This prevents the "printing 100 times" issue
df = pd.read_csv("T.csv")
print(df)