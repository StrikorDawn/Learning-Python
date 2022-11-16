movies = [
    "Batman",
    "Princess Bride"
]

removed_list = []


movies.append("Avengers")
movies.insert(1, "Batman Begins")
movies.insert(len(movies), 'Knives out')




#Removing items
removed = movies.pop(3)
removed_list.append(movies.pop(3))
movies.remove('batman')
# Is very specific with casing and spelling, does not deal with indexing. 
to_remove = movies[0]
movies.remove(to_remove)

# Changeing things
movies[1] = 'Iron Man'




print("Movies: ")
for movie in movies:
    print(f"\t- {movie}")


