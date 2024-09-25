import cashier 
import sandwich_maker
import data

recipes = data.recipes
resources = data.resources

sandwich_maker = sandwich_maker.SandwichMaker(resources)
cashier = cashier.Cashier()

### Takes user input with prompt ###
while True:
    choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

    if choice == "off":
        print("Turning off the machine. Goodbye!")
        break
    elif choice == "report":
        print(f"Bread: {sandwich_maker.machine_resources['bread']} slice(s)")
        print(f"Ham: {sandwich_maker.machine_resources['ham']} slice(s)")
        print(f"Cheese: {sandwich_maker.machine_resources['cheese']} ounce(s)")
    elif choice in recipes:
        sandwich = recipes[choice]
        if sandwich_maker.check_resources(sandwich["ingredients"]):
            coins_inserted = cashier.process_coins()
            if cashier.transaction_result(coins_inserted, sandwich["cost"]):
                sandwich_maker.make_sandwich(choice, sandwich["ingredients"])
    else:
        print("Invalid option. Please try again.")

p