# import csv
# file = open('Salary_Data.csv', 'a')
# mydict =[{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'}, 
#          {'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'}, 
#          {'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'}, 
#          {'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'}, 
#          {'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'}, 
#          {'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}]
# fields = ['name', 'branch', 'year', 'cgpa'] 
# writer= csv.DictWriter(file, fieldnames= fields)
# writer.writeheader()
# writer.writerows(mydict)
# file.close()
# =============================================================================
import csv
fields = ['name', 'branch', 'year', 'cgpa'] 
arr=[['mahmoud', 1, 1997, 22],['mahmoud', 1, 1997, 22],['mahmoud', 1, 1997, 22]]
file2 = open('Salary_Data2.csv', 'w', newline='') # newline='' to prevent printing empty line between each row
writer= csv.writer(file2)
writer.writerow(fields)
writer.writerows(arr)
file2.close()

file3 = open('Salary_Data2.csv')
csvreader = csv.reader(file3)
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)
print(header)
print(rows)