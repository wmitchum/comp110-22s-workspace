"""Example of a class and object instantiation."""


class Pizza: 
    """Models th eidea of a Pizza."""

    # Attribute definitions
    size: str
    toppings: int
    extra_cheese: bool


    def price(self) -> float:
        """Calculate the price of a Pizza."""
        total: float = 0.0
        if self.size == "large":
            total += 10.0
        else:
            total += 8.0
        total += self.toppings * 0.75
        if self.extra_cheese:
            total += 1.0
        
        return total


a_pizza: Pizza = Pizza()
a_pizza.size = "large"
a_pizza.toppings = 3
a_pizza.extra_cheese = False
print(Pizza)
print(a_pizza)
print(a_pizza.size)
print(a_pizza.price())  # This is a method call