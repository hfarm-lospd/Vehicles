from fleet import print_vehicle_types, get_vehicle_count

if __name__ == "__main__":

    print("-" * 50)
    print_vehicle_types()

    print("-" * 50)
    get_vehicle_count("moto", "ITALIA NORD-OCCIDENTALE", "Fino a 125", "0")
    get_vehicle_count("bus", "ITALIA NORD-ORIENTALE", "Privato", "1")
    get_vehicle_count("moto", "ITALIA NORD-ORIENTALE", "Privato", "0")