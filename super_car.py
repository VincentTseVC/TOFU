# Exercise 1 - Car Simulation
# ---------------------------------------------
class CarManager:
    """A class responsible for keeping track of all cars in the system.
    """
    # === Private Attributes ===
    # @type cars: dict[str, Car]
    #     A map of unique string identifiers to the corresponding cars.
    def __init__(self):
        """Create a new CarManager.

        Initially there are no cars in the system.

        @type self: CarManager
        @rtype: None
        """
        self.cars = {}

    def add_car(self, id, fuel):
        """Add a new car to the system.

        The new car is identified by the string <id>, and has initial amount
        of fuel <fuel>.

        Do nothing if there is already a car with the given id.

        @type self: CarManager
        @type id: str
        @type fuel: int
        @rtype: None
        """
        # Check to make sure the identifier isn't already used.
        if id not in self.cars:
            self.cars[id] = Car(id, fuel)

    def move_car(self, id, new_x, new_y):
        """Move a car in the system.

        The car called <id> should be moved to position (<new_x>, <new_y>).

        @type self: CarManager
        @type id: str
        @type new_x: int
        @type new_y: int
        @rtype: None
        """
        if id in self.cars:
            car = self.cars[id]

            (x, y) = car.position

            step = abs(x + new_x) + abs(y + new_y)

            if step <= car.fuel:
                car.position = (new_x, new_y)
                car.fuel -= step


    def get_car_position(self, id):
        """Return the position of car <id> in the system.

        Return a tuple of the (x, y) position of the car.

        @type self: CarManager
        @type id: str
        @rtype: (int, int)
        """
        if id in self.cars:
            return self.cars[id].position

    def get_car_fuel(self, id):
        """Return the amount of fuel of car <id> in the system.

        @type self: CarManager
        @type id: str
        @rtype: int
        """
        if id in self.cars:
            return self.cars[id].fuel


class Car:
    """A car in the Super system.

    Fill in the attributes for this class!
    """
    # TODO: design and implement this class.
    
    def __init__(self, id, fuel):
        self.id = id
        self.fuel = fuel
        self.position = (0, 0)


