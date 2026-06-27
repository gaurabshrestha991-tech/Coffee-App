class CoffeeApp:
    def _init_(self):
        self.menu = {
            "Espresso": 2.50,
            "Latte": 3.50,
            "Cappuccino": 3.75,
            "Americano": 3.00,
            "Mocha": 4.00
        }
        self.order = []

    def display_menu(self):
        print("\n-------Coffee Menu-------")
        i = 1
        for item, price in self.menu.item():
            print(f"{i}. {item} - ${price:.2f}")
            i += 1

    def add_to_order(self):
        self.display_menu()

        try:
            choice = int(inout("Enter coffee number: "))

            if choice >= 1 and choice <= len(self.menu):
                item = list(self.menu.keys())[choice - 1]
                self.order.append(item)
                print(item, "added to your order.")
            else:
                print("Invalid Choice.")

        except ValueError:
            print("Please enter a number.")
    
    def view_order(self):
        if len(self.order) == 0:
            print("\nYour order is empty.")
            return False

        print("\n-------Your Oreder------")
        total = 0

        for items in self.order:
            print(item, "-$", self.menu[item])
            total += self.menu[item]

        print("Total = $",total)
        return True

class CoffeeApp: # Creates a new class called coffee app.It will hold the coffee shop's menu and orders
    def __init__(self): # This tries to define the initializer (the method that runs when we create a new CoffeeApp object).
        self.menu = {
            "Espresso": 2.50,
            "Latte": 3.50,
            "Cappuccino": 3.75,
            "Americano": 3.00,
            "Mocha": 4.00
        }
        self.order = [] # Creates an empty list called order where selected coffee names will be stored.

    def display_menu(self):
        print("\n-------Coffee Menu-------")
        i = 1
        for item, price in self.menu.items():
            print(f"{i}. {item} - ${price:.2f}")
            i += 1

    def add_to_order(self):
        self.display_menu()

        try:
            choice = int(input("Enter coffee number: "))

            if choice >= 1 and choice <= len(self.menu):
                item = list(self.menu.keys())[choice - 1]
                self.order.append(item)
                print(item, "added to your order.")
            else:
                print("Invalid Choice.")

        except ValueError:
            print("Please enter a number.")
    
    def view_order(self):
        if len(self.order) == 0:
            print("\nYour order is empty.")
            return False

        print("\n-------Your Order------")
        total = 0

        for item in self.order:
            print(item, "-$", self.menu[item])
            total += self.menu[item]

        print("Total = $",total)
        return True

    def checkout(self):
        if self.view_order():
            choice = input("Confirm order? (yes/no): ").lower()

            if choice == "yes":
                print("Thnak you! Your coffee is being prepared.")
                self.order.clear()
                return True
            else:
                print("Checkout cancelled.")

        return False

    def run(self):
        while True:
            print("\n====== Coffee App ======")
            print("1. Add Coffee")
            print("2. View Order")
            print("3. Checkout")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_to_order()
            elif choice == "2":
                self.view_order()
            elif choice == "3":
                self.checkout()
            elif choice == "4":
                print("Thank You for visiting😊")
                break
            else:
                print("Invalid Choice.")

app = CoffeeApp()
app.run()
