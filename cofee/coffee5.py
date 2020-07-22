
def printMessage(water,milk,beans,cups,money):
    print(f'''The coffee machine has:
    {water} of water
    {milk} of milk
    {beans} of coffee beans
    {cups} of disposable cups
    {money} of money''')

def buyAction(water,milk,beans,cups,money):
    buyItem = input()
    if(buyItem == '3'):
        water -= 200
        milk -= 100
        beans -= 12
        cups -= 1
        money += 6
    elif buyItem == '2':
        water -= 350
        milk -= 75
        beans -= 20
        cups -= 1
        money += 7
    elif buyItem == '1':
        water -= 250
        beans -= 16
        cups -= 1
        money += 4
    printMessage(water,milk,beans,cups,money)

def take(water,milk,beans,cups,money):
    print(f'I gave you ${money}')
    money = 0
    printMessage(water,milk,beans,cups,money)

def fillAction(water,milk,beans,cups,money):
    print("Write how many ml of water do you want to add:")
    water += int(input())
    print("Write how many ml of milk do you want to add:")
    milk += int(input())
    print("Write how many grams of coffee beans do you want to add:")
    beans += int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    cups += int(input())
    printMessage(water,milk,beans,cups,money)

def main():
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550
    printMessage(water,milk,beans,cups,money)
    print('Write action (buy, fill, take):')
    action = input()
    if(action == 'buy'):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        buyAction(water,milk,beans,cups,money)
    elif(action == 'fill'):
        fillAction(water,milk,beans,cups,money)
    elif(action == 'take'):
        take(water,milk,beans,cups,money)

main()