print('enter 1 for addition \nenter 2 for subtraction \nenter 3 for multiplication \nenter 4 for division of no.1/no2\nenter 5 for division of no.2/no1')
z=int(input('enter the number to select the opreation' ))

def calculator(a,c):
    if z==1:
        return a+b
    elif z==2:
        return a-b
    elif z==3:
        return a*b
    elif z==4:
        return a/b
    elif z==5:
        return b/a
if z>4:
    print('There is no opreation assined to the number')
else :
    a=int(input('enter no.1 :'))
    b=int(input('enter no.2 :'))
    print('your answer is:',calculator(a,b))
   

