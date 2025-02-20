from enum import Enum

class GeoPoliticalZone(Enum):
    NORTH_CENTRAL = ["Benue", "FCT", "Kogi", "Kwara", "Nasarawa", "Niger", "Plateau"]
    NORTH_EAST = ["Adamawa", "Bauchi", "Borno", "Gombe", "Taraba", "Yobe"]
    NORTH_WEST = ["Kaduna", "Katsina", "Kano", "Kebbi", "Sokoto", "Jigawa", "Zamfara"]
    SOUTH_EAST = ["Anambra", "Abia", "Ebonyi", "Enugu", "Imo"]
    SOUTH_WEST = ["Ekiti", "Lagos", "Osun", "Ondo", "Ogun", "Oyo"]
    SOUTH_SOUTH = ["Akwa-Ibom", "Bayelsa", "Cross_River", "Delta", "Edo", "Rivers"]

def get_geo_political_zone(state):

    for zone in GeoPoliticalZone:
        if state in zone.value:
            return zone.name

    return None

print(get_geo_political_zone("Anambra"))