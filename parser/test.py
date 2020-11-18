#!/usr/bin/python
import csv , json

projectsCsvFilePath = "C:/projects/organizer/src/Projects.csv"
transactionsCsvFilePath = "C:/projects/organizer/src/Transactions.csv"
tasksCsvFilePath = "C:/projects/organizer/src/TaskList.csv"
jsonFilePath = "my_data.json"
arr = []
arr1 = []
i=0
k=0
#read the csv and add the arr to a arrayn

with open (projectsCsvFilePath, encoding='utf-8') as projectsCsv:
    projectsReader = csv.DictReader(projectsCsv)
    for projectsRow in projectsReader:
        #arr.append(projectsRow)
        #i=i+1
        print(projectsRow['opportunity'])
        with open (transactionsCsvFilePath, encoding='utf-8') as transactionsCsv, open (tasksCsvFilePath, encoding='utf-8') as taskCsv:
            transactionsReader = csv.DictReader(transactionsCsv)
            taskReader = csv.DictReader(taskCsv)

            for transactionRow in transactionsReader:
                print(transactionRow['opportunity_in_transaction'])
                
