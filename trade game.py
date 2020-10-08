#make a trading app
tnc='''XXXXXXXXXXXXXX This game is pwerd by AKELA XXXXXXXXXXXXXXXXXXXXXXX
*********about game**************
actually it is a type of trading app which  is for fun.
this have 50-50 chances of win randomly any one can win.
if you win this game then you have color full sccreen for some time.
and if you loose then you have blinking red color screen for some time

-----------how to play------------
..steps..
1>. file will load automaticaly
2>.computer will randomly choice the tern b/w opponet and user.who will get turn will be printed in screen
3>.then player will deposit his amount
4>.then player have to predict that graph will go up or down
5>.then select that for how much sec you want to move graph
6>.after given interval of time you will have you result on your screen that you are looser or winerr

XXXXXXXXXXXXXXXXXXXXXXXXX
1>.winner should have money
2>.looser should loss ther money
3>.if player bank get empty then game dhould warn

'''
import time
import random
import os
def wait():
    t=random.randint(1,3)
    time.sleep(t)
    print("file loaded..")
    print("                                       Game Powerd by AKELA                                    ")
    print("                                       Owner name Ankit                                        \n\n\n")
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
        if os.path.isfile("data.txt"):#it see file exiest or not
            f=open("data.txt",mode="r")
            fd=f.read()
            print(f"money you have now is {fd}")
            f.close()
            trading_money=int(input("Deposit your money:-"))
            file_money=int(fd)
            remaind_money=file_money-trading_money
            print(f"money now you have= {remaind_money}")
            f=open("data.txt",mode="w")
            update_file_data=f.write(f"{remaind_money}")
            f.close()
        else:
            f=open("data.txt",mode="w")
            insert_money=f.write("500")
            f=open("data.txt",mode="r")
            fd=f.read()
            print(f"money you have now is {fd}")
            f.close()
            trading_money=int(input("Deposit your money:-"))
            file_money=int(fd)
            remaind_money=file_money-trading_money
            print(f"money now you have= {remaind_money}")
            f=open("data.txt",mode="w")
            update_file_data=f.write(f"{remaind_money}")
            f.close()
            
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
                    for i in range(10):
                        rc=random.choice(["9","a","b","c","d"])
                        os.system(f"color {rc}f")
                        time.sleep(.6)
                        os.system("color 0f")


                else:
                    print("???you loos and opponent win???")
                    for i in range(5):
                        rrc=random.choice(["4","c"])
                        os.system(f"color {rrc}f")
                        os.system("color 0f")
                        os.system(f"color {rrc}f")
                        os.system("color 0f")
                        time.sleep(.8)

            elif grc=="D":
                if a<12:
                    print("(((you win and opponent loos)))")
                    for i in range(10):
                        rc=random.choice(["9","a","b","c","d"])
                        os.system(f"color {rc}f")
                        time.sleep(.6)
                        os.system("color 0f")
                else:
                    print("???you loos and opponent win???")
                    for i in range(5):
                        os.system("color cf")
                        os.system("color 0f")
                        os.system("color cf")
                        os.system("color 0f")
                        time.sleep(.8)
                    

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
                    for i in range(10):
                        rc=random.choice(["9","a","b","c","d"])
                        os.system(f"color {rc}f")
                        time.sleep(.6)
                        os.system("color 0f")
                else:
                    print("???you loos and opponent win???")
                    for i in range(5):
                        os.system("color cf")
                        os.system("color 0f")
                        os.system("color cf")
                        os.system("color 0f")
                        time.sleep(.8)
            elif pre=="D":
                if a<12:
                    print("(((you win and opponent loos)))")
                    for i in range(10):
                        rc=random.choice(["9","a","b","c","d"])
                        os.system(f"color {rc}f")
                        time.sleep(.6)
                        os.system("color 0f")
                else:
                    print("???you loos and opponent win???")
                    for i in range(5):
                        os.system("color cf")
                        os.system("color 0f")
                        os.system("color cf")
                        os.system("color 0f")
                        time.sleep(.8)

    
    elif r==2:
        print(tnc)

    else:
        break
print("                                                                         ....Thank you for palying....")        
            
                        
                 
                         
        
        
        
        

        
        
        
        
