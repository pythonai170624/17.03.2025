from abc import ABC, abstractmethod


# Abstract Products
class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass

    @abstractmethod
    def describe(self):
        pass


class Table(ABC):
    @abstractmethod
    def place_item(self, item):
        pass

    @abstractmethod
    def describe(self):
        pass


class Sofa(ABC):
    @abstractmethod
    def lie_on(self):
        pass

    @abstractmethod
    def describe(self):
        pass


# Concrete Products - Expensive Furniture
class ExpensiveChair(Chair):
    def sit_on(self):
        return "Sitting on a luxurious ergonomic chair with premium leather upholstery"

    def describe(self):
        return "An Italian handcrafted chair made of premium mahogany with genuine leather ($1,200)"


class ExpensiveTable(Table):
    def place_item(self, item):
        return f"Placing {item} on a polished marble-top table"

    def describe(self):
        return "A designer marble-top table with gold-plated legs ($3,500)"


class ExpensiveSofa(Sofa):
    def lie_on(self):
        return "Lying on a spacious sectional sofa with memory foam cushions"

    def describe(self):
        return "A custom-made Italian leather sectional sofa with built-in recliners ($5,800)"


# Concrete Products - Garden Furniture
class GardenChair(Chair):
    def sit_on(self):
        return "Sitting on a weather-resistant garden chair"

    def describe(self):
        return "A foldable plastic garden chair with UV protection ($45)"


class GardenTable(Table):
    def place_item(self, item):
        return f"Placing {item} on a sturdy garden table"

    def describe(self):
        return "A round aluminum garden table with parasol hole ($120)"


class GardenSofa(Sofa):
    def lie_on(self):
        return "Lying on a comfortable garden sofa with water-resistant cushions"

    def describe(self):
        return "A rattan-style garden sofa with removable cushions ($350)"


# Abstract Factory
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_table(self) -> Table:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass


# Concrete Factories
class ExpensiveFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ExpensiveChair()

    def create_table(self) -> Table:
        return ExpensiveTable()

    def create_sofa(self) -> Sofa:
        return ExpensiveSofa()


class GardenFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return GardenChair()

    def create_table(self) -> Table:
        return GardenTable()

    def create_sofa(self) -> Sofa:
        return GardenSofa()


# Client code
def furnish_room(factory: FurnitureFactory):
    chair = factory.create_chair()
    table = factory.create_table()
    sofa = factory.create_sofa()

    print("=== Room Furnishing ===")
    print("Chair:", chair.describe())
    print("Table:", table.describe())
    print("Sofa:", sofa.describe())
    print("\nUsing the furniture:")
    print(chair.sit_on())
    print(table.place_item("a coffee cup"))
    print(sofa.lie_on())
    print("========================")


# Usage
if __name__ == "__main__":
    print("Client: Furnishing a luxury living room")
    furnish_room(ExpensiveFurnitureFactory())

    print("\nClient: Furnishing a garden patio")
    furnish_room(GardenFurnitureFactory())