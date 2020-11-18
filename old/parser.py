#!/usr/bin/python
import csv , json

conCsvFilePath = "ContactList.csv"
oppCsvFilePath = "OpportunityList.csv"
tasCsvFilePath = "TaskList.csv"
jsonFilePath = "Output1.json"
arr = []
arr1 = []
i=0
k=0
#read the csv and add the arr to a arrayn

with open (conCsvFilePath, encoding='utf-8') as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        #arr.append(csvRow)

        i=i+1
        print(csvRow['Name'])
        with open (oppCsvFilePath, encoding='utf-8') as OpportunityCsv, open (tasCsvFilePath, encoding='utf-8') as taskCsv:
            oppReader = csv.DictReader(OpportunityCsv)
            taskReader = csv.DictReader(taskCsv)

            for oppRow in oppReader:
                if (oppRow['Contact1'] or oppRow['Contact2'] )!= "":
                    if (oppRow['Contact1'] or oppRow['Contact2']) in csvRow['Name']:
                        print("Contact 1 is  " +oppRow['Contact1']+ " and Contact2 is "+ oppRow['Contact2'] )
                        arr1.append(oppRow)

            csvRow['Opportunities']=arr1
            arr1=[]
            for taskRow in taskReader:
                if taskRow['PrimaryContact']!= "":
                    if taskRow['PrimaryContact'] in csvRow['Name']:
                        print("Primary Contact is  " +taskRow['PrimaryContact'])
                        arr1.append(taskRow)
            csvRow['tasks']=arr1
            arr1=[]

        arr.append(csvRow)
# write the data to a json file
with open(jsonFilePath, "w", encoding='utf-8') as jsonFile:
    jsonFile.write(json.dumps(arr, indent = 4))
