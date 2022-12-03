
movies = []
movie_votes = []
total_votes = 0
hit_movie = ''
hit_movie_votes = 0
flop_movie = ''
flop_movie_votes = 99999

with open('data3.txt') as file:
    header = file.readline()
    for line in file:
        parts = line.strip().split(',')
        title = parts[0].strip()
        genre = parts[1].strip()
        votes = float(parts[2].strip())


        total_votes += votes

        if hit_movie_votes < votes:
            hit_movie_votes = votes
            hit_movie = title

        if flop_movie_votes > votes:
            flop_movie_votes = votes
            flop_movie = title

        if title not in movies:
            movies.append(title)
            movie_votes.append(votes) 
        else:
            movie_index = movies.index(title)
            movie_votes[movie_index] += votes

print(f'Extracted Movie Data (total votes found: {total_votes}):')
for i in range(len(movies)):
    print(f' {movies[i]} - {movie_votes[i]}')

print()
print(f'Hit movie {hit_movie} with {hit_movie_votes}')
print()
print(f'Flop movie {flop_movie} with {flop_movie_votes}')