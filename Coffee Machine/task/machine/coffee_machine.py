class CoffeeMachine:

    def __init__(self, water_amount, milk_amount, beans_amount, cups_amount, money_amount):
        self.water = water_amount
        self.milk = milk_amount
        self.beans = beans_amount
        self.cups = cups_amount
        self.money = money_amount
        self.state = "Main Action"

    def print_status(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.beans, "of coffee beans")
        print(self.cups, "of disposable cups")
        print("${0} of money".format(self.money))
        self.state = "Main Action"
        return

    def choose_coffee(self):
        self.state = "Choose Coffee"

    def buy_coffee(self, coffee_type):
        self.state = "Main Action"  # After action no matter what we will be back to main action
        if coffee_type == "1":
            water_needed = 250
            milk_needed = 0
            beans_needed = 16
            cups_needed = 1
            cost = 4
        elif coffee_type == "2":
            water_needed = 350
            milk_needed = 75
            beans_needed = 20
            cups_needed = 1
            cost = 7
        elif coffee_type == "3":
            water_needed = 200
            milk_needed = 100
            beans_needed = 12
            cups_needed = 1
            cost = 6
        elif coffee_type == "back":  # Nothing changes
            return
        else:
            print("Coffee Type not recognized")
            return
        # Test if enough material
        if self.water < water_needed or self.milk < milk_needed or self.beans < beans_needed or self.cups < cups_needed:
            if self.water < water_needed:
                print("Sorry, not enough water!")
            if self.milk < milk_needed:
                print("Sorry, not enough milk!")
            if self.beans < beans_needed:
                print("Sorry, not enough beans!")
            if self.cups < cups_needed:
                print("Sorry, not enough cups!")
            return
        else:
            print("I have enough resources, making you a coffee")
            self.water -= water_needed
            self.milk -= milk_needed
            self.beans -= beans_needed
            self.cups -= 1
            self.money += cost
            return

    def main_action(self, command):
        if command == "buy":
            self.state = "Choose Coffee"
        elif command == "fill":
            self.state = "Fill Water"
        elif command == "take":
            self.take_money()
        elif command == "remaining":
            self.print_status()
        elif command == "exit":
            return
        else:
            print("Command not recognized")

    def fill_machine(self, amount):
        fill_options = {
            "Fill Water" : self.fill_water,
            "Fill Milk" : self.fill_milk,
            "Fill Beans" : self.fill_beans,
            "Fill Cups" : self.fill_cups,
        }
        fill_options[self.state](amount)
        
    def fill_water(self, amount):
        self.water += amount
        self.state = "Fill Milk"

    def fill_milk(self, amount):
        self.milk += amount
        self.state = "Fill Beans"

    def fill_beans(self, amount):
        self.beans += amount
        self.state = "Fill Cups"

    def fill_cups(self, amount):
        self.cups += amount
        self.state = "Main Action"

    def take_money(self):
        print("I gave you ${0}".format(self.money))
        self.money = 0
        self.state = "Main Action"
        return

    def text_to_display(self):
        switcher = {
            "Main Action": "Write action (buy, fill, take, remaining, exit):",
            "Fill Water": "Write how many ml of water do you want to add: ",
            "Fill Milk": "Write how many ml of milk do you want to add: ",
            "Fill Beans": "Write how many grams of coffee beans do you want to add: ",
            "Fill Cups": "Write how many disposable cups of coffee do you want to add: ",
            "Choose Coffee": "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:"
        }
        return switcher.get(self.state, "Invalid State")

    def do_action(self, input_string):
        if self.state == "Main Action":
            self.main_action(input_string)
        elif self.state in ["Fill Water", "Fill Milk", "Fill Beans", "Fill Cups"]:
            self.fill_machine(int(input_string))
        elif self.state == "Choose Coffee":
            self.buy_coffee(input_string)


# def print_ingredients():
#     # Write your code here
#     number = int(input())
#     print("""For {0} cups of coffee you will need:
#     {1} ml of water
#     {2} ml of milk
#     {3} g of coffee beans""".format(number, 200 * number, 50 * number, 15 * number))


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
# money = 550
# water = 400  # int(input("Write how many ml of water the coffee machine has:"))
# milk = 540  # int(input("Write how many ml of milk the coffee machine has:"))
# beans = 120  # int(input("Write how many grams of coffee beans the coffee machine has:"))
# cups = 9  # int(input("Write how many cups of coffee you will need:"))

# print_status(water, milk, beans, cups, money)

while True:
    user_input = input(coffee_machine.text_to_display())
    if user_input == "exit":
        break
    print()
    coffee_machine.do_action(user_input)
    if coffee_machine.state == "Main Action":
        print()
    continue  # End of loop

# print()
# print_status(water, milk, beans, cups, money)

# possible_cups = min(water // 200, milk // 50, beans // 15)
#
# if cups == possible_cups:
#     print("Yes, I can make that amount of coffee")
# elif cups < possible_cups:
#     print("Yes, I can make that amount of coffee (and even {0} more than that)".format(possible_cups - cups))
# else:
#     print("No, I can make only {0} cups of coffee".format(possible_cups))
