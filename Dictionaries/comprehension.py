# Video - Python dictionary comprehension (25 Jan. 2021)
# Channel - Bro Code

# -------------------------------------------------------------------------
# dictionary = {key: expression for (key,value) in iterable}

cities_in_F = {'New York': 32,
                'Boston': 75,
                'Los Angeles': 100,
                'Chigaco': 50}

cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C) # {'New York': 0, 'Boston': 24, 'Los Angeles': 38, 'Chigaco': 10}


# -------------------------------------------------------------------------
# dictionary = {key: expression for (key,value) in iterable if conditional}

weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}

sunny_weather = {key: value for (key, value) in weather.items() if value == 'sunny'}
print(sunny_weather) # {'Boston': 'sunny', 'Los Angeles': 'sunny'}


# -------------------------------------------------------------------------
# dictionary = {key: (if/else) for (key,value) in iterable}

cities = {'New York': 0, 'Boston': 24, 'Los Angeles': 38, 'Chigaco': 10}
desc_cities = {key: ("warm" if value >= 20 else "cold") for (key,value) in cities.items()}
print(desc_cities) # {'New York': 'cold', 'Boston': 'warm', 'Los Angeles': 'warm', 'Chigaco': 'cold'}


# -------------------------------------------------------------------------
# dictionary = {key: function(value) for (key,value) in iterable}

def check_temp(value):
    if value >= 30:
        return "WARM"
    elif value  >= 10:
        return "warm"
    else:
        return "cold"
    
cities = {'New York': 0, 'Boston': 24, 'Los Angeles': 38, 'Chigaco': 10}
desc_cities2 = {key: check_temp(value) for (key,value) in cities.items()}
print(desc_cities2) # {'New York': 'cold', 'Boston': 'warm', 'Los Angeles': 'WARM', 'Chigaco': 'warm'}