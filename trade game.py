#make a trading app
tnc='''XXXXXXXXXXXXXX This game is pwerd by indgamesXXXXXXXXXXXXXXXXXXXXXXX
*********about game**************
actually it is a type of trading app which  is for fun.
this have 50-50 chances of win randomly any one can win.
iff you win this game then you have color full sccreen for some time.
and if you loose then you have rgb colorfull screen

-----------how to play------------
..steps..
1>. file will load automaticaly
2>.computer will randomly choice the the b/w opponet and user
3>.who will get turn will be printed in screen
4>.then player have to predict that graph will go up or down
5>.then select that for how much sec you want to move graph
6>.after given interval of time you will have you result on your screen that you are looser or winerr
'''
import time
import random
def wait():
    t=random.randint(1,3)
    time.sleep(t)
    print("file loaded..")
print("                                       Game Powerd by AKELA(Made In India)                                       \n\n\n")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX------------------------welcome in ANKIT TRADING app-----------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#printing loading for sahort time
wait()
print("")
while True:
    print("________________________________________________________^^^^^^1-start........0-exit.....2-help^^^^^^^^_____________________________________________")
    r=int(input("Start or Exit\t"))
    print("")
    if r==1:
        #file work
        f=open("data.txt","w+")
        f.write(f"500")
        f.seek(0)
        r=f.read()
        ri=int(r)
        print("main balance = ",r)
        print("********deposit your amount and maximum amount is 100**************")
        ad=int(input(""))
        ub=ri-ad
        print(ub)
        f.write(f"{ub}")
        print("now bal is",f.read())
        #selecting player
        p_selct=random.choice([":::::::::opponent turn:::::::::::","::::::::::::your turn::::::::::::::"])
        print(p_selct)
        print("")
        #print(f"{} has selected to pridict")
        if p_selct=="::::::::::::your turn::::::::::::::":
            print("-----------------------predict that graph will go up or down------------------")
            print("/\/\/\/\/\/\/\/\^^^^^^^^^^^U-up.......D-down^^^^^^^^^/\/\/\/\/\/\/\\/\/\/\/\//\\")
            gr=input("tell graph will go up or down:-  ")
            grc=gr.upper()
            print("your choice is",grc)
            print("")
            #random graph program
            while True:
                print("----------- select time of graph for how much time you want play it --------")
                t=int(input("time=  "))
                print(f"you selected {t} sec time")
                print("graph is |-\n")
                for i in range(t*3):
                    a=random.randint(3,25)
                    print("%"*a,"*")
                    time.sleep(0.3)
                time.sleep(1)
                break
            if grc=="U":
                if a>12:
                    print("(((you win and opponent loos)))")
                else:
                    print("???you loos and opponent win???")

            elif grc=="D":
                if a<12:
                    print("(((you win and opponent loos)))")
                else:
                    print("???you loos and opponent win???")

        else:
            print("")
            ad=random.randint(1,100)
            print(f"opponent deposited amount is {ad}")
            pre=random.choice(["U","D"])
            time.sleep(random.randint(1,2))
            print("opponent selected",pre)
            time.sleep(random.randint(1,2))
            otm=random.randint(1,12)
            print("")
            print(f"opponent selected {otm} sec time")
            #random graph program
            while True:
                for i in range(otm*3):
                    a=random.randint(3,25)
                    print("%"*a,"*")
                    time.sleep(0.3)
                time.sleep(1)
                break
            if pre=="U":
                if a>12:
                    print("(((you win and opponent loos)))")
                else:
                    print("???you loos and opponent win???")

            elif pre=="D":
                if a<12:
                    print("(((you win and opponent loos)))")
                else:
                    print("???you loos and opponent win???")

    
    elif r==2:
        print(tnc)

    else:
        break
        
            
                        
                 
                         
        
        
        
        
