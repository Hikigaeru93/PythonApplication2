list1 = ['January',"February",'March','April','May',"Juny",'July','August','September','October','November','December']
a = int(input('Enter number of your month: '))
while a >= 13 or a <= 0:
    a = int(input('Enter number from 1 to 12! Your number: '))
print(list1[a-1])
