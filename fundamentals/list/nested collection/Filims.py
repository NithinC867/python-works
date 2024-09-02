movies = [
    # Malayalam Movies
    {
        "title": "Drishyam",
        "year": 2013,
        "language": "Malayalam",
        "genres": ["Crime", "Drama", "Thriller"],
        "rating": 8.6
    },
    {
        "title": "Premam",
        "year": 2015,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    {
        "title": "Bangalore Days",
        "year": 2014,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    # Tamil Movies
    {
        "title": "Kaala",
        "year": 2018,
        "language": "Tamil",
        "genres": ["Action", "Drama"],
        "rating": 7.3
    },
    {
        "title": "Vikram Vedha",
        "year": 2017,
        "language": "Tamil",
        "genres": ["Action", "Crime", "Thriller"],
        "rating": 8.4
    },
    {
        "title": "Super Deluxe",
        "year": 2019,
        "language": "Tamil",
        "genres": ["Drama", "Mystery", "Thriller"],
        "rating": 8.3
    },
    # Hindi Movies
    {
        "title": "Dangal",
        "year": 2016,
        "language": "Hindi",
        "genres": ["Action", "Biography", "Drama"],
        "rating": 8.4
    },
    {
        "title": "3 Idiots",
        "year": 2009,
        "language": "Hindi",
        "genres": ["Comedy", "Drama"],
        "rating": 8.4
    },
    {
        "title": "Gully Boy",
        "year": 2019,
        "language": "Hindi",
        "genres": ["Drama", "Music"],
        "rating": 8.0
    }
]


# total_movies=len(movies)
# print(total_movies)

# genres_filer=[g.get("title") for g in movies if "Drama" in g.get("genres")]
# print(genres_filer)

# def get_year(mov):
#     return mov.get("year")
# latest_movie_data=max(movies,key=get_year)
# latest_movies=[m.get("titile") for m in movies if m.get("year")==latest_movie_data.get("year")]
# print(latest_movies)


# def get_rating(mov):
#     return mov.get("rating")
# top_rated_movie=max(movies,key=get_rating)
# topratedmovies=[m.get("title") for m in movies if m.get("rating")==top_rated_movie.get("rating")]
# print(topratedmovies)


# malayalam_movies=[m.get("title") for m in movies if m.get("language")=="Malayalam"]
# print(malayalam_movies)

after_2016=[m.get("title") for m in movies if m.get("year")>=2016]
print(after_2016)