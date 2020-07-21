print('Write how many cups of coffee you will need:')
cups = input()
print(f'For {cups} cups of coffee you will need:')
water = 200 * int(cups)
milk = 50 * int(cups)
beans = 15 * int(cups)
print(f'''{water} ml of water
{milk} ml of milk
{beans} g of coffee beans''')