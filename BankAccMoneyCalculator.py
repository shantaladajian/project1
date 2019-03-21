def setupInitMoney():
    while True:
        initialMoney = float(input(" input the initial amount of money you have in our bank="))
        if initialMoney < 0:
            print ("Please try again","\n","You can't input negative numbers")
        else:
            return initialMoney


def setupPercent():
    while True:
        Percent = int(input("Please input the interest rate in the integer form from 0 to 100="))
        if Percent >0 and Percent <100:
            return Percent
        else:
            print ("Please try again","\n","input the number in the integer form in the range of 0 to 100")


def setupYears():
    while True:
        Years = int(input("input the number of years it has been since you put you money in our bank="))
        if Years >1 and Years <20:
            return Years
        else:
            print ("Please try again.","\n"," input the years in an integer form between 0 and 20")


def CalculateTheResultMoney(Money, Percent, Years):
    Percent = (Percent/100) + 1
    while Years>0:
        Money = Money * Percent
        Years = Years-1
    return Money


def main():
    print ("Dear user,","\n","This application is made in order to calculate your balance","\n"," after some years by calculating the interest rate on it.")
    print ("To do so,","\n","We need to have some information from you" ,"\n" " your initial amount of money, the years after which you want to calculate your balance with the interest rate.")
    initMoney = setupInitMoney()
    Percent = setupPercent()
    Years = setupYears()
    result = CalculateTheResultMoney(initMoney, Percent, Years)
    print ("After", Years,"years your initial balance of",initMoney,"\n","with the interest rate of",Percent,"has become your final balance of",result)


main()    
