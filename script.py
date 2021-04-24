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

choice = int(input())
if choice == 1:
    slNoInput = input("Enter Serial No:  ")
    with open("gsquarterly_december-2020-revised.csv", "rt") as f:
        reader = csv.reader(f, delimiter=",")
        for i, row in enumerate(reader):
            if i != 0:
                if slNoInput.strip() == row[0]:
                    print(row)


if choice == 2:
    accInput = input("Enter Account:  ")
    with open("gsquarterly_december-2020-revised.csv", "rt") as f:
        reader = csv.reader(f, delimiter=",")
        for i, row in enumerate(reader):
            if i != 0:
                if accInput.strip() == row[2]:
                    print(row)

if choice == 3:
    codeInput = input("Enter Code:  ")
    with open("gsquarterly_december-2020-revised.csv", "rt") as f:
        reader = csv.reader(f, delimiter=",")
        for i, row in enumerate(reader):
            if i != 0:
                if codeInput.strip() == row[3]:
                    print(row)


if choice == 4:
    countryCodeInput = input("Enter Country Code:  ")
    with open("gsquarterly_december-2020-revised.csv", "rt") as f:
        reader = csv.reader(f, delimiter=",")
        for i, row in enumerate(reader):
            if i != 0:
                if countryCodeInput.strip() == row[4]:
                    print(row)

if choice == 5:
    productTypeInput = input("Enter Product Type:  ")
    with open("gsquarterly_december-2020-revised.csv", "rt") as f:
        reader = csv.reader(f, delimiter=",")
        for i, row in enumerate(reader):
            if i != 0:
                if productTypeInput.strip() == row[5]:
                    print(row)

if choice == 6:
    valueInput = input("Enter Value:  ")
    with open("gsquarterly_december-2020-revised.csv", "rt") as f:
        reader = csv.reader(f, delimiter=",")
        for i, row in enumerate(reader):
            if i != 0:
                if valueInput.strip() == row[6]:
                    print(row)

if choice == 7:
    statusInput = input("Enter Status:  ")
    with open("gsquarterly_december-2020-revised.csv", "rt") as f:
        reader = csv.reader(f, delimiter=",")
        for i, row in enumerate(reader):
            if i != 0:
                if statusInput.strip() == row[7]:
                    print(row)

if choice == 8:
    with open("gsquarterly_december-2020-revised.csv", "rt") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            print(row)