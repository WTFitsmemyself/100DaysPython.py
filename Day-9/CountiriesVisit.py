Nested_Dictionary = {
    "Cities_Visited": ["Paris", "Lille", "Dijon"]
}

travel_log = [
    {
    "France": Nested_Dictionary,
    "Germany": {"cities_visited2":["Berlin", "Hamburg", "Stuttgart"]}
    },
    {
    "Iran": Nested_Dictionary,
    "Kore": {"cities_visited2":["Berlin", "Hamburg", "Stuttgart"]}
    }
]

print(travel_log[1]) 
