import csv
fileName=r'Samples\SampleCSVFile_11kb.csv'
included_cols=[1, 8]
with open(fileName, 'r', encoding='cp850') as fdata:
    reader=csv.reader(fdata)
    for row in reader:
        print(row[1]) 
        content = list(row[i] for i in included_cols)
        print(content)
