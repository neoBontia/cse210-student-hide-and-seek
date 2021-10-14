import random

class Hider:
    """"A code template for a the hider. The responsibility of 
    this class of objects is to spicify a location that the 
    seeker has to guess and give hints to the seeker according
    to its distance from the hider.
    
    Stereotype:
        Information Holder
        Service Provider

    Attributes:
        location (integer): The location of the Hider (1-1000).
        distance (list): The distance between the hider and seeker.
    
    """
    
    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Hider): An instance of Hider.
        """
        self.location = random.randint(1, 1000)
        self.distance = [1000]

    def get_hint(self):
        """Returns a hint that depends on whether or not the seeker has moved
        closer or farther away. This is determined by inspecting the last two
        distances contained in the distance attribute.

        Args:
            self (Hider): An instance of Hider.

        Returns:
            string: A message from the hider.
        """
        message = "Find me if you can!"
        if self.distance[-1] == 0:
            message = "You found me!"
        elif self.distance[-1] < self.distance[-2]:
            message = "Getting warmer!"
        elif self.distance[-1] > self.distance[-2]:
            message = "Getting colder!"
        return message


    def watch(self, location):
        """Keeps track of how far away the seeker is by calculating the
        difference between their locations. The distance is appended to the
        corresponding attribute for later use.
        
        Args:
            self (Hider): An instance of Hider.
            location (number): The location of the seeker.
        """
        difference = abs(self.location-location)
        self.distance.append(difference)
