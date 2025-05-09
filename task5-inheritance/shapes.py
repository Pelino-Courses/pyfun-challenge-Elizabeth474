import math

class Shape:
    def __init__(self, name: str):
        self.name = name

    def area(self):
        raise NotImplementedError("Subclasses must implement the area method.")

    def __str__(self):
        return f"{self.name} Shape"

class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"{self.name} with radius = {self.radius:.2f}, area = {self.area():.2f}"

    @classmethod
    def from_diameter(cls, diameter: float):
        return cls(diameter / 2)

class Rectangle(Shape):
    def __init__(self, width: float, length: float):
        super().__init__("Rectangle")
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def __str__(self):
        return f"{self.name} with width {self.width} and height {self.length}, area = {self.area():.2f}"

class Triangle(Shape):
    def __init__(self, base: float, height: float):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"{self.name} with base {self.base} and height {self.height}, area = {self.area():.2f}"

def main():
    while True:
        print("\nChoose a shape to create:")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Triangle (this will stop the program after creation)")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            use_diameter = input("Create circle using diameter? (yes/no): ").lower()
            if use_diameter == "yes":
                diameter = float(input("Enter diameter: "))
                shape = Circle.from_diameter(diameter)
            else:
                radius = float(input("Enter radius: "))
                shape = Circle(radius)
            print(shape)

        elif choice == "2":
            width = float(input("Enter width: "))
            length = float(input("Enter length: "))
            shape = Rectangle(width, length)
            print(shape)

        elif choice == "3":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            shape = Triangle(base, height)
            print(shape)
            break  # Exit after triangle is created and printed

        else:
            print("Invalid choice. Try again.")

# Run the program
main()
1