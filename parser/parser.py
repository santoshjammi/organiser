#!/usr/bin/python
import csv , json

companies=["pushpak", "Euro Asia", "KC Capital"]

projectsCsvFilePath = "C:/projects/organizer/src/Projects.csv"
transactionsCsvFilePath = "C:/projects/organizer/src/Transactions.csv"
tasksCsvFilePath = "C:/projects/organizer/src/TaskList.csv"
jsonFilePath = "my_data.json"
arr = []
arr1 = []
arr2 = []
i=0
k=0
#read the csv and add the arr to a arrayn

with open (projectsCsvFilePath, encoding='utf-8') as projectsCsv:
    projectsReader = csv.DictReader(projectsCsv)
    for projectsRow in projectsReader:
        #arr.append(projectsRow)
        #i=i+1
        #print(projectsRow['opportunity'])
        with open (transactionsCsvFilePath, encoding='utf-8') as transactionsCsv, open (tasksCsvFilePath, encoding='utf-8') as taskCsv:
            transactionsReader = csv.DictReader(transactionsCsv)
            taskReader = csv.DictReader(taskCsv)

            for transactionsRow in transactionsReader:
                #print(transactionsRow['opportunity_in_transaction'])
                if ( transactionsRow['opportunity_in_transaction'] != '' ):
                    if (transactionsRow['opportunity_in_transaction'] in projectsRow['opportunity']):
                        #print(transactionsRow)
                        arr1.append(transactionsRow)
                        for taskRow in taskReader:
                            if taskRow['opportunity_in_task']!= "":
                                if ( (taskRow['opportunity_in_task'] in transactionsRow['opportunity_in_transaction']) and (taskRow['counterparty'] in transactionsRow['counterparty_in_transaction']) ):
                                    #print("Primary Contact is  " +taskRow['PrimaryContact'])
                                    print(taskRow)
                                    arr2.append(taskRow)
                        transactionsRow['tasks']=arr2
                        arr2=[]
            projectsRow['transactions']=arr1
            arr1=[]

        arr.append(projectsRow)
# write the data to a json file
with open(jsonFilePath, "w", encoding='utf-8') as jsonFile:
    jsonFile.write(json.dumps(arr, indent = 4))
