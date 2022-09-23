print("This Program prints the given text to AlTeRnAtE cApS")
test = input("enter the string you want? ")
for i in range(len(test)):
    if i % 2 == 0:
        test1 = (test[i].upper())
    else:
        test1 = (test[i])
    print(str(test1), end='')






