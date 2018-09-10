"""
Functions to support main file
"""

def end_notificacion(found):
    """
    Sends a notification with the number of found products
    """
    print('Revision finalizada.', end=' ')
    if found == 0:
        print('No se localizó ningún producto')
    elif found == 1:
        print('Se localizó un producto')
    else:
        print('Se localizaron {} productos'.format(found))


def location_notification(length):
    """
    Sends a notification with the number of found drugstores
    """
    if length == 0:
        print('No se encontró ninguna farmacia')
    elif length == 1:
        print('Se encontró una farmacia')
    else:
        print('Se encontraron {} farmacias'.format(length))


def match_notification(matches):
    """
    Sends a notification with the number of matches
    """
    print('Se encontraron {} coincidencias'.format(matches))


def check_notification(count, matches):
    """
    Sends a notification for each found product to notify the user
    the progress of the searching process
    """
    print('Revisando coincidencia {}/{}'.format(count, matches), end=': ')


def save_into_text_file(product_name, addresses, text_file):
    """
    Save process info into txt file
    """
    text_file.write(product_name + '\n')
    if addresses:
        for address in addresses:
            text_file.write(address + '\n')
    else:
        text_file.write('Producto no disponible\n')
    text_file.write('\n')
