## Read Json to CSV
Data = '{"employee_name": "James", "email": "james@gmail.com", "job_profile": [{"title1":"Team Lead", "title2":"Sr. Developer"}]}'
print(pd.read_json(Data))

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header=None)

print(df.head())

# convert Json to csv

df.to_csv('wine.csv')
# convert Json to different json formats
df.to_json(orient="index")

df.to_json(orient="records")#it store according recordss
