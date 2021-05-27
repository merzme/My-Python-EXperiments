"""
1.get the number of unit consumed
2.calculate the bill amount
3.add 100 as meter rent
4.subtract 3% as discount
5.add 18% as GST
6.display bill
LOGIC:
c
0-100  = 100
101-200 = 100
201-350 = 150
351-400 = 30


N=380
(100*.20)+(100*.35)+(150*.50)+(30*.75)
         ****************
N=220
(100*.20)+(100*0.35)+(20*.50)
        ****************
N=120
(100*.20)+(20*.35)
        ****************
N=250
(100*.20)+(100*.35)+(50*.50)
"""
def main():
    unit = float(input("enter unit"))
    amount = 0
    if(unit <= 100):
        amount = unit * .20
    elif(unit <= 200):
        #120=100*.20 + 20*.35
        amount = (100 * .20) + (unit - 100 ) * .35
    elif(unit <= 350):
        #250=100*.20+100*.35+50*.50
        amount =  (100 * .20) + (200 - 100) * .35 + (unit - 200 ) * .50
    elif(unit <= 400):
        amount = (100 * .20) + (200 - 100) * .35 + (350 - 200) * .50 + (unit - 350 ) * .75
    elif(unit <= 500):
        amount = (100 * .20) + (200 - 100) * .35 + (350 - 200) * .50 + (400 - 350) * .75 + (unit - 400 ) * 1
    else:
        amount = (100 * .20) + (200 - 100) * .35 + (350 - 200) * .50 + (400 - 350) * .75 + (500 - 400) * 1 + (unit - 500 ) * 1.25

    print('bill amount', amount)

    metercharge = amount + 100
    print('meter charge is',metercharge)

    discount = metercharge - metercharge * .03
    print('discount is', discount)

    GST =  discount + (discount * .18)
    print('GST',GST)

    total_amount = GST
    print('Net total amount is',total_amount)

if __name__ == "__main__":

    main()





