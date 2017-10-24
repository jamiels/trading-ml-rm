import pandas as pd

df = pd.read_csv('data/IBM.TradesOnly.012815.csv')

print(df.columns)

print(df.shape)
print(df.tail())
print(df.ix[177])
df = df.drop(' Conditions',axis=1)
print(df.head())
nb = df[' EventType']==' TRADE NB'
df = df[nb]
print(df.head())
print(df.tail())
df = pd.DataFrame(df,columns=[' Price'])
print(df.head())

df.plot.hist(alpha=.8)
df.diff().hist(color='k',alpha=.8,bins=20)