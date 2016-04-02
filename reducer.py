import csv
import collections
import os

array= []
results= {}
toCSV = {}
with open('result.csv') as result:
	reader = csv.DictReader(result)
	i=0
	for row in reader:
		results = {}
		i=i+1
		se = row['se']
		results["Requested memory"] = se  
		toCSV[i] = results



with open('result1.csv') as result:
	reader = csv.DictReader(result)
	i=0
	for row in reader:
		results = {}
		i=i+1
		se = row['se']
		toCSV[i]["Allocation Processors"] = se
		

def WriteDictToCSV(csv_file,csv_columns,dict_data):
    
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
            	
                writer.writerow(data)
    except IOError as (errno, strerror):
            print("I/O error({0}): {1}".format(errno, strerror))    
    return 

 
for i in range(1,13):
	array.append(toCSV[i])

# print array


dict_data=array
csv_columns = ["Allocation Processors","Requested memory"]
WriteDictToCSV('prediction.csv',csv_columns,array)

#print array

# keys = toCSV[1].keys()

# with open('prediction.csv','wb') as csvfile:
#      writer = csv.writer(csvfile)
#      writer.writerow(array)