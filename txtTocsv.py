import pandas as pd
import csv
csv_columns = ['time','ID','name', 'text']

f = open('dataquery.txt', 'r', encoding='utf-8')
list = f.readlines()
dictList = []
for i in list:
    dictList.append(eval(i))

print(dictList)

csv_file = "dataquery.csv"
try:
    with open(csv_file, 'w', encoding='utf-8-sig') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dictList:
            writer.writerow(data)
except IOError:
    print("I/O error")

# df = pd.read_csv("dataquery.txt",delimiter="\n")
#
# df.to_csv("test3.csv", encoding='utf-8', index=False)
with open('file_path', 'r', encoding='utf-8') as chatlog_file:
    chatlog_list = [line.strip() for line in chatlog_file if line.strip() != ""]
ss = originalF.readline()

print(ss)
