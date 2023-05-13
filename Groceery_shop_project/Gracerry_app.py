#create Dictionary to define the avilable grocerry
grocerry={'orange':20,'Apple':35,'chees':15,'pasta':13,'Milk':50,'eggs':60}
#create price refrance to helping us to use list
Pref={'orange':0,'Apple':1,'chees':2,'pasta':3,'Milk':4,'eggs':5}
#create list to define the price of grocerry
prices=[10,30,30,9,25,5]
cart={'orange':0,'Apple':0,'chees':0,'pasta':0,'Milk':0,'eggs':0}
carttuple=('orange','Apple','chees','pasta','Milk','eggs')
cost=0
#take order from user 
ask='take'
while ask!='done' :
    ask=input('enter ur Grocerry u want to add to cart  ')
    if ask!= 'done'  :
        amount=int(input('enter amount of this kind   '))
        # cheak if the we have enough from the asked kind
    if ask in grocerry and grocerry[ask] != 0 and grocerry[ask]>=cart[ask] :
        cart[ask]+=amount
        cost+=(amount*prices[Pref.get(ask)])
        grocerry[ask]-=cart[ask]
    elif ask == 'done' :
        print('thank u wait amoments for ur bill  ')
    else :
        print('kind not exist  ')
i=range(0,6)
for n in i:
    if cart[carttuple[n]]==0:
        cart.pop(carttuple[n])

print('the remaining amount of grocerry is =  ',grocerry)
print('the orderd amount of grocerry is =  ',cart)
print('the total cost of  grocerry =  ',cost)        