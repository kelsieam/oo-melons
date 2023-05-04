"""Classes for melon orders."""

class AbstractMelonOrder:
    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""
       
        base_price = 5

        if self.name.lower() == "christmas":
            base_price == base_price * 1.5
            
        total = (1 + self.tax) * self.qty * base_price
        
        if self.order_type == "international" and self.qty < 10:
            total = total + 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    def __init__(self, species, qty):
        super().__init__(species, qty, "domestic", .08)
        """Initialize melon order attributes."""

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, "international", .17)
        self.country_code = country_code
    def get_country_code(self):
        """Return the country code."""
        return self.country_code
    
class GovernmentMelonOrder(AbstractMelonOrder):
    def __init__(self, species, qty):
        super().__init__(species, qty, "domestic", 0)
        
        self.passed_inspection = False


    def mark_inspection(self, passed):
        if passed == True:
            self.passed_inspection = True

order0 = InternationalMelonOrder("watermelon", 6, "AUS")

order1 = DomesticMelonOrder("melon", 8)

order2 = DomesticMelonOrder("christmas", 10)

order3 = GovernmentMelonOrder("watermelon", 14)




"""
class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species


class Cat(Animal):

    def __init__(self, name):
        super().__init__(name, "cat")
        
"""