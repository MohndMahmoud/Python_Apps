#this project for Kepda shop : 5/9/2023
import time
import os
ownerdata=("Mohnd",0000)
# string for welcome user
S='''                                              Welcome   to Kepdtna                                            '''
#string for main menu
Mode='''Main Menu   :
        1-Owner
        2-Customer'''
#string for customer 
Menu='''Customer Menu :
        1-List Product
        2-Select Product 
        3-Print Bill'''
#string for owner
Ownermenu='''Owner menu : choose one PLZ
        1- add product
        2-show product
        3-change cost      '''
Product_list={'Kepda':50,'HotDog':50,'sogo2':50,'Kofta':50}        
   
print(S)
time.sleep(2)
while 1 :
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Mode)
    M=input("PLZ ENTER UR MODE   ")
    if M=='1':
        user=input("PLZ ENTER UR USER NAME   ")
        pas=int(input("PLZ ENTER UR PASSWORD   "))
        if (user ==ownerdata[0]) and (pas==ownerdata[1]):
            x=1
            print("WELCOME SIR : amoment for ur options PLZ ")
            while x==1:
                
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(Ownermenu)
        #let the user choose an option
                OOP=input("press x for Exit  ")
                if OOP=='1':
                    print("product list :")
                    print(Product_list)
                    # take th e new product and quantity
                    prd=input("Enter the New Product or x for go back to the main menu   ")
                    if prd!="x":
                        cost=int(input("PLZ ENTER THE NEW PRODUCT COST   "))
                        Product_list[prd]=cost
                    else :
                        x=0
                elif OOP=='2':
                    print(Product_list)
                    time.sleep(5)
                elif OOP=='3':
                    print("product list :  ")
                    print(Product_list)
                    # take th e new product and new cost
                    prd=input("Enter the New Product or x for go back to the owner menu    ")
                    if prd in Product_list:
                        cost=int(input("PLZ ENTER THE NEW  COST    "))
                        Product_list[prd]=cost
                    else :
                        print("the product is not exist ADD it first ")
                elif OOP=='x':
                    x=0
                
    elif M=="2":
        cart={}
        list=[]
        a=1
        print("WELCOME SIR : amoment for ur options PLZ ")
        while a==1:
                
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(Menu)
            #let the user choose an option
                OOP=input("press x for Exit  ")
                if OOP=='1':
                    print("product list :")
                    print(Product_list)
                    time.sleep(10)
                elif OOP=='2':
                    z=1
                    while z==1:
                    
                        prd=input("Enter ur choice or x for exit choice menu   ")
                        if prd in Product_list:
                            cost=int(input("PLZ ENTER amount U Want   "))
                            cart[prd]=cost
                            list.append(prd)
                        elif prd =='x':
                            z=0
                elif OOP=='3':
                    i=len(list)
                    ii=range(i)
                    bill=0
                    for q in ii:
                        bill+=cart[list[q]]*Product_list[list[q]]
                    print ("ur bill  is  : %d LE ",bill)
                    print ("THANK U FOR Visiting US Sir")
                    time.sleep(5)
                    a=0
                elif OOP=='x':
                    a=0       

    