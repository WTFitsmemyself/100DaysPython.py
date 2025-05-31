travel_log =[
    {
        "country": "France",
        "visits": 12,
        "cities": ["Lille", "Paris", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]       
    },
]

country = input("Enter the name of the country: ")
Visit = int(input("Enter the number of visits: "))
Cities = input("Enter the cities(Seperate cities with ','): ").split(",")

def add_new_country(NameOfCountry, VisitedTimes, CitiesYouVisit):
    length_travel_log = len(travel_log)
    travel_log.append({
        "country": NameOfCountry,
        "visits": VisitedTimes,
        "cities": CitiesYouVisit,
    })
    countrySelectedFirst = travel_log[length_travel_log]
    countryFinal = countrySelectedFirst["country"]
    VisitFinal = countrySelectedFirst["visits"]
    CitiesFinal = countrySelectedFirst["cities"]
    print(f"You've visited {countryFinal} {VisitFinal} times.")
    print(f"You've been to {CitiesFinal[0]} and {CitiesFinal[1]}")

add_new_country(country,Visit,Cities)
