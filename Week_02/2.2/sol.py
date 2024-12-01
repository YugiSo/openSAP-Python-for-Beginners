# Week 2 - Unit 2: Exercise

star_wars_movies = [
    ["The Phantom Menace", "Attack of the Clones", "Revenge of the Sith"],
    ["A New Hope", "The Empire Strikes Back", "Return of the Jedi"],
    ["The Force Awakens", "The Last Jedi", "The Rise of Skywalker"],
]

trilogy = int(input("Enter Trilogy: "))
trilogy_film = int(input("Enter Film in Trilogy: "))

print(f'Title: {star_wars_movies[trilogy - 1][trilogy_film - 1]}')