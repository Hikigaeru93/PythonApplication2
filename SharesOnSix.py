a = input('Enter number: ')
b = a.isdigit()
if b == True:
    c = (int(a)%6)
    if c == 0:
        print("Shares")
    else :
        print("Not Shares")
else:
    print("Please, enter the NUMBER")