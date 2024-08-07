import pandas as pd

# Load the CSV file
csv_file = '/home/kunlay03/Documents/methane_final_data.csv'
df = pd.read_csv(csv_file)

# Save as Excel file
excel_file = '/home/kunlay03/Documents/methane_final_data.xlsx'
df.to_excel(excel_file, index=False)
