import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

excel_file_path = "perrin-freres-monthly-champagne-.csv"
data = pd.read_csv(excel_file_path)

#changing the names for the columns
data.columns=['Month','Sales']

#removing the rows with missing values with drop method
data.drop(105, axis=0, inplace=True)
data.drop(106, axis=0, inplace=True)

#sometimes the data is not in the right format so we need to convert it . here, we are converting it to datetime 
data['Month'] = pd.to_datetime(data['Month'])


data.set_index('Month', inplace=True)
# data.plot()

# plt.show()

test_result = adfuller(data['Sales'])

print(test_result)










