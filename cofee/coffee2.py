print("Write how many ml of water the coffee machine has:")
water = input()
print("Write how many ml of milk the coffee machine has:")
milk = input()
print("Write how many grams of coffee beans the coffee machine has:")
beans = input()
print("Write how many cups of coffee you will need:")
cups = input()
can = (int(int(water)/200 >= int(cups)) and (int(int(milk)/50) >= int(cups)) and (int(int(beans)/15) >= int(cups)))
if can:
    
    minCups = min(int(int(water)/200),int(int(milk)/50),int(int(beans)/15))
    if(minCups > int(cups)):
        more = minCups - int(cups)
        print(f"Yes, I can make that amount of coffee (and even {more} more than that)")
    else:
        print("Yes, I can make that amount of coffee")
else:
    minCups = (int(int(water)/200))
    if minCups > int(int(milk)/50):
        minCups = int(int(milk)/50)
    if minCups > int(int(beans)/15):
        minCups = int(int(beans)/15)
    print(f'No, I can make only {minCups} cups of coffee')