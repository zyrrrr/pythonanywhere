import csv

with open('./data/小学.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        print(row)

