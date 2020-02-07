import pandas as pd
df = pd.read_csv('peoples.txt', sep=' ')
def ageCheck(df):
    age_range = lambda r : r in range(151)
    print(df["Age"].apply(age_range))
ageCheck(df)
def ageMarried(df):
    age_married= lambda x : x[0]>x[1]
    print(df[["Age","yearsmarried"]].apply(age_married,axis=1))
ageMarried(df)
def status(df):
    status_check= lambda x : x in {'married','single','widowed'}
    print(df["status"].apply(status_check))
status(df)
def ageRange(df):
    age_group= lambda x : (x[0]<18 and x[1]=='child') or (18<=x[0]<=65 and x[1]=='adult') or (x[0]>65 and x[1]=='elderly')
    print(df[["Age","agegroup"]].apply(age_group,axis=1))
ageRange(df)
ruleset= {"Agecheck": ageCheck,"ageMarried":ageMarried,"status":status,"ageRange":ageRange}
ruleset["AgeCheck"](df)
