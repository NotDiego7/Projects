MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "profit": 0,
}


def get_resource_report():
    """Returns a list of the resources, formatted to print on a report."""
    results = []
    for key, value in resources.items():
        if key in ["water", "milk"]:
            formatted_string = f"{key.capitalize()}: {value}ml"
        elif key == "coffee": formatted_string = f"{key.capitalize()}: {value}g"
        elif key == "profit": formatted_string = f"{key.capitalize()}: ${value:.2f}"
        results.append(formatted_string)
    return results


def get_ingredients_and_resources(user_pick_param, resources_param):
    """Returns the ingredients for the user's coffee of choice & the resources available (in a comparable/tuple form)."""
    coffee_ingredients_tuple = list(MENU[user_pick_param]["ingredients"].items())
    resources_tuple = list(resources_param.items())
    coffee_ingredients_dict = MENU[user_pick_param]["ingredients"]
    return coffee_ingredients_tuple, resources_tuple, coffee_ingredients_dict


def enough_resources_check(coffee_ingredients_tuple_param, resources_tuple_param):
    """Checks if there are enough resources, else, print's what resource is depleted."""
    for i in range(3):
        if coffee_ingredients_tuple_param[i] > resources_tuple_param[i]:
            print(f"Sorry, there is not enough {resources_tuple_param[i]}.")
        else:
            sufficient_resources = True
            return sufficient_resources


def coin_count(quarters_param, dimes_param, nickels_param, pennies_param):
    """Does all the math in terms of the coins inserted."""
    quarters_value = 0.25
    dimes_value = 0.10
    nickels_value = 0.05
    pennies_value = 0.01

    total_inserted = (quarters_param * quarters_value) + (dimes_param * dimes_value) + (nickels_param * nickels_value) + (pennies_param * pennies_value) 
    return total_inserted


def profits_and_change(total_inserted_param, user_pick_param):
    """Checks if inserted money is enough for the chosen coffee, and if so, returns change amount and updates profits accordingly"""
    if total_inserted_param < MENU[user_pick_param]["cost"]:
        print("Sorry, that is not enough. Your money has been refunded.")
        #TODO if we get a None, we might need a return here
    elif total_inserted_param >= MENU[user_pick_param]["cost"]:
        user_change_amount = total_inserted_param - MENU[user_pick_param]["cost"]
        profit_amount = total_inserted_param - user_change_amount
        
        #Adding a profit section to resources (first profit instance will add, all others will simply update amount)
        resources.update({"profit": resources["profit"] + profit_amount})

        #Converting change amount to 2 decimal places if needed
        user_change_amount = f"{user_change_amount:.2f}"
    return user_change_amount


def deduct_ingredients_from_resources(coffee_ingredients_dict_param):
    """After purchase is confirmed, deducts the ingredients from resources."""
    for key in coffee_ingredients_dict_param:
        resources[key] -= coffee_ingredients_dict_param[key]




def main_flow():
    """Contains program's principal flow and functionalities."""
    flow_on = True

    while flow_on:
        user_pick = input("What would you like: Espresso, Latte or Cappuccino? ").lower() #TODO Need recursion once coffee is served or money is refunded
        
        if user_pick == "report":
            resource_report = get_resource_report()
            for item in resource_report:
                print(item)
            
        
        elif user_pick == "off":
            flow_on = False
            return
        
        elif user_pick in ["espresso", "latte", "cappuccino"]:
            coffee_ingredients_tuple, resources_tuple, coffee_ingredients_dict = get_ingredients_and_resources(user_pick, resources)

            if enough_resources_check(coffee_ingredients_tuple, resources_tuple) == True:
                print(f"Please go ahead and insert coins.")
                quarters = int(input("How many quarters? "))
                dimes = int(input("How many dimes? "))
                nickels = int(input("How many nickels? "))
                pennies = int(input("How many pennies? "))
                
                total_inserted = coin_count(quarters, dimes, nickels, pennies)
                user_change_amount = profits_and_change(total_inserted, user_pick)
                if float(user_change_amount) > 0:
                    print(f"Here is your change: ${user_change_amount}")

                deduct_ingredients_from_resources(coffee_ingredients_dict)

                print(f"Here is your {user_pick}. Enjoy!")


main_flow()