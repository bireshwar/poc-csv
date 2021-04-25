# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 04:45:48 PM 2021

@author: Bireshwar
"""
import csv

print("Press 1 to Search by Serial No")
print("Press 2 to Search by Account")
print("Press 3 to Search by Code")
print("Press 4 to Search by Country Code")
print("Press 5 to Search by Product Type")
print("Press 6 to Search by Value")
print("Press 7 to Search by Status")
print("Press 8 to List all data")

def getData ( searchText, index ):
    with open("gsquarterly_december-2020-revised.csv", "rt") as f:
        for i, row in enumerate(csv.reader(f, delimiter=",")):
            if i != 0:
                if searchText == "all":
                    print(row)
                else:
                    inputValue = input(searchText)
                    if str(inputValue).strip() == str(row[index]):
                        print(row)

choice = int(input())
if choice == 1:
    getData("Enter Serial No:  ", 0 )

if choice == 2:
    getData("Enter Account:  ", 2 )

if choice == 3:
    getData("Enter Code:  ", 3 )

if choice == 4:
    getData("Enter Country Code:  ", 4 )

if choice == 5:
    getData("Enter Product Type:  ", 5 )

if choice == 6:
    getData("Enter Value:  ", 6 )

if choice == 7:
    getData("Enter Status:  ", 7 )

if choice == 8:
    getData("all", 0 )