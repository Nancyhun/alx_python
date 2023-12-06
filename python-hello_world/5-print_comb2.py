for i in range(100):
    if i < 99:
        print(str(i).zfill(2), end=", ")
    else:
        print(str(i).zfill(2))