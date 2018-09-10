"""
Locatel web scrapping
"""
import re
import os
import requests
from bs4 import BeautifulSoup
from utils import (end_notificacion, location_notification,
                   match_notification, check_notification,
                   save_into_text_file)

# Ask user input
PRODUCT_NAME = input('Ingrese el nombre del producto a buscar: ').lower()
ZONE_NAME = input('Ingrese el nombre del producto a buscar: ').lower()

# Prepare product name for query
PRODUCT = PRODUCT_NAME.replace(' ', '%20')
ZONE = ZONE_NAME.replace(' ', '%20')

# Set default searching zone
DEFAULT_ZONE = 'Venezuela'

# Prepare url to get product ids
LIST_API = 'https://www.farmatodo.com.ve/BuscadordeProductos.aspx?SearchQuery={}'.format(PRODUCT)

# Get html code
SOURCE = requests.get(LIST_API).text
# Convert code into into BS object
SOUP = BeautifulSoup(SOURCE, 'lxml')

# Get product matches
product_matches = SOUP.find_all('div', class_='moreInfo')
number_of_matches = len(product_matches)
match_notification(number_of_matches)

# Delete file if exists and create a new one
file_name = 'resultados_{}_{}_farmatodo.txt'.format(
    PRODUCT_NAME.replace(' ', '_'),
    ZONE_NAME.replace(' ', '_')
)
if os.path.exists(file_name):
    os.remove(file_name)
text_file = open(file_name, 'a')

# Set counters
count, found = 1, 0

# Loop over product matches
for item in product_matches:

    # Notify user actual step
    check_notification(count, number_of_matches)

    # Use regular expressions to extract product id and name from url
    product_url = re.search(
        r'ItemID=(?P<id>\d+)[a-zA-Z0-9&;=]+SearchQuery=(?P<name>[a-zA-Z0-9-.]+)',
        item.a.get('href')
    )
    product_id = product_url.group('id')
    product_name = product_url.group('name').replace('-', ' ')

    # Prepare detail api url
    DETAIL_API = 'https://www.farmatodo.com.ve/DetalledeProductos.aspx?ItemID={}&Zone={}'\
                    .format(product_id, ZONE if ZONE else DEFAULT_ZONE)
    # Get html code
    SOURCE = requests.get(DETAIL_API).text
    # Convert code into into BS object
    SOUP = BeautifulSoup(SOURCE, 'lxml')

    # Find all available locations
    addresses = [address.span.text for address in SOUP.find_all('div', class_='large-30')]
    if addresses:
        found += 1

    # Notify user if there is any location available
    location_notification(len(addresses))

    # Save result in text file
    save_into_text_file(product_name, addresses, text_file)

    count += 1

# Send notification to tell the user the process has finished
end_notificacion(found)

# Close file
text_file.close()
