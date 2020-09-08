#making function
import time
mess='''___________________________________________________________| welcome in ankit calculator |_________________________________________________ '''
print(mess)

def sum():
    "this function is for addition"
    a=int(input("enter first num:- "))
    b=int(input("enter second num:- "))
    r=a+b
    re=f'''--------------
|result is|{r}|
--------------\n'''
    print(re)
def min():
    "this function is for subttraction"
    a=int(input("enter first num:- "))
    b=int(input("enter second num:- "))
    r=a-b
    re=f'''--------------
|result is|{r}|
--------------\n'''
    print(re)
def mult():
    "this function is for multipication"
    a=int(input("enter first num:- "))
    b=int(input("enter second num:- "))
    r=a*b
    re=f'''--------------
|result is|{r}|
--------------\n'''
    print(re)
def div():
    "this function is for division"
    a=int(input("enter first num:- "))
    b=int(input("enter second num:- "))
    r=a/b
    re=f'''--------------
|result is|{r}|
--------------\n'''
    print(re)
def power():
    "this function is for finding power"
    a=int(input("enter first num:- "))
    re=f'''--------------
|result is|{a*a}|
--------------\n'''
    print(re)

info='''1->addition
2->subtraction
3->multiplication
4->division
5->power
0->quit\n'''
print(info)

while(True):
        inp=int(input("enter num for yor calculation:- "))
        if inp==1:
            sum()
        if inp==2:
            min()
        if inp==3:
            mult()
        if inp==4:
            div()
        if inp==5:
            power()
        elif inp==0:
            break
        if inp>5:
            print("XXXX____dont give irelelent input____XXXX")
print("                     THANK YOU FOR USING CALCULATOR               ")

time.sleep(3)      


