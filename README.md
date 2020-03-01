# Movie_Filter_API
# Filtering movies according to genre using API

This project was meant for personal use and hence can be modified according to the requirement. 


I wanted to sort some unwatched movies according to their genre into different folders, but it was boring and tiredsome (around 90 - 100 movies) and I didn't knew overview of every movie. So, instead of searching genre of every movie on internet and then sorting them, I tried to automate this task using TMDB's API.


To register for an API key, click the [API Link](https://www.themoviedb.org/documentation/api) from within your account settings page. 


1. Click on your avatar or initials in the main navigation
2. Click the "Settings" link
3. Click the "API" link in the left sidebar 
4. Click "Create" or "click here" on the API page 

You can refer to the complete documentation [here](https://developers.themoviedb.org/3/getting-started/introduction)

Once you get the API, you need to install tmdbsimple, a python wrapper for tmdb v3 API.

# Installation

#### It can be easily installed using pip

```
pip install tmdbsimple
```

# Example

After getting API key and installing package, you can start experimenting

First import the library and provide the API Key

```
>>> import tmdbsimple as tmdb
>>> tmdb.API_KEY = 'YOUR_API_KEY_HERE'
```

In the next step, create a search instance and and call the results method:

```
>>> search = tmdb.Search()
>>> response = search.movie(query='Batman')
>>> search.results[0]:
...
...
{'popularity': 25.442,
 'vote_count': 13633,
 'video': False,
 'poster_path': '/dr6x4GyyegBWtinPBzipY02J2lV.jpg',
 'id': 272,
 'adult': False,
 'backdrop_path': '/9myrRcegWGGp24mpVfkD4zhUfhi.jpg',
 'original_language': 'en',
 'original_title': 'Batman Begins',
 'genre_ids': [28, 80, 18],
 'title': 'Batman Begins',
 'vote_average': 7.6,
 'overview': 'Driven by tragedy, billionaire Bruce Wayne dedicates his life to uncovering and defeating the corruption that plagues his home, Gotham City.  Unable to work within the system, he instead creates a new identity, a symbol of fear for the criminal underworld - The Batman.',
 'release_date': '2005-06-10'}
```

It will return a list of python dictionaries, you can extract any information you want.
Here, I am taking first element in list (as I only wanted to know the genre).

In 'genre_ids', it is giving list of integers representing different genre.
To get all the genre ids and names, just make a simple get request at 
```
https://api.themoviedb.org/3/genre/movie/list?api_key=<<api_key>>&language=en-US
```

replace <<api_key>> with your API Key.

It will return result in json format:
```
{"genres":[{"id":28,"name":"Action"},{"id":12,"name":"Adventure"},{"id":16,"name":"Animation"},{"id":35,"name":"Comedy"},{"id":80,"name":"Crime"},{"id":99,"name":"Documentary"},{"id":18,"name":"Drama"},{"id":10751,"name":"Family"},{"id":14,"name":"Fantasy"},{"id":36,"name":"History"},{"id":27,"name":"Horror"},{"id":10402,"name":"Music"},{"id":9648,"name":"Mystery"},{"id":10749,"name":"Romance"},{"id":878,"name":"Science Fiction"},{"id":10770,"name":"TV Movie"},{"id":53,"name":"Thriller"},{"id":10752,"name":"War"},{"id":37,"name":"Western"}]}

```

## Source :-

https://www.themoviedb.org/documentation/api

https://pypi.org/project/tmdbsimple/

```
Note - API used in this project is for personal and non-commercial use only.
For commercial use, read TMDB's terms and conditions.
```
