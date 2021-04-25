import csv

fileName = "gsquarterly_december-2020-revised.csv"

def getData ( index ):
    if index != -1:
        inputValue = input("Enter Data : ")

    with open(fileName, "rt") as f:
        for i, row in enumerate(csv.reader(f, delimiter=",")):
            if i != 0:
                if index == -1:
                    print(row)
                else:
                    if str(inputValue).strip() == str(row[index]):
                        print(row)

def listData ():
    getData( -1 )

def searchData ():
    print("> [ Press 1 ] Serial No")
    print("> [ Press 2 ] Account")
    print("> [ Press 3 ] Code")
    print("> [ Press 4 ] Country Code")
    print("> [ Press 5 ] Product Type")
    print("> [ Press 6 ] Value")
    print("> [ Press 7 ] Status")

    searchChoice = int(input())

    if searchChoice == 1:
        getData( 0 )
    else :
        getData( searchChoice )

def sortData ():
    print("> [ Press 1 ] Serial No")
    print("> [ Press 2 ] Account")
    print("> [ Press 3 ] Code")
    print("> [ Press 4 ] Country Code")
    print("> [ Press 5 ] Product Type")
    print("> [ Press 6 ] Value")
    print("> [ Press 7 ] Status")

    sortChoice = int(input())

    if sortChoice == 1:
        reArrangeData( 0 )
    else :
        reArrangeData( sortChoice )


def reArrangeData( index ):
    with open(fileName, "rt") as f:
        for i, row in enumerate(csv.reader(f, delimiter=",")):
            print(row)
            # for j in range(i+1, len(arr)):
    #Sort the array in ascending order    
    # for i in range(0, len(arr)):    
    #     for j in range(i+1, len(arr)):    
    #         if(arr[i] > arr[j]):    
    #             temp = arr[i];    
    #             arr[i] = arr[j];    
    #             arr[j] = temp;

print("[ Press 1 ] List")
print("[ Press 2 ] Search")
print("[ Press 3 ] Sort")

mainChoice = int(input())

if mainChoice == 1:
    listData()

if mainChoice == 2:
    searchData()

if mainChoice == 3:
    sortData()