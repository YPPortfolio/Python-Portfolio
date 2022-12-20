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

def coffee_machine():

    def machine_status():
        """Turning the coffee machine off if the coffee selection input is 'off'"""
        machine_on = True
        if coffee_selection == "off":
            machine_on = False
            print("The coffee machine has been turned off.")
            exit()


    def resources_report():
        """function to print report"""
        for key in resources:
            if key in ("water", "milk"):
                measurement = "ml"
                print(key + ": " + str(resources[key]) + measurement)
            elif key in "coffee":
                measurement = "g"
                print(key + ": " + str(resources[key]) + measurement)
            elif key in "profit":
                measurement = "$"
                print(key + ": " + measurement + str(resources[key]))


    def check_resource():
        """function to check if there are sufficient resources to make the output"""
        resource_required = MENU[coffee_selection]["ingredients"]
        missing_resources = []
        for resource in resource_required:
            if resource_required[resource] - resources[resource] > 0:
                missing_resources.append(resource)
        if len(missing_resources) > 0:
            print(f"There is insufficient {missing_resources}.")
            coffee_machine()


    def accept_payment():
        coins = {"quarter": .25,
                 "dime": .1,
                 "nickel": .05,
                 "penny": .01,
                 }
        payment = []
        for coin in coins:
            payment.append(coins[coin] * float(input(f"How many {coin}? ")))
        return payment


    def compare():
        remaining_cost = round(cost - total_payment, 2)
        change = round(total_payment - cost, 2)
        if total_payment < cost:
            print(f"Sorry that's not enough money, your remaining cost is {remaining_cost}. Money refuned.")
            coffee_machine()
        elif total_payment > cost:
            print(f"Your change is {change}.")
            print(f"Here is your {coffee_selection}. Enjoy!")
        else:
            print(f"Here is your {coffee_selection}. Enjoy!")


    def reduce_resource():
        resource_required = MENU[coffee_selection]["ingredients"]
        for resource in resource_required:
            resources[resource] = resources[resource] - resource_required[resource]

    def process_transaction():
        transactions = []
        transactions.append(total_payment)
        resources["profit"] += sum(transactions)

    resources.update({"profit": 0})
    continue_purchase = True
    while continue_purchase:


        ### Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
        coffee_selection = input("What would you like? (espresso/latte/cappuccino):\n").lower()


        ### Turning the coffee machine off if the coffee selection input is "off"
        machine_status()


        ### Printing the current remaining resources when the coffee_selection input is "report"
        if coffee_selection == "report":
            resources_report()
            coffee_machine()


        if coffee_selection not in MENU:
            print("Selection not found. Please select again.")
            coffee_machine()

        ### function to check if there are sufficient resources for the selected coffee
        check_resource()


        ### if sufficient resources, accept payment
        cost = MENU[coffee_selection]["cost"]
        print(f"Your cost is {cost}.")


        payment = accept_payment()
        total_payment = sum(payment)


        ### compare payment against cost
        compare()


        ### processing successful transaction and recording the profits in the 'resources' dictionary
        process_transaction()

        ### reduce remaining resources after a successful transaction
        reduce_resource()

### coffee_machine program
coffee_machine()
