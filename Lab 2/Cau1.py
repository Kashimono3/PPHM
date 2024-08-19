import pandas as pd
import csv


filename = "data.csv"
df = pd.read_csv(filename)
print('pandas ')
print(df)

print("========================================")
with open(filename,mode='r') as file:
    csv_reader = csv.DictReader(file)
    data = [row for row in csv_reader]
    for row in data:
        print(row)