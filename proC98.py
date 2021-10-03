def swapData():
    fileName1 = input('Enter file name for file 1: ')
    fileName2 = input('Enter file name for file 2: ')
    #file1 = open(fileName1)
    #file2 = open(fileName2)
    with open(fileName1) as file1:
        data_A = file1.read()
        
    with open(fileName2) as file2:
        data_B = file2.read()

    file1 = open(fileName1,'w')
    file2 = open(fileName2,'w')
    file1.write(data_B)
    file2.write(data_A)
swapData()

