from data import MENU
from data import resources


def check_resources(p):
    order_requirements = MENU[p]["ingredients"]
    print(f"Checking resources for {p}")

    for key in order_requirements:
        if resources[key] - order_requirements[key] < 0:
            print(f"Sorry, not enough {key}")
            return False

    return True


def deduct_resources(p):
    order_requirements = MENU[p]["ingredients"]

    for key in order_requirements:
        resources[key] -= order_requirements[key]


def process_coins():
    quarters = int(input("Enter Number of Quarters: "))
    dimes = int(input("Enter Number of Dimes: "))
    nickels = int(input("Enter Number of Nickels: "))
    pennies = int(input("Enter Number of Pennies: "))

    t = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    print(f"You paid ${t:.2f}")

    return t


def check_transaction(total_submitted, item_cost):
    change_amt = total_submitted - item_cost
    if change_amt > 0:
        print(f"Here is ${change_amt:.2f} change.")
        return True
    elif change_amt == 0:
        print("Thank you for providing exact change.")
        return True
    else:
        print(
            f"Sorry that's not enough money. Refunding {total_submitted:.2f}")
        return False


while True:
    prompt = input("What would you like? (espresso/latte/cappuccino): ")

    if prompt == "off":
        break
    if prompt == "report":
        for k in resources:
            print(f"{k} :", resources[k])
        continue
    if prompt == "reset":
        resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            "money": 0.0,
        }
        continue

    if not check_resources(prompt):
        continue

    cost = MENU[prompt]["cost"]
    print(f"A {prompt} costs ${cost:.2f}")

    total = process_coins()

    if not check_transaction(total, cost):
        continue

    # Update machine track of money
    resources["money"] += cost

    deduct_resources(prompt)

    print(f"Here is your {prompt}, enjoy!")
