class Product:
    """
    A class called Product representing a product in inventory system 
    attributes:
    name(str): name of the product 
    price(float): price of the product per unit and should be greater than 0
    quantity(int): quantity of the product and should be greater than 0
   
    """
    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialize the Product object with name, price, and quantity.
        attributes:
        name (str): The name of the product.
        price (float): The price of the product per unit. Must be greater than 0.
        quantity (int): The quantity of the product. Must be greater than 0.
        Raises:
        ValueError: If price or quantity is less than or equal to 0.
        Example:
        product = Product("Hair drier", 10000.0, 2)
        product = Product("Hair drier", -10000.0, 2) raises ValueError
        """
        self.name = name
        self.price = price
        self.quantity = quantity

        if price <= 0:
            raise ValueError("Price cannot be negative.")
        if quantity <= 0:
            raise ValueError("Quantity cannot be negative.")
    def adding_inventory(self, amount: int):
        """
        Adds to the product inventory.

        Args:
            amount (int): Number of items to add. Must be > 0.

        Raises:
            ValueError: If amount is negative.
        """
        if amount < 0:
            raise ValueError("Cannot add negative amount to inventory.")
        else:
            self.quantity += amount
    def removing_inventory(self, amount: int):
        """
        Removes from the product inventory.

        Args:
            amount (int): Number of items to remove. Must be > 0.

        Raises:
            ValueError: If amount is negative or exceeds available quantity.
        """
        if amount < 0:
            raise ValueError("Cannot remove negative amount from inventory.")
        elif amount > self.quantity:
            raise ValueError("Cannot remove more than available quantity.")
        else:
            self.quantity -= amount
    def total_value_inventory(self) -> float:
        """
        Calculates total inventory value.

        Returns:
            float: Total value (price × quantity).
        """
        return self.price * self.quantity

    def display_product_info(self):
        """
        Displays product information.
        """
        print(f"Product: {self.name}")
        print(f"Price: rwf{self.price:.2f}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Value in stock : rwf{self.total_value_inventory():.2f}")
def main():
    try:
    # Get product details from user
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter the quantity: "))
        
        product = Product(name, price, quantity)
        print("\nProduct created successfully!\n")
        product.display_product_info()
        
            
        while True:
            print("\nOptions:")
            print("1. Add to inventory")
            print("2. Remove from inventory")
            print("3. Display product info")
            
        
            choice = input("Enter your choice: ")
        
            if choice == "1":
                amount = int(input("Enter amount to add: "))
                product.adding_inventory(amount)
                print(f"Added {amount} units to inventory.")
        
            elif choice == "2":
                amount = int(input("Enter amount to remove: "))
                product.removing_inventory(amount)
                print(f"Removed {amount} units from inventory.")
        
            elif choice == "3":
                product.display_product_info()
                break
        
            else:
                print("Invalid choice. Please try again.")
            
        
               
    except ValueError as e:
        print(f"InputError: {e}")
    except ZeroDivisionError as se:
        print(f"Invalid value Error: {se}")

        
main()
        