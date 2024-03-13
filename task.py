#Sam has been dumped by his girlfriend so he's gone into the local milk 
#bar to drown his sorrows. He has a budget, and there's a choice of three (or more) 
#milkshakes, 
#differently priced. The barman says, "What can I fix you?" and Sam can reply with a 
#number corresponding 
#to the relevant flavour - this list is displayed every iteration. 
#If he enters Q, he quits and leaves; the barman wishes him well in his search for love. 
#If he orders but can't pay he's thrown out.


#budget = input
#shakes = {}

#while true:
  #  print shakes options

  #  Choice

  #  if....q quit

  #  if.... invalid option

  #  price > budget
   # ..... kicked out

  #  budget -= priced

#    print remaining budget


milkshake_menu = {1: {"flavor": "Vanilla", "price": 3.50}, 2: {"flavor": "Chocolate", "price": 4.00}, 3: {"flavor": "Strawberry", "price": 3.75}}

budget = float(input("Sam, what's your budget for milkshakes today? £"))

while True:
    print("\nMilkshake Menu:")
    for key, details in milkshake_menu.items():
        print(f"{key}. {details['flavor']} - £{details['price']}") 

    choice = input("\nWhat can I get you? (Enter a number or Q to quit): ").upper()

    if choice == 'Q':
        print("The barman wishes you well in your search for love. Goodbye!")
        break

    selected_milkshake = milkshake_menu.get(int(choice))

    if not selected_milkshake or selected_milkshake["price"] > budget:
        print("Invalid choice or not enough budget. Please enter a valid number or Q to quit.")
        continue

    print(f"You ordered a {selected_milkshake['flavor']} milkshake and spent £{selected_milkshake['price']}.")
    budget -= selected_milkshake["price"]
    print(f"Remaining budget: £{budget}")

print("Welcome to the Milk Bar, Sam!")


