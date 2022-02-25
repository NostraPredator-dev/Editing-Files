def swap():
    file1 = input("Enter name of file 1 : ")
    file2 = input("Enter name of file 2 : ")

    with open(file1,'r') as a:
        data_a = a.read()
        a.close()
    with open(file2,'r') as b:
        data_b = b.read()
        b.close()
    with open(file2, 'w') as a:
        a.write(data_a)
        a.close()
    with open(file1, 'w') as b:
        b.write(data_b)
        b.close()

    print("Swapped")

swap()