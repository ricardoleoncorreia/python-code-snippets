"""
Executes vehicule logging testing
"""
from vehicule import Vehicule

# Create vehicules
HILUX = Vehicule('Toyota', 'Hilux')
AVEO = Vehicule('Chevrolet', 'Aveo')
CIVIC = Vehicule('Honda', 'Civic')
CHEROKEE = Vehicule('Jeep', 'Cherokee')

# Fill tanks
HILUX.fill_tank(40)
AVEO.fill_tank(20)
CIVIC.fill_tank(20)
CHEROKEE.fill_tank(40)

# Vehicules that were sold
HILUX.was_sold()
AVEO.was_sold()
CIVIC.was_sold()

# Empty tank
AVEO.empty_tank()

# One vehicule was crashed
CIVIC.was_crashed()
