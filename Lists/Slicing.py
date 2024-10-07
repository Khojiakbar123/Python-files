pizzas = ['chicken pizza', 'cheese pizza', 'meat pizza', 'peperoni pizza']
friend_pizzas = pizzas[:]


pizzas.append('mixed pizza')
friend_pizzas.append('simple pizza')

print("My favorite pizzas are:\n")
for pizza in pizzas:
	print(pizza)

print()


print("My friend's favorite pizzas are:\n")
for friend in friend_pizzas:
	print(friend)

