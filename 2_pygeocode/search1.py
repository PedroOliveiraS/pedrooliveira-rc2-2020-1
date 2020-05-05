from geopy.geocoders import Nominatim

if __name__ == '__main__':
    address = 'Belarmino Vilela Junqueira, Ituiutaba, MG'
    user_agent = 'Search1'
    location = Nominatim(user_agent=user_agent).geocode(address, exactly_one=False)
    #print repr(location)
    print("Endereço buscado: " + address)

    for i in range(len(location)):
        print("Resultado " + str(i))
        print("     CEP" + str(location[i].address.split(",")[-2]))
        print("     (Latitude, Longitude) : (" + str(location[i].latitude) + " , " + str(location[i].longitude) + ")")
