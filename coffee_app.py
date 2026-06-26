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