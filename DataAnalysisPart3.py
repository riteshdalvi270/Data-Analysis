import pandas as pd

df = pd.read_csv("ZILLOW-Z77006_ZHVI3B.csv")

#print(df.head())

df.set_index('Date', inplace=True)

print(df.head())

df.to_csv("Zillow-House-three-bedroom.csv")

df = pd.read_csv("Zillow-House-three-bedroom.csv", index_col=0)

df.columns = ['House Price']

df.to_csv("Zillow-House-three-bedroom-new.csv", header=False)

print(df.head());


df = pd.read_csv("Zillow-House-three-bedroom-new.csv", names=['Dates', 'House Price'], index_col=0)

print(df.head())

df.to_html("example.html")

df.rename(columns={'House Price':'Price'}, inplace=True)

print(df.head())
