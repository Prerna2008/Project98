file1= input("Enter the 1 st file Name")
file2= input("Enter the 2nd file Name")
def swapFileData():
    with open(file1,'r') as a:
        data_a = a.read()
    with open(file1,'w') as a:
        a.write('data_b')
swapFileData()