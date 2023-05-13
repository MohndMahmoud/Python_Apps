# this project is implemintation or calculator  
#8/5/2023

#take operaation Mode
m='''choose one of  the provided Mode plz  
      1- Seintific Mode   
      2- Programming  Mode
     '''
os='''choose one of  the provided operation plz  
      1- ADD  (+)  
      2- Sup  (-)
      3- Mult (*)   
      4- Div  (/)
     '''
op='''choose one of  the provided operation plz  
      1- AND         (&)  
      2- OR          (|)
      3- SHIFT left  (<<)   
      4- SHIFT RIGHT (>>)
      
     '''
#create fun for operation in calculator
def Sum_AND(Mode,op1,op2):
    if Mode=='1':
        return op1+op2
    elif Mode =='2':
        return op1 & op2
def Sup_OR(Mode,op1,op2):
    if Mode=='1':
        return op1-op2
    elif Mode =='2':
        return op1 | op2
def MULT_SHIFTLift(Mode,op1,op2):
    if Mode=='1':
        return op1*op2
    elif Mode =='2':
        return op1 << op2
def DIV_SHIFTRight(Mode,op1,op2):
    if Mode=='1':
        return op1/op2
    elif Mode =='2':
        return op1 >> op2  

sysrun="R" 
while sysrun== 'R':       
    Mode=input(m)
#Do operation in scientific Mode
    if Mode =="1":
        s=os
    elif Mode =='2':
        s=op

# repeate operations
    re='y'
    while re == 'y':
        Operation=input(s)
        op1=int(input("plz enter op1    "))
        op2=int(input("plz enter op2    "))
        if Operation == '1':
            res=Sum_AND(Mode,op1,op2)
            print(res)
            re=input("for More Operation press Y or N for Mode menu   ")
        elif Operation == '2':
            res=Sup_OR(Mode,op1,op2)
            print(res)
            re=input("for More Operation press y or N for Mode menu   ")
        elif Operation == '3':
            res=MULT_SHIFTLift(Mode,op1,op2)
            print(res)
            re=input("for More Operation press y or N for Mode menu   ")
        elif Operation == '4':
            res=DIV_SHIFTRight(Mode,op1,op2)
            print(res)
            re=input("for More Operation press y or N for Mode menu    ")
    sysrun=input("For Mode menu press R /for exit press any button     ")
        