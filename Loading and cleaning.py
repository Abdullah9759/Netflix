import pandas as pd 

df=pd.read_csv("netflix_titles.csv")
print(df.describe(include='all')) #Give the description aabout the data 

print(df.isnull().sum())  #finding total missing values 
df.fillna("Unknown",inplace=True)  #Putting unkown inplace of missing values
df = df.drop_duplicates()    #Removing duplicate from the dataset 
df['country'] = df['country'].str.strip().str.title()
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['date_added'] = df['date_added'].dt.strftime('%d-%m-%y') #adding date in format
df.columns = [col.lower().replace(" ","_") for col in df.columns]
df['release_year']=pd.to_numeric(df['release_year'], errors='coerce', downcast='integer') #converting to integer
print(df.head())
df.to_csv("cleaned_netflix_titles.csv", index = False) #saving the cleaned csv file
