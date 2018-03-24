people = [
    {
        'name': "Maria",
        'interests': ['travel', 'dancing', 'swimming', 'movies'],
        'age': 24,
        'gender': "female",
        "ex": ["Kiril", "Petar"],
    },
    {
        'name': "Dayana",
        'interests': ['fashion', 'sport shooting', 'reading', 'сscandinavian literature'],
        'age': 21,
        'gender': "female",
        "ex": [],
    },
    {
        'name': "Darina",
        'interests': ['dancing', 'poker', 'history', 'software'],
        'age': 34,
        'gender': "female",
        "ex": ["Boris"],
    },
    {
        'name': "Liliya",
        'interests': ['poker', 'cars', 'dancing', 'movies'],
        'age': 36,
        'gender': "female",
        "ex": [],
    },
    {
        'name': "Galya",
        'interests': ['travel', 'cars', 'swimming', 'basketball'],
        'age': 18,
        'gender': "female",
        "ex": ['Dimitar'],
    },
    {
        'name': "Valeriya",
        'interests': ['swimming', 'poker', 'science', 'scandinavian literature'],
        'age': 27,
        'gender': "female",
        "ex": [],
    },
    {
        'name': "Inna",
        'interests': ['movies', 'hunting with falcons', 'swimming', 'fashion'],
        'age': 20,
        'gender': "female",
        "ex": [],
    },
    {
        'name': "Kiril",
        'interests': ['basketball', 'cars', 'movies', 'science'],
        'age': 19,
        'gender': "male",
        'ex': ["Maria"],
    },
    {
        'name': "Georgi",
        'interests': ['cars', 'football', 'swimming', 'dancing'],
        'age': 32,
        'gender': "male",
        'ex': [],
    },
    {
        'name': "Andrei",
        'interests': ['football', 'scandinavian literature', 'history', 'dancing'],
        'age': 26,
        'gender': "male",
        'ex': ["Maria"],
    },
    {
        'name': "Emil",
        'interests': ['flying', 'basketball', 'software', 'science'],
        'age': 34,
        'gender': "male",
        'ex': ['Darina'],
    },
    {
        'name': "Dimitar",
        'interests': ['football', 'hunting with falcons', 'cars', 'basketball'],
        'age': 22,
        'gender': "male",
        'ex': ['Galya'],
    },
    {
        'name': "Petar",
        'interests': ['travel', 'poker', 'basketball', 'hunting with falcons'],
        'age': 23,
        'gender': "male",
        'ex': ["Maria"],
    },
    {
        'name': "Kaloyan",
        'interests': ['movies', 'poker', 'travel', 'cars'],
        'age': 29,
        'gender': "male",
        'ex': [],
    },
]
i = 0
for person1 in people:
    i += 1
    for person2 in people[i:len(people)]:
        if person1["gender"] == person2["gender"]:
            continue
        elif abs(person1["age"] - person2["age"]) > 6:
            continue
        elif person1["name"] in person2["ex"]:
            continue
        else:
            person_one_interests = set(person1["interests"])
            person_two_interests = set(person2["interests"])
            if person_one_interests & person_two_interests:
                common_interests = person_one_interests & person_two_interests
                common_interests = ", ".join(common_interests)
                print(person1["name"], "(%d)"%person1["age"], "и", person2["name"], "(%d)"%person2["age"], "- common interests:", common_interests)
            else:
                continue
