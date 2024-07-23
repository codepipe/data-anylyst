import pandas as pd

# Load the Excel file
file_path = 'path_to_your_excel_file.xlsx'
sheet1 = pd.read_excel(file_path, sheet_name='Sheet1')
sheet2 = pd.read_excel(file_path, sheet_name='Sheet2')

# Perform VLOOKUP-like merge
result = pd.merge(sheet1, sheet2, on='ID', how='left')

print(result)

