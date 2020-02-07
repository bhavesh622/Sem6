import pandas as pd
lol = [] #list of list
with open('people.txt') as f:
    for line in f:
        inner_list = [line.strip() for line in line.split(' ')]
        lol.append(inner_list)
df = pd.DataFrame(lol)
df=df.rename(columns=df.iloc[0]).drop(df.index[0])
print(df)