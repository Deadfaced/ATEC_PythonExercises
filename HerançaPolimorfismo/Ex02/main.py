from movie import Movie

def main():
    movie_1 = Movie("Titanic", 1997)
    movie_2 = Movie("Matrix", 1999)
    
    print(movie_1)
    print(repr(movie_1))
    print([movie_1, movie_2])

if __name__ == "__main__":
    main()