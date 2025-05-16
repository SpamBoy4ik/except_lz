import pandas as pd

df = pd.read_csv('test.csv')
float_cols = df.select_dtypes(['object', 'float']).columns
print(list(float_cols))