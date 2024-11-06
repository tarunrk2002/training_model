import pandas as pd
excel_file_path = "WalmartData2022To2024.xlsx"
data = pd.read_excel(excel_file_path)
data['Date']=pd.to_datetime(data['week_end_date'])
data = data.drop(['week_end_date', ], axis=1)

data = data.sort_values(by='Date')

data.to_csv('WalmartData2022To2024_sorted.csv',index=False)   







