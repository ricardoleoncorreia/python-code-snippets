"""
Sets logging config and creates the vehicule class
Console will show 
"""
import logging

# Create logger
LOGGER = logging.getLogger(__name__)
# Set minimum level to log
LOGGER.setLevel(logging.DEBUG)

# Create base formatter
FORMATTER = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

# Create the file handler
FILE_HANDLER = logging.FileHandler('car.log')
# Set minimum level to log
FILE_HANDLER.setLevel(logging.WARNING)
# Set formatter to file handler
FILE_HANDLER.setFormatter(FORMATTER)

# Create Stream Handler
STREAM_HANDLER = logging.StreamHandler()
# Set formatter to the Stream Handler
STREAM_HANDLER.setFormatter(FORMATTER)

# Add handlers to logger
LOGGER.addHandler(FILE_HANDLER)
LOGGER.addHandler(STREAM_HANDLER)


class Vehicule:
    """
    Creates an object Vehicule given a brand and a model
    """

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.sold = False
        self.crashed = False
        self.gas_tank = 0
        LOGGER.debug('A car was created: %s - %s', self.brand, self.model)

    def fill_tank(self, liters):
        """
        Fills the gas tank
        """
        self.gas_tank += liters
        LOGGER.info('%s - %s was filled with %s liters', self.brand, self.model, str(liters))

    def was_sold(self):
        """
        Indicates if a vehicule has been sold
        """
        self.sold = True
        LOGGER.warning('%s - %s was sold', self.brand, self.model)

    def empty_tank(self):
        """
        Empty the tank level
        """
        self.gas_tank = 0
        LOGGER.error('%s - %s tank is empty', self.brand, self.model)

    def was_crashed(self):
        """
        Crashes the car
        """
        self.crashed = True
        LOGGER.critical('%s - %s crashed', self.brand, self.model)
