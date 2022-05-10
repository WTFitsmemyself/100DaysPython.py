Money = 0

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report(request):
    if request == "report":
        waterMeasure = resources["water"]
        milkMeasure = resources["milk"]
        coffeeMeasure = resources["coffee"]
        moneyMeasure = Money
        print(f"Water: {waterMeasure}ml")
        print(f"Milk: {milkMeasure}ml")
        print(f"Coffee: {coffeeMeasure}g")
        print(f"Money: ${moneyMeasure}")
        Machine()

def MoneyCalculate():
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    
    penniesFinal = pennies * 0.01
    nicklesFinal = nickles * 0.05
    dimesFinal = dimes * 0.10
    quartersFinal = quarters * 0.25
    FinalAmount = penniesFinal + nicklesFinal + dimesFinal + quartersFinal
    return FinalAmount

def IsMoneyEnough(UserOrder, AmountUser):
    MoneyNedded = MENU[UserOrder]["cost"]
    ChangeOfMoney = AmountUser - MoneyNedded  
    if MoneyNedded > AmountUser:
        print(f"Sorry Not enough money to buy {UserOrder}")
        return False
    else:
        print(f"Money you paid is {AmountUser}")
        print(f"Here is your change: {ChangeOfMoney}")
        print(f"Here is your {UserOrder}!")
        return True
        
        
def ResoucesUpdate(UserOrder):
    global Money
    if UserOrder == "espresso":
        WaterOrder = MENU[UserOrder]["ingredients"]["water"]
        CoffeeOrder = MENU[UserOrder]["ingredients"]["coffee"]
    else:
        WaterOrder = MENU[UserOrder]["ingredients"]["water"]
        CoffeeOrder = MENU[UserOrder]["ingredients"]["coffee"]
        MilkOrder = MENU[UserOrder]["ingredients"]["milk"]
    WatterResource = resources["water"]
    MilkResource = resources["milk"]
    CoffeeResource = resources["coffee"]
    if UserOrder == "espresso":
        finalWatter = WatterResource - WaterOrder 
        finalCoffee = CoffeeResource - CoffeeOrder
        resources["coffee"] = finalCoffee
        resources["water"] = finalWatter
        Money += 1.5
    else:
        finalWatter = WatterResource - WaterOrder 
        finalCoffee = CoffeeResource - CoffeeOrder
        finalMilk = MilkResource - MilkOrder
        resources["coffee"] = finalCoffee
        resources["water"] = finalWatter
        resources["milk"] = finalMilk
        if UserOrder == "latte":
            Money += 2.5
        else:
            Money += 3
        
def Machine():       
    UserInput = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if UserInput == "espresso" or UserInput == "latte" or UserInput == "cappuccino" or UserInput == "report":    
        report(UserInput)
        Money_Neded = MoneyCalculate()
        OrderCompelete = IsMoneyEnough(UserInput, Money_Neded)
        if OrderCompelete == True:
            ResoucesUpdate(UserInput)
            Machine()
    else:
        exit(1)

Machine()