# this project to print pattern arrow 
import time
import os
s='''                                                                                                                                       











                                                                                                                                                                          '''
def arrow1():
    # Number of Rows
    n=8
# start of my implem
    for i in range(n-1):
        if i<3 :
            print("\t\t   ", end = "")
            for j in range(3-i):
                print(" ", end = "  ")
            print("*")
        elif i==3 :
            print("\t\t   ", end = "")
            for i in range(n):
                print("* ", end = " ")
            print()
        else :
            print("\t\t   ", end = "")
            for j in range(i-3):
                print(" ", end = "  ")
            print("*")
  
def arrow2():
    # Number of Rows
    n=8
# start of my implem
    for i in range(n-1):
        if i<3 :
            print("\t\t\t\t\t   ", end = "")
            for j in range(i+4):
                print(" ", end = "  ")
            print("*")
        elif i==3 :
            print("\t\t\t\t\t   ", end = "")
            for i in range(n):
                print("* ", end = " ")
            print()
        else :
            print("\t\t\t\t\t   ", end = "")
            for j in range(n-i+2):
                print(" ", end = "  ")
            print("*")


def arrow3():
    # Number of Rows
    n = 12
    
    for i in range(n - 1):
        if i == 0 :
            print("\t\t\t\t   ", end = "")
            print("      *", end = "")
        elif (i < 7):
            print("\t\t\t\t   ",end = "")
            for j in range(n):
                
                if  i == 2 and ((j == 4) or (j == 6) or (j == 8)):
                   
                    print("*", end = "")
                elif i == 4 and ((j == 2) or (j == 6) or (j == 10)):
                    
                    print("*", end = "")
                elif i == 6 and ((j == 0) or (j == 6) or (j == 11)):
                   
                    print("*", end = "")
                else:
                    
                    print(" ", end = '')	
        elif i > 7:
            print("\t\t\t\t   ", end = "")
            print("      *", end = "\n")
        print("")
        
def arrow4():
    # Number of Rows
    n = 12
    
    for i in range(n):
        if i == 11 :
            print()
            print("\t\t\t\t\t *", end = "")
        elif i < 5:
            print("\t\t\t\t   ", end = "")
            if i % 2 == 0:
                print("      *", end = "")
            else:
                print(" ", end = '')
        elif (i > 5):
            print("\t\t\t\t   ", end = "")
            for j in range(n):
                if   i == 6 and ((j == 0) or (j == 6) or (j == 11)):
                    print("*", end = "")
                elif i == 8 and ((j == 2) or (j == 6) or (j == 10)):
                    print("*", end = "")
                elif i == 10 and ((j == 4) or (j == 6) or (j == 8)):
                    print("*", end = "")
                else:
                    print(" ", end = '')	
        print("")
		
#while True:
ss=input("enter 1 for cw /2 fow acw")
if ss=='1':
    while True:
        print()
        print()
        arrow3()
        time.sleep(.1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(s)
        arrow2()
        time.sleep(.1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(s)
        print(s)
        arrow4()
        time.sleep(.1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(s)
   
        arrow1()
        time.sleep(.1)
        os.system('cls' if os.name == 'nt'else'clear')
elif ss=='2':
    while True:
        print()
        print()
        arrow3()
        time.sleep(.1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(s)
        arrow1()
        time.sleep(.1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(s)
        print(s)
        arrow4()
        time.sleep(.1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(s)
   
        arrow2()
        time.sleep(.1)
        os.system('cls' if os.name == 'nt'else'clear')