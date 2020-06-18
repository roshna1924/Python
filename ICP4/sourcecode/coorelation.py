import pandas as pd

df= pd.read_csv('train.csv')

#directly mapping value
df['Sex']=df['Sex'].replace( {'female': 1, 'male': 0} )

# use correlation function
print(df['Survived'].corr(df['Sex']))