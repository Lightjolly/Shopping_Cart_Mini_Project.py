shopping_list = []
print("Hi, Welcome to Jolly's Market.")
while True:
	customer = input("Press[1] to add to cart. Press[r] to remove an item. Press [s] to see shopping list. To leave press [2].\n")


	if customer == "1":
		shopping_list.append(input("Add to cart: "))
		continue

	if customer == "r":
		shopping_list.pop(int(input("Remove item : ")))  #Remove items by index value, starting with 0
		print(shopping_list)
		break	

	if customer == "s":
		print(shopping_list)
		continue
		
			
	if len(shopping_list) == 10:
		print("You have ten items, do you wish to add more? (y, n)")
		customer = input(" ").lower()
			
	if customer == "y":
		shopping_list.append(input("Add to cart: "))
	
	elif customer == "n":
		print("Sending you back to the main menu")
		break 	
					

	elif customer == "2":
		print("Thank you for shopping with Jolly's Market")
		break

	else:
		print("I didn't get that, please try again")

	

