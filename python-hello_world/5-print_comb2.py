for i in range(10):
    for j in range(10):
        if int(str(i)+str(j)) == 99:
            print(str(i)+str(j))
        else:
            print(str(i)+str(j), end=", ")    
            