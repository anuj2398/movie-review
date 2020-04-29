import imdb
x=imdb.IMDb()
movie_name=input("Enter the movie name:")
movies=x.search_movie(str(movie_name))
index=movies[0].getID()
movie=x.get_movie(index)
title=movie['title']
year=movie['year']
cast=movie['cast']
list_of_cast=','.join(map(str,cast))
print("title: ",title)
print("year of release: ",year)
print("full cast: ",list_of_cast)
for genre in movie['genres']:
    print("genre: ",genre)
