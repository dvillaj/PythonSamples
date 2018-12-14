def get_formatted_city_data(ciudad, pais):
    """Genera el nombre de la ciudad seguido del pais"""
    city_data = ciudad + ", " + pais
    return city_data.title()

def get_formatted_city_data(ciudad, pais, poblacion=""):
    """Genera el nombre de la ciudad seguido del pais"""
    if poblacion:
        city_data = ciudad + ", " + pais + ", poblacion: " + str(poblacion)
    else:
        city_data = ciudad + ", " + pais
    return city_data.title()
