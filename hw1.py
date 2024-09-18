import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
df = pd.read_csv('student dropout.csv')
# df.info()

numeric_columns = df.select_dtypes(include=[np.number]).columns
for column in numeric_columns:
    df[column] = df[column].replace(0, np.nan) 
# print(df.isnull().sum())
df_new = df['Number_of_Absences'].dropna()
print(df_new)

m = df['Number_of_Absences'].mean()
print(m)
mean = round(m,2)
df_fill = df['Number_of_Absences'].fillna(mean.mean())
print(df_fill)
df_fill = df['Number_of_Absences'].ffill()
print(df_fill)
df_fill = df['Number_of_Absences'].bfill()
print(df_fill)