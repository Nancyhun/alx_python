for i in range(10):
    for j in range(i+1, 10):
        if int(str(i)+str(j)) == 89:
            print(str(i)+str(j))
        else:
            print(str(i)+str(j), end=", ")    
            