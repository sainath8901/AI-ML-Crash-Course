import pandas as pd

def main():
    df = pd.read_csv('Walmart.csv')
    print("Dataset Loaded")
# Printing the following
# first 5 rows
    print(df.head())
# last 10 rows
    print(df.tail(10))
# all values
    print(df.values)
# rows, columns
    print("Shape:", df.shape)
# each column’s data type
    print("Data types:\n", df.dtypes)
# column names
    print("Columns:", list(df.columns))

    print(f"Total weekly sales = {df['Weekly_Sales'].sum()}")
# copy of one column
    print(df['Weekly_Sales'].copy())
# subset of columns
    print(df[['Date', 'Weekly_Sales', 'Fuel_Price']])

    df.insert(4, 'Description', 'describe')
    print(df.head())

# Dropping any row missing Fuel_Price or Temperature, then fill other NaNs with 0
    df_clean = df.dropna(subset=['Fuel_Price', 'Temperature']).fillna(0)
    print(df_clean)

    print(f"Highest Temperature: {df_clean['Temperature'].max()}")
    print(f"Lowest gas price: {df_clean['Fuel_Price'].min()}")

if __name__ == '__main__':
    main()
