import random
from enum import Enum
from typing import List

def seed(seed_value):
    """
    A decorator that sets the random seed for a function.
    Args:
        seed_value: Value to use as the random seed.
    Returns:
        The decorated function with a set random seed.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            random.seed(seed_value)
            return func(*args, **kwargs)
        return wrapper
    return decorator


class DiceType(Enum):
    """
    Enum representing different types of dice with their corresponding number of faces.
    """
    D4 = 4
    D6 = 6
    D8 = 8
    D12 = 12
    D20 = 20

    class Side(Enum):
        One = 1

    def __eq__(self, other):
        """
        Check if two dice types are equal.

        Args:
            other: Another DiceType object to compare with.

        Returns:
            bool: True if the dice types have the same number of faces, False otherwise.
        """
        if not isinstance(other, DiceType):
            return False
        return self.value == other.value

    # not > --> <=
    def __lt__(self, other):
        """
        Check if this dice type has fewer faces than another.

        Args:
            other: Another DiceType object to compare with.

        Returns:
            bool: True if this dice has fewer faces than the other, False otherwise.
        """
        if not isinstance(other, DiceType):
            raise TypeError("Can only compare DiceType with another DiceType")
        return self.value < other.value

    def __gt__(self, other):
        """
        Check if this dice type has more faces than another.

        Args:
            other: Another DiceType object to compare with.

        Returns:
            bool: True if this dice has more faces than the other, False otherwise.
        """
        if not isinstance(other, DiceType):
            raise TypeError("Can only compare DiceType with another DiceType")
        return self.value > other.value

DiceType.D4.Side.One

class Dice:
    """
    Class representing a dice with a specific type and current value.
    """

    def __init__(self, dice_type: DiceType):
        """
        Initialize a new dice with the specified type and roll it to get an initial value.

        Args:
            dice_type: The type of dice (D4, D6, D8, D12, D20).
        """
        self._type = dice_type
        self.roll()  # Roll to get an initial value

    def get_type(self) -> DiceType:
        """
        Get the type of this dice.

        Returns:
            DiceType: The type of this dice.
        """
        return self._type

    def get_value(self) -> int:
        """
        Get the current value shown on the dice.

        Returns:
            int: The current value of the dice.
        """
        return self._value

    @seed(42)  # Using a fixed seed for predictable testing
    def roll(self) -> int:
        """
        Roll the dice to get a new random value.

        Returns:
            int: The new value of the dice after rolling.
        """
        self._value = random.randint(1, self._type.value)
        return self._value

    def __eq__(self, other) -> bool:
        """
        Check if this dice shows the same value as another dice.

        Args:
            other: Another dice object to compare with.

        Returns:
            bool: True if both dice show the same value, False otherwise.
        """
        if not isinstance(other, Dice):
            return False
        return self._value == other.get_value()

    def __lt__(self, other) -> bool:
        """
        Check if this dice shows a lower value than another dice.

        Args:
            other: Another dice object to compare with.

        Returns:
            bool: True if this dice shows a lower value than the other, False otherwise.
        """
        if not isinstance(other, Dice):
            raise TypeError("Can only compare a Dice with another Dice")
        return self._value < other.get_value()

    def __gt__(self, other) -> bool:
        """
        Check if this dice shows a higher value than another dice.

        Args:
            other: Another dice object to compare with.

        Returns:
            bool: True if this dice shows a higher value than the other, False otherwise.
        """
        if not isinstance(other, Dice):
            raise TypeError("Can only compare a Dice with another Dice")
        return self._value > other.get_value()

    def __hash__(self) -> int:
        """
        Get a hash code for this dice based on its current value.

        Returns:
            int: Hash code based on the current value.
        """
        return hash(self._value)

    def __getitem__(self, times: int) -> List[int]:
        """
        Roll the dice a specified number of times and return the results.

        Args:
            times: Number of times to roll the dice.

        Returns:
            List[int]: List of values obtained from rolling the dice.
        """
        if not isinstance(times, int) or times <= 0:
            raise ValueError("Number of rolls must be a positive integer")

        return [self.roll() for _ in range(times)]

d4 = Dice (DiceType.D4)
print(d4)
print(hex(id(d4)).upper())


