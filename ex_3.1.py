def space():
    print('*'*20)
space()
print('Zadanie 1')
space()
shopping = {
    'warzywniak' : ['seler','marchew', 'rukola'],
    'piekarnia' : ['chleb','bułka', 'pączek']
}
x = 0
for shop, items in shopping.items():
    for item in items:
        print(f"Idę do {shop.capitalize()} i kupuję {item.capitalize()}")
        x += 1
print(f"W sumie kupiłem {x} produktów")
space()
print('Zadanie 2')
space()

divided_by_5 = []
their_power_of_3 = []
for number in range(0, 101):
    if number % 5 == 0:
        divided_by_5.append(number)
        power_3 = number**3
        their_power_of_3.append(power_3)
print(divided_by_5)
print(their_power_of_3)
