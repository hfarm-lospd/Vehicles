# Here we have some toy data
# Toy nested dictionary data using direct shorthand keys
vehicles = {
    "moto": {
        "ITALIA NORD-OCCIDENTALE": {
            "Fino a 125": {"0": 198580, "1": 48882},
            "126 - 250": {"0": 134064, "1": 60332},
            "251 - 750": {"0": 178233, "1": 55234},
            "Oltre 750": {"0": 51039, "1": 39103}
        },
        "ITALIA NORD-ORIENTALE": {
            "Fino a 125": {"0": 159880, "1": 38063},
            "126 - 250": {"0": 95346, "1": 36822},
            "251 - 750": {"0": 135378, "1": 38650},
            "Oltre 750": {"0": 43082, "1": 35582}
        }
    },
    "bus": {
        "ITALIA NORD-OCCIDENTALE": {
            "Noleggio": {"0": 240, "1": 51, "5B": 120, "6B": 45},
            "Privato": {"0": 433, "1": 83},
            "Pubblico": {"0": 404, "1": 31},
            "Altri usi": {"0": 53, "1": 2}
        },
        "ITALIA NORD-ORIENTALE": {
            "Noleggio": {"0": 270, "1": 81},
            "Privato": {"0": 278, "1": 59},
            "Pubblico": {"0": 272, "1": 19},
            "Altri usi": {"0": 19, "1": 7}
        }
    }
}

def print_vehicle_types():
    '''Prints the available vehicle types'''
    print('Welcome to the fleet data set. We have data for these vehicle types:')
    for v_type in vehicles:
        print(f"- {v_type}")
        
def get_vehicle_count(vehicle_type, area, category, euro_standard):
    '''Returns the number of vehicles for a given type, area, category, and euro standard'''
    try:
        count = vehicles[vehicle_type][area][category][euro_standard]
        print(f"There are {count} {vehicle_type} vehicles in {area} (Category: {category}, Euro std: {euro_standard}).")
    except KeyError:
        print("Sadly, we don't have data for that specific combination.")
