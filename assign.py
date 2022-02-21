def swap():
    file1 = input("Enter name of file 1 : ")
    file2 = input("Enter name of file 2 : ")

    with open(file1,'r') as a:
        data_a = a.read()
    with open(file2, 'w') as a:
        a.write(data_a)
    
    with open(file2,'r') as b:
        data_b = b.read()
    with open(file1, 'w') as b:
        b.write(data_b)

    print("Swapped")

swap()